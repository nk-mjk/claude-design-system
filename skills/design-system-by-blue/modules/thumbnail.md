# modules/thumbnail.md — ShowCase B (썸네일) 생성 플로우

> 진입 경로:
>   - create.md / update.md 쇼케이스 제안 → "ShowCase B" 또는 "둘 다" 선택
>   - 사용자가 "썸네일 만들어줘", "썸네일 이미지 만들어줘" 등 직접 트리거

---

## Step 1 — bds_ 파일 확인

같은 대화에서 방금 생성/수정한 경우 → 토큰 데이터 이미 메모리에 있음. 탐색 생략.

그 외 → `modules/common.md` 참조해 작업 폴더에서 bds_ 탐색:
- 1개 → 바로 사용
- 여러 개 → AskUserQuestion으로 파일 선택
- 0개 → "먼저 디자인 스타일을 만들어주세요." 안내 후 modules/create.md로 연결

---

## Step 2 — 웹폰트 URL 결정

bds_ 파일의 `heading_font` / `body_font` 값으로 CDN URL을 결정한다.
`heading_font`가 없으면 `font_name`(구 bds_)으로 폴백.
**로컬 폰트 탐색 없음. font.md 호출 없음.**

폰트 종류에 따라 로딩 방식이 다르다 — Google Fonts·일부 jsDelivr CSS 파일은 `<link>` 태그로 OK, **눈누(woff/woff2 직접 URL) 폰트는 inline `@font-face` 블록이 필수**다.

`get_webfont_url()` 함수의 전체 구현은 **`modules/showcase_a.md` Step 2와 완전히 동일하다.** thumbnail.md 단독 실행 시에도 그 함수를 그대로 옮겨 쓴다. (반환: `(url, kind, css_family)` 튜플)

```python
# get_webfont_url 구현은 showcase_a.md Step 2 참조
# heading_font / body_font 분리 (구 bds_는 font_name 단일값)
heading_font = bds_data.get('heading_font') or bds_data.get('font_name', 'Pretendard')
body_font    = bds_data.get('body_font')    or heading_font
same_font    = (heading_font == body_font)

heading_url, heading_kind, heading_family = get_webfont_url(heading_font)
if same_font:
    body_url, body_kind, body_family = None, None, heading_family
else:
    body_url, body_kind, body_family = get_webfont_url(body_font)
```

> **css_family 정규화**: 사용자 입력이 "KCC환기체"라도 `heading_family`는 `'KCCHwangi'`로 반환된다. 템플릿 치환 시 `[FONT_FAMILY]` / `[BODY_FONT_FAMILY]`에는 **`heading_family` / `body_family` 값**을 사용해야 inline `@font-face` 선언과 일치한다.

---

## Step 3 — HTML 썸네일 생성

`references/thumbnail-template.md`를 읽고, HTML 템플릿의 플레이스홀더를 bds_ 토큰값으로 치환해 HTML 파일을 생성한다.

**폰트 플레이스홀더 치환 (css_family 정규화 값 사용):**
- `[FONT_FAMILY]` → `heading_family` (제목·히어로·버튼)
- `[BODY_FONT_FAMILY]` → `body_family` (본문·캡션·카드 body)
- `same_font`이면 두 플레이스홀더에 같은 값 (`heading_family`)
- `[FONT_NAME]` → `font_display` (heading ≠ body면 `"Heading / Body"` 형식)

**웹폰트 주입 — kind에 따라 분기:**

```python
def _font_block(url, kind, family):
    """showcase_a.md Step 4와 동일한 헬퍼."""
    if kind == 'link':
        return f'<link rel="stylesheet" href="{url}">\n'
    fmt = 'woff2' if url.endswith('.woff2') else 'woff'
    return (
        '<style>\n'
        f"@font-face {{ font-family: '{family}'; "
        f"src: url('{url}') format('{fmt}'); "
        "font-weight: 400; font-style: normal; }\n"
        f"@font-face {{ font-family: '{family}'; "
        f"src: url('{url}') format('{fmt}'); "
        "font-weight: 700; font-style: normal; }\n"
        '</style>\n'
    )

webfont_block = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
)
webfont_block += _font_block(heading_url, heading_kind, heading_family)
if not same_font:
    webfont_block += _font_block(body_url, body_kind, body_family)
# NKR fallback은 template에 이미 들어있어 중복 추가하지 않는다.
```

생성된 `webfont_block`을 템플릿의 `</head>` 바로 앞에 삽입한다:
```python
html = template.replace('</head>', webfont_block + '</head>', 1)
```

HTML 템플릿에 적용하는 폰트 CSS — heading/body 구분 (이미 template에 반영됨):
```css
/* heading 폰트: Display~Heading 4 */
.hero-title, h1, h2, h3, h4 { font-family: '[FONT_FAMILY]', 'Noto Sans KR', sans-serif; }
/* body 폰트: 나머지 전체 */
body { font-family: '[BODY_FONT_FAMILY]', 'Noto Sans KR', sans-serif; }
```

카드 구조 (680×680px):
- **히어로 헤더** (height: 150px 고정, overflow: hidden): Primary 컬러 배경 + 브랜드명 + Primary HEX + 폰트·모드 뱃지. 높이를 고정해야 디자인 시스템마다 폰트 렌더링 차이로 레이아웃이 흔들리는 문제를 방지할 수 있다. 콘텐츠가 많아도 잘려 들어간다.
- Primary 틴트 스트립 (10칸, 50~900 라벨, 500 굵게)
- Neutral 팔레트 스트립 (6칸, 100~900 라벨)
- Brand 스와치 3개 (Primary / Secondary / Accent)
- 실선 구분선
- Neutral 스와치 3개 (100 / 500 / 900)
- 타이포그래피 샘플 (Heading + Body + Caption), flex:1 로 남은 공간 채움
- 버튼 2개 (적용하기 / 미리보기)

PNG 다운로드: html2canvas scale:2 캡처 후 40px 패딩 추가 → 1440×1440px 정사각형.

---

## Step 4 — 파일 저장 및 전달

1. 파일명: `bds_[BRAND_NAME_SAFE]-showcase_b.html`
2. 저장 위치: bds_ 파일과 같은 폴더 (별도 확인 불필요)
3. 저장 완료 후 computer:// 링크 제공:

```
썸네일 HTML을 만들었어요. 파일을 열고 "PNG 다운로드" 버튼을 누르면 이미지로 저장돼요.
[bds_[BRAND_NAME_SAFE]-showcase_b.html 열기](computer://[절대경로])
```

> 브라우저에서 열어야 html2canvas가 작동하고 PNG 저장이 가능하다는 점을 함께 안내한다.
> 웹폰트가 적용되려면 온라인 상태에서 열어야 한다.
