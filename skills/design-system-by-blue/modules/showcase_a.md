# modules/showcase_a.md — ShowCase A (상세 가이드) 생성 모듈

> **진입 경로:**
>   - 경로 A: create.md / update.md 쇼케이스 제안 → "ShowCase A" 또는 "둘 다" 선택
>   - 경로 B: 사용자가 "디자인 가이드 만들어줘", "쇼케이스 A 만들어줘", "PDF로 뽑아줘" 등 직접 요청
>
> **출력물:** `showcase_a_[브랜드명].html` — 브라우저에서 열어 PNG 저장 또는 인쇄(PDF)

---

## 진입 직후 — bds_ 파일 확인

**경로 A (방금 생성/수정한 경우)**: 토큰이 이미 메모리에 있음 → 파일 탐색 없이 Step 2로 바로 이동.

**경로 B (직접 트리거)**: 작업 폴더에서 bds_ 파일을 탐색한다 (modules/common.md 참조).
- 1개 → 바로 사용
- 여러 개 → "어떤 스타일의 ShowCase를 만들까요?" AskUserQuestion으로 선택
- 0개 → "먼저 디자인 스타일을 만들어야 해요. 지금 만들어드릴까요?" → modules/create.md로

---

## Step 1 — 의존성 확인 (경량)

playwright, pypdf 불필요. generate_combined_html() 사용을 위해 스크립트 경로만 확인.

```bash
python3 -c "
import glob, sys
# 스킬 스크립트 경로 동적 감지
candidates = glob.glob('/sessions/*/mnt/.claude/skills/design-system-by-blue/scripts')
if candidates:
    sys.path.insert(0, candidates[0])
    from generate_ds_html import generate_combined_html
    print('OK')
else:
    print('SCRIPT_NOT_FOUND')
"
```

`SCRIPT_NOT_FOUND`이면: "스킬 스크립트를 찾지 못했어요. 스킬이 올바르게 설치됐는지 확인해주세요." 안내 후 중단.

---

## Step 2 — 웹폰트 URL 결정

bds_ 파일의 `heading_font` / `body_font` 값으로 CDN URL을 결정한다.
`heading_font`가 없으면 `font_name`(구 bds_)으로 폴백.
**로컬 폰트 탐색 없음. font.md 호출 없음.**

폰트 종류에 따라 로딩 방식이 다르다 — Google Fonts·일부 jsDelivr CSS 파일은 `<link>` 태그로 OK, **눈누(woff/woff2 직접 URL) 폰트는 inline `@font-face` 블록이 필수**다. 이 분기를 함수에서 함께 처리한다.

```python
def get_webfont_url(font_name):
    """font_name → (url, kind, css_family) 반환.
    - kind='link': CSS URL → <link rel="stylesheet">로 주입
    - kind='face': woff/woff2 직접 URL → inline @font-face 블록으로 주입
    - css_family: HTML에서 실제 사용할 font-family 값 (한글 별칭은 영문 family로 정규화)
    """
    # ── CSS 파일 URL (link로 로드) ─────────────────────────────────
    css_fonts = {
        'Pretendard':            'https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.css',
        'SUIT':                  'https://cdn.jsdelivr.net/gh/orioncactus/suit@v1.0.3/dist/variable/SUITVariable.css',
        'SUITE':                 'https://cdn.jsdelivr.net/gh/sun-typeface/SUITE@2/fonts/variable/woff2/SUITE-Variable.css',
        'Wanted Sans':           'https://cdn.jsdelivr.net/gh/wanteddev/wanted-sans@v1.0.3/packages/wanted-sans/fonts/webfonts/variable/split/WantedSansVariable.min.css',
        'LINE Seed Sans KR':     'https://cdn.jsdelivr.net/npm/@kfonts/line-seed-sans-kr@latest/index.css',
        'Spoqa Han Sans Neo':    'https://cdn.jsdelivr.net/npm/spoqa-han-sans@latest/css/SpoqaHanSansNeo.css',
        'NanumSquare Neo':       'https://cdn.jsdelivr.net/gh/moonspam/NanumSquareNeo@1.0/nanumsquareneovar.css',
        'Seoul Namsan':          'https://cdn.jsdelivr.net/gh/fonts-archive/SeoulNamsan/subsets/SeoulNamsan-dynamic-subset.css',
        'BM Hanna Pro':          'https://cdn.jsdelivr.net/npm/@kfonts/bm-hanna-pro-otf@latest/index.css',
        'BM Hanna Air':          'https://cdn.jsdelivr.net/npm/@kfonts/bm-hanna-air-otf@latest/index.css',
        'KoPubWorld Batang':     'https://cdn.jsdelivr.net/npm/font-kopubworld@1.0/batang.min.css',
        'KoPubWorld Dotum':      'https://cdn.jsdelivr.net/npm/font-kopubworld@1.0/dotum.min.css',
        'BM Euljiro':            'https://cdn.jsdelivr.net/npm/@kfonts/bm-euljiro@latest/index.css',
        'BM Euljiro 10 Years Later': 'https://cdn.jsdelivr.net/npm/@kfonts/bm-euljiro-10years-later@latest/index.css',
        'Galmuri11':             'https://cdn.jsdelivr.net/npm/galmuri/dist/galmuri.css',
        'D2Coding':              'https://cdn.jsdelivr.net/gh/Joungkyun/font-d2coding/d2coding.css',
    }
    css_aliases = {
        'BM 한나체 Pro':       'BM Hanna Pro',
        'BM 한나에어':         'BM Hanna Air',
        'BM 을지로체':         'BM Euljiro',
        'BM 을지로10년후체':   'BM Euljiro 10 Years Later',
    }
    # ── 눈누 woff/woff2 직접 URL (inline @font-face 필요) ──────────
    face_fonts = {
        'Binggrae':                'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/Binggrae.woff',
        'BinggraeSamanco':         'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-10@1.0/BinggraeSamanco.woff',
        'KCCGanpan':               'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/KCC-Ganpan.woff2',
        'Cafe24Shiningstar':       'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.1/Cafe24Shiningstar.woff',
        'KyoboHandwriting2024psw': 'https://cdn.jsdelivr.net/gh/projectnoonnu/2507-1@1.0/KyoboHandwriting2024psw.woff2',
        'Cafe24Ohsquare':          'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/Cafe24Ohsquare.woff',
        'GangwonState':            'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2307-2@1.0/GangwonState.woff2',
        'ChosunGs':                'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@1.0/ChosunGs.woff',
        'ChosunilboMyungjo':       'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/Chosunilbo_myungjo.woff',
        'KOMACON':                 'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_seven@1.2/KOMACON.woff',
        'YanoljaYache':            'https://gcore.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/YanoljaYacheR.woff',
        'BMJUA':                   'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/BMJUA.woff',
        'BMEuljirooraeorae':       'https://gcore.jsdelivr.net/gh/projectnoonnu/noonfonts_2110@1.0/BMEuljirooraeorae.woff2',
        'DOSGothic':               'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_eight@1.0/DOSGothic.woff',
        'DungGeunMo':              'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/DungGeunMo.woff',
        'ChosunCentennial':        'https://gcore.jsdelivr.net/gh/projectnoonnu/noonfonts_2206-02@1.0/ChosunCentennial.woff2',
        'KCCKimHoon':              'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/KCCKimHoon.woff2',
        'KCCAnJungGeun':           'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/KCCAnJungGeun.woff2',
        'KCCHwangi':               'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/KCCHwangi.woff2',
        'MapoMaponaruA':           'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoMaponaruA.woff',
        'GabiaBombaram':           'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/GabiaBombaram.woff',
        'BMKIRANGHAERANG':         'https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/BMKIRANGHAERANG.woff',
    }
    face_aliases = {
        '빙그레체':              'Binggrae',
        '빙그레 싸만코체':       'BinggraeSamanco',
        'KCC간판체':             'KCCGanpan',
        '카페24 빛나는별':       'Cafe24Shiningstar',
        '교보손글씨2024 박서우': 'KyoboHandwriting2024psw',
        '카페24 아네모네':       'Cafe24Ohsquare',
        '강원특별자치도체':      'GangwonState',
        '조선궁서체':            'ChosunGs',
        '조선일보명조체':        'ChosunilboMyungjo',
        '만화진흥원체':          'KOMACON',
        '야놀자야체':            'YanoljaYache',
        '주아체':                'BMJUA',
        '을지로오래오래체':      'BMEuljirooraeorae',
        '도스고딕':              'DOSGothic',
        '둥근모꼴Fixedsys':      'DungGeunMo',
        '둥근모꼴':              'DungGeunMo',
        '조선100년체':           'ChosunCentennial',
        'KCC김훈체':             'KCCKimHoon',
        'KCC안중근체':           'KCCAnJungGeun',
        'KCC환기체':             'KCCHwangi',
        '마포마포나루':          'MapoMaponaruA',
        '가비아 봄바람체':       'GabiaBombaram',
        '기랑해랑체':            'BMKIRANGHAERANG',
    }

    # 1) 직접 매칭
    if font_name in css_fonts:
        return css_fonts[font_name], 'link', font_name
    if font_name in face_fonts:
        return face_fonts[font_name], 'face', font_name
    # 2) 한글 별칭 → 정규화된 영문 family로 변환
    if font_name in css_aliases:
        canonical = css_aliases[font_name]
        return css_fonts[canonical], 'link', canonical
    if font_name in face_aliases:
        canonical = face_aliases[font_name]
        return face_fonts[canonical], 'face', canonical
    # 3) 그 외 → Google Fonts 시도 (없으면 시스템 폰트로 fallback)
    family_param = font_name.replace(' ', '+')
    google_url = f"https://fonts.googleapis.com/css2?family={family_param}:wght@400;700&display=swap"
    return google_url, 'link', font_name


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

> **css_family 정규화 주의**: 사용자가 "KCC환기체"로 입력해도 css_family는 `'KCCHwangi'`로 반환된다. **brand_config의 `heading_font`/`body_font` 값을 css_family로 갱신해야** 본문 HTML의 `font-family:'{heading_font}'` 선언이 실제 로드된 폰트와 일치한다 (Step 3에서 처리).

NKR fallback(한글 비상용)도 함께 로드:
```python
nkr_url = "https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap"
# heading_font 또는 body_font가 Noto Sans KR이면 nkr_url 중복 로드 생략
nkr_fonts = {heading_font, body_font, heading_family, body_family}
```

---

## Step 3 — brand_config 구성

`references/brand-config-schema.md`의 키 매핑표에 따라 bds_ 파일을 Python dict로 변환한다.

**웹폰트 전환 핵심 설정 (css_family로 정규화):**
사용자가 한글 별칭("KCC환기체")으로 입력해도 실제 CSS에서는 영문 family("KCCHwangi")로 선언된다.
brand_config의 `heading_font`/`body_font` 값을 Step 2에서 반환된 `heading_family`/`body_family`로 갱신해 본문 HTML의 `font-family` 선언이 실제 로드된 폰트와 일치하도록 한다.

```python
# heading 폰트 (CDN 사용 → 로컬 파일 없음)
brand_config['heading_font'] = heading_family    # css_family로 정규화
brand_config['font_files'] = {
    'family':  heading_family,
    'regular': None,   # 로컬 파일 없음 → @font-face src 비워짐 → CDN이 대체
    'bold':    None,
}

# body 폰트 (heading과 다를 때만 — same_font일 때는 동일 값)
brand_config['body_font'] = body_family
if not same_font:
    brand_config['body_font_files'] = {
        'family':  body_family,
        'regular': None,
        'bold':    None,
    }
```

> `generate_combined_html()`은 `font_files.regular`가 None이면 `@font-face src: url('')`를 생성한다.
> 이 빈 선언이 CDN 폰트보다 먼저 `<style>`에 심어지면 CDN 폰트를 덮어버린다.
> Step 4에서 `re.sub`으로 빈 `@font-face` 선언을 제거해 CDN 폰트가 정상 적용되도록 한다.

---

## Step 4 — ShowCase A HTML 생성

```python
import glob, sys, re

# 스크립트 경로
candidates = glob.glob('/sessions/*/mnt/.claude/skills/design-system-by-blue/scripts')
sys.path.insert(0, candidates[0])
from generate_ds_html import generate_combined_html

# fonts_dir: 로컬 폰트 불필요 → 존재하지 않는 경로 전달 (find_font 결과 None → 빈 src)
html_str = generate_combined_html(brand_config, fonts_dir='/tmp/_no_local_fonts')

# ── 웹폰트 주입 (</head> 바로 앞) ─────────────────────────────────
# kind에 따라 분기:
#   - 'link': Google Fonts·jsDelivr CSS URL → <link rel="stylesheet">
#   - 'face': 눈누 woff/woff2 직접 URL → inline <style>@font-face</style>
def _font_block(url, kind, family):
    if kind == 'link':
        return f'  <link rel="stylesheet" href="{url}">\n'
    # face: 확장자 감지 후 inline @font-face
    fmt = 'woff2' if url.endswith('.woff2') else 'woff'
    return (
        '  <style>\n'
        f"  @font-face {{ font-family: '{family}'; "
        f"src: url('{url}') format('{fmt}'); "
        "font-weight: 400; font-style: normal; }\n"
        f"  @font-face {{ font-family: '{family}'; "
        f"src: url('{url}') format('{fmt}'); "
        "font-weight: 700; font-style: normal; }\n"
        '  </style>\n'
    )

webfont_links = (
    '  <link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
)
webfont_links += _font_block(heading_url, heading_kind, heading_family)
if not same_font:
    webfont_links += _font_block(body_url, body_kind, body_family)

# NKR fallback — heading/body 중 Noto Sans KR이 없을 때만 추가
if 'Noto Sans KR' not in nkr_fonts and 'Noto+Sans+KR' not in nkr_fonts:
    webfont_links += f'  <link rel="stylesheet" href="{nkr_url}">\n'

html_str = html_str.replace('</head>', webfont_links + '</head>', 1)

# ── 컨트롤 바 주입 (<body> 바로 뒤) ───────────────────────────────────
primary_color = brand_config['primary']
primary_on    = brand_config.get('primary_on', '#FFFFFF')  # 버튼 텍스트 색

control_bar = f"""
<div id="ctrl" style="
  position:fixed; top:0; left:0; right:0; z-index:9999;
  display:flex; align-items:center; gap:10px; padding:8px 16px;
  background:rgba(255,255,255,0.92); backdrop-filter:blur(6px);
  border-bottom:1px solid #e0e0e0; font-family:sans-serif; font-size:13px;
">
  <span style="font-weight:600; color:#333; margin-right:4px;">ShowCase A</span>
  <button onclick="downloadPage(1)" style="
    background:{primary_color}; color:{primary_on}; border:none; border-radius:6px;
    padding:6px 14px; cursor:pointer; font-size:13px; font-weight:600;
  ">⬇ Page 1 PNG</button>
  <button onclick="downloadPage(2)" style="
    background:{primary_color}; color:{primary_on}; border:none; border-radius:6px;
    padding:6px 14px; cursor:pointer; font-size:13px; font-weight:600;
  ">⬇ Page 2 PNG</button>
  <button onclick="downloadPage(3)" style="
    background:{primary_color}; color:{primary_on}; border:none; border-radius:6px;
    padding:6px 14px; cursor:pointer; font-size:13px; font-weight:600;
  ">⬇ Page 3 PNG</button>
  <button onclick="window.print()" style="
    background:transparent; color:{primary_color}; border:1.5px solid {primary_color};
    border-radius:6px; padding:5px 14px; cursor:pointer; font-size:13px; font-weight:600;
  ">🖨 PDF로 저장</button>
  <span style="color:#888; font-size:11px; margin-left:4px;">
    PDF: 인쇄 대화상자 → "PDF로 저장" 선택
  </span>
</div>
<div id="ctrl-spacer" style="height:48px;"></div>
"""
html_str = html_str.replace('<body>', '<body>' + control_bar, 1)

# ── html2canvas + 저장 JS 주입 (</body> 바로 앞) ──────────────────────
js_code = """
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script>
function downloadPage(pageNum) {
  var pages = document.querySelectorAll('.page');
  if (!pages[pageNum - 1]) { alert('페이지를 찾을 수 없어요.'); return; }
  var btn = event.currentTarget;
  btn.textContent = '처리 중...';
  btn.disabled = true;
  html2canvas(pages[pageNum - 1], {
    scale: 2,
    useCORS: true,
    backgroundColor: window.getComputedStyle(document.body).backgroundColor || '#ffffff'
  }).then(function(canvas) {
    var link = document.createElement('a');
    link.download = 'showcase_a_page' + pageNum + '.png';
    link.href = canvas.toDataURL('image/png');
    link.click();
    btn.textContent = '⬇ Page ' + pageNum + ' PNG';
    btn.disabled = false;
  });
}
</script>
"""
# ── 빈 @font-face 선언 제거 (CDN 폰트 덮어쓰기 방지) ─────────────────
html_str = re.sub(r"@font-face \{ font-family: '[^']+'; src: url\(''\)[^}]+\}\n?", '', html_str)
html_str = html_str.replace("'NKR'", "'Noto Sans KR'")

html_str = html_str.replace('</body>', js_code + '</body>', 1)
```

---

## Step 5 — 파일 저장 및 전달

```python
import os, glob

# 세션 경로 동적 감지
mounts = glob.glob('/sessions/*/mnt/claude_work')
base   = mounts[0]

# bds_ 파일과 같은 폴더에 저장
brand_name_safe = re.sub(r'[^a-zA-Z0-9가-힣_-]', '', brand_config.get('name', 'brand')).lower()
out_filename = f"bds_{brand_name_safe}-showcase_a.html"
out_path     = os.path.join(bds_folder_bash_path, out_filename)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_str)

# computer:// 링크: bash 경로 → macOS 경로 변환
# /sessions/.../mnt/claude_work/[폴더] → /Volumes/Youtube/claude_work/[폴더]
mac_path = out_path.replace(base, '/Volumes/Youtube/claude_work')
```

결과 멘트:
```
ShowCase A를 만들었어요! 파일을 열고 PNG 또는 PDF로 저장하세요.
[bds_[브랜드명]-showcase_a.html 열기](computer://[mac_path])

- PNG: "Page 1 PNG" / "Page 2 PNG" 버튼 클릭
- PDF: "PDF로 저장" 버튼 → 인쇄 대화상자 → "PDF로 저장" 선택
```

---

## 웹폰트 추천 목록 (참고)

| 스타일 | 폰트명 | font_name 값 |
|--------|--------|-------------|
| 고딕/모던 | Noto Sans KR | `Noto Sans KR` |
| 고딕/고급 | Pretendard | `Pretendard` |
| 고딕/깔끔 | SUIT | `SUIT` |
| 명조/세리프 | Noto Serif KR | `Noto Serif KR` |
| 명조/우아 | Gowun Batang | `Gowun Batang` |
| 손글씨 | Nanum Pen Script | `Nanum Pen Script` |
| 귀여운 | Jua | `Jua` |
| 디스플레이 | Black Han Sans | `Black Han Sans` |

---

## print CSS 처리 (PDF 저장 시)

`generate_combined_html()`이 이미 `@media print` 규칙을 포함한다.
컨트롤 바는 print 시 숨겨야 함 — html_str에 아래 CSS를 추가 주입:

```python
print_css = "<style>@media print { #ctrl, #ctrl-spacer { display:none !important; height:0 !important; margin:0 !important; padding:0 !important; } }</style>"
html_str = html_str.replace('</head>', print_css + '</head>', 1)
```

---

## 에러 처리

| 상황 | 처리 |
|------|------|
| 스크립트 없음 | "스킬이 올바르게 설치됐는지 확인해주세요." 안내 후 중단 |
| bds_ 없음 | modules/common.md의 3지선다 안내 |
| 저장 실패 (권한 등) | "파일 저장에 실패했어요. 폴더 경로를 확인해주세요." + 경로 출력 |
| 웹폰트 로드 안 됨 | HTML 파일은 정상 생성됨. 온라인 연결 상태에서 열도록 안내 |
