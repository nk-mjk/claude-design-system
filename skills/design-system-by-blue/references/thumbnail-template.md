# references/thumbnail-template.md — PNG 썸네일 HTML 템플릿

> thumbnail.md Step 3에서 참조. 플레이스홀더를 bds_ 토큰값으로 치환 후 HTML 파일로 저장한다.
> **v6 업데이트 (2026-05-18)**: [PERSONALITY] BRAND 레이블 구조 변경 + [COMPONENT_HINTS] 3열 Card/Badge/Input 레이아웃으로 전면 교체

---

## HTML 템플릿

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<style>
/* [FONT_FAMILY] = heading_family (Display~Heading 4) */
/* [BODY_FONT_FAMILY] = body_family (Body, Caption 및 일반 UI) */
/* heading == body이면 두 플레이스홀더에 동일 값 사용 */
/* 웹폰트는 thumbnail.md Step 3에서 head 종료 직전에 동적 주입 — 로컬 파일 선언 없음 */
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background: #DCDCDC;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 40px;
  font-family: '[BODY_FONT_FAMILY]', 'Noto Sans KR', sans-serif;
  gap: 20px;
}
.dl-btn {
  padding: 12px 36px;
  background: [PRIMARY];
  color: #fff;
  border: none;
  border-radius: 8px;
  font-family: '[BODY_FONT_FAMILY]', 'Noto Sans KR', sans-serif;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  letter-spacing: 0.02em;
}
</style>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>

<div id="card" style="background:#FFFFFF; border-radius:16px; overflow:hidden; width:680px; height:680px; display:flex; flex-direction:column;">

  <!-- 상단 히어로 (Primary 컬러 배경) -->
  <div style="background:[PRIMARY]; height:150px; padding:20px 30px 0; flex-shrink:0; overflow:hidden; display:flex; flex-direction:column; justify-content:flex-start;">
    <div style="font-size:40px; font-weight:700; color:#fff; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif; line-height:1.1; letter-spacing:-0.5px;">[BRAND_NAME]</div>
    <div style="font-size:12px; color:rgba(255,255,255,0.6); margin-top:4px; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif;">[PRIMARY]</div>
    <div style="display:flex; gap:8px; margin-top:12px; align-items:center; flex-wrap:wrap;">
      <span style="font-size:13px; padding:2px 14px 6px; border-radius:100px; border:1.5px solid rgba(255,255,255,0.65); color:#fff; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif; white-space:nowrap;">[FONT_NAME]</span>
      <span style="font-size:13px; padding:2px 14px 6px; border-radius:100px; background:rgba(255,255,255,0.18); color:#fff; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif;">[MODE_LABEL]</span>
      [SREF_BADGE]
    </div>
  </div>

  <!-- 메인 콘텐츠 영역 -->
  <div style="padding:18px 30px 0; display:flex; flex-direction:column; flex:1; overflow:hidden;">

    <!-- Primary 틴트 스트립 -->
    <div>
      <div style="display:flex; border-radius:5px; overflow:hidden; height:34px;">
        <div style="flex:1; background:[PRIMARY_50];"></div>
        <div style="flex:1; background:[PRIMARY_100];"></div>
        <div style="flex:1; background:[PRIMARY_200];"></div>
        <div style="flex:1; background:[PRIMARY_300];"></div>
        <div style="flex:1; background:[PRIMARY_400];"></div>
        <div style="flex:1; background:[PRIMARY_500]; box-shadow:inset 0 0 0 2.5px #fff;"></div>
        <div style="flex:1; background:[PRIMARY_600];"></div>
        <div style="flex:1; background:[PRIMARY_700];"></div>
        <div style="flex:1; background:[PRIMARY_800];"></div>
        <div style="flex:1; background:[PRIMARY_900];"></div>
      </div>
      <div style="display:flex; margin-top:4px;">
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.45;">50</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.45;">100</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.45;">200</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.45;">300</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.45;">400</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; font-weight:700;">500</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.45;">600</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.45;">700</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.45;">800</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.45;">900</div>
      </div>
    </div>

    <!-- Neutral 팔레트 스트립 -->
    <div style="margin-top:8px;">
      <div style="display:flex; border-radius:5px; overflow:hidden; height:20px;">
        <div style="flex:1; background:[NEUTRAL_100]; border:1px solid [BORDER_LIGHT];"></div>
        <div style="flex:1; background:[NEUTRAL_200];"></div>
        <div style="flex:1; background:[NEUTRAL_300];"></div>
        <div style="flex:1; background:[NEUTRAL_500];"></div>
        <div style="flex:1; background:[NEUTRAL_700];"></div>
        <div style="flex:1; background:[NEUTRAL_900];"></div>
      </div>
      <div style="display:flex; margin-top:4px;">
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.4;">100</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.4;">200</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.4;">300</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.4;">500</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.4;">700</div>
        <div style="flex:1; text-align:center; font-size:9px; color:[TEXT_SUB]; opacity:.4;">900</div>
      </div>
    </div>

    <!-- Brand 스와치 (Primary / Secondary / Accent) -->
    <div style="display:flex; gap:12px; margin-top:12px;">
      <div style="flex:1; text-align:center;">
        <div style="height:54px; border-radius:10px; background:[PRIMARY]; margin-bottom:7px;"></div>
        <div style="font-size:12px; color:[TEXT_SUB]; font-weight:700; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif;">Primary</div>
        <div style="font-size:11px; color:[TEXT_SUB]; opacity:.6; margin-top:2px;">[PRIMARY]</div>
      </div>
      <div style="flex:1; text-align:center;">
        <div style="height:54px; border-radius:10px; background:[SECONDARY]; margin-bottom:7px;"></div>
        <div style="font-size:12px; color:[TEXT_SUB]; font-weight:700; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif;">Secondary</div>
        <div style="font-size:11px; color:[TEXT_SUB]; opacity:.6; margin-top:2px;">[SECONDARY]</div>
      </div>
      <div style="flex:1; text-align:center;">
        <div style="height:54px; border-radius:10px; background:[ACCENT]; margin-bottom:7px;"></div>
        <div style="font-size:12px; color:[TEXT_SUB]; font-weight:700; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif;">Accent</div>
        <div style="font-size:11px; color:[TEXT_SUB]; opacity:.6; margin-top:2px;">[ACCENT]</div>
      </div>
    </div>

    <!-- 타이포그래피 샘플 -->
    <div style="margin-top:12px; padding:13px 16px; background:[NEUTRAL_100]; border-radius:12px;">
      <div style="font-size:20px; font-weight:700; color:[TEXT_MAIN]; line-height:1.2; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif;">제목 Heading 1</div>
      <div style="font-size:12px; color:[TEXT_SUB]; margin-top:5px; line-height:1.6; font-family:'[BODY_FONT_FAMILY]','Noto Sans KR',sans-serif;">본문 텍스트 — 읽기 좋은 간격으로 콘텐츠를 담아냅니다.</div>
      <div style="font-size:11px; color:[TEXT_CAPTION]; margin-top:6px; line-height:1.5; font-family:'[BODY_FONT_FAMILY]','Noto Sans KR',sans-serif;">캡션 · 보조 설명이나 출처 표기에 사용합니다.</div>
    </div>

    <!-- 브랜드 퍼스낼리티 3단어 -->
    [PERSONALITY]

    <!-- 컴포넌트 힌트 — Card / Badge / Input -->
    [COMPONENT_HINTS]

    <!-- 하단 버튼 -->
    <div style="margin-top:auto; padding-bottom:24px;">
      <div style="display:flex; gap:12px;">
        <button style="flex:1; padding:12px 8px; border-radius:100px; background:[PRIMARY]; color:#fff; border:none; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif; font-size:16px; font-weight:700; cursor:default;">적용하기</button>
        <button style="flex:1; padding:12px 8px; border-radius:100px; background:transparent; color:[PRIMARY]; border:2px solid [PRIMARY]; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif; font-size:16px; font-weight:700; cursor:default;">미리보기</button>
      </div>
    </div>

  </div>
</div>

<button class="dl-btn" onclick="downloadPng()">⬇ PNG 다운로드</button>

<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script>
async function downloadPng() {
  const card = document.getElementById('card');
  const canvas = await html2canvas(card, { scale: 2, useCORS: true, backgroundColor: null });
  const pad = 40;
  const out = document.createElement('canvas');
  out.width  = canvas.width  + pad * 2;
  out.height = canvas.height + pad * 2;
  const ctx = out.getContext('2d');
  ctx.fillStyle = '#DCDCDC';
  ctx.fillRect(0, 0, out.width, out.height);
  ctx.drawImage(canvas, pad, pad);
  const a = document.createElement('a');
  a.download = 'thumbnail_[BRAND_NAME_SAFE].png';
  a.href = out.toDataURL('image/png');
  a.click();
}
</script>
</body>
</html>
```

---

## 토큰 치환 규칙

| 플레이스홀더 | bds_ 파일 항목 |
|------------|--------------|
| `[PRIMARY]` | Brand.Primary HEX |
| `[SECONDARY]` | Brand.Secondary HEX |
| `[ACCENT]` | Brand.Accent HEX |
| `[PRIMARY_50]`~`[PRIMARY_900]` | Primary 틴트 스케일 각 단계 HEX |
| `[NEUTRAL_100]` | Neutral-100 HEX |
| `[NEUTRAL_200]` | Neutral-200 HEX |
| `[NEUTRAL_300]` | Neutral-300 HEX |
| `[NEUTRAL_500]` | Neutral-500 HEX |
| `[NEUTRAL_700]` | Neutral-700 HEX |
| `[NEUTRAL_900]` | Neutral-900 HEX |
| `[FONT_FAMILY]` | `heading_family` (css_family 정규화 값) — 제목·히어로·버튼 |
| `[BODY_FONT_FAMILY]` | `body_family` (css_family 정규화 값) — 본문·캡션·카드 body. same_font이면 `[FONT_FAMILY]`와 동일 값 |
| `[FONT_NAME]` | 표시용 폰트명 (heading ≠ body면 `"Heading / Body"`) |
| `[BRAND_NAME]` | bds_ 파일 헤더의 스타일 이름 |
| `[BRAND_NAME_SAFE]` | 스타일 이름에서 공백·특수문자 제거한 파일명용 문자열 |
| `[MODE_LABEL]` | 듀얼 → "Dual" / 라이트만 → "Light" / 다크만 → "Dark" |
| `[TEXT_MAIN]` | Text.Main HEX (라이트 모드 기준) |
| `[TEXT_SUB]` | Text.Sub HEX (라이트 모드 기준) |
| `[TEXT_CAPTION]` | Text.Caption HEX (라이트 모드 기준) |
| `[BORDER_LIGHT]` | Border.Light HEX (라이트 모드 기준) |
| `[SREF_BADGE]` | sref 값 있으면 → `<span style="font-size:13px; padding:4px 14px; border-radius:100px; background:[NEUTRAL_100]; color:[TEXT_SUB];">sref XXXXXXXX</span>`, 없으면 빈 문자열 |
| `[PERSONALITY]` | personality 키 있으면 → 아래 PERSONALITY 렌더링 형식 참조, 없으면 빈 문자열 |
| `[COMPONENT_HINTS]` | component_hints 키 있으면 → 아래 COMPONENT_HINTS 렌더링 형식 참조, 없으면 빈 문자열 |

> **카드 구조 (V3)**: Primary 컬러 히어로 상단 → Primary 틴트 스트립(50~900) → Neutral 스트립(100~900) → Brand 스와치 3개(Primary/Secondary/Accent) → 타이포그래피 샘플 → **[PERSONALITY]** → **[COMPONENT_HINTS]** → 버튼 2개. 전체 680×680px.

---

### [PERSONALITY] 렌더링 형식 (v6)

```html
<!-- personality 있을 때 치환 -->
<div style="text-align:center; margin-top:10px; margin-bottom:10px;">
  <div style="font-size:9px; color:[TEXT_CAPTION]; letter-spacing:.08em; margin-bottom:4px; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif;">BRAND</div>
  <div style="font-size:13px; color:[TEXT_MAIN]; letter-spacing:.04em; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif;">[PERSONALITY_WORD1] <span style="color:[PRIMARY];">·</span> [PERSONALITY_WORD2] <span style="color:[PRIMARY];">·</span> [PERSONALITY_WORD3]</div>
</div>
```

| 플레이스홀더 | 소스 |
|------------|------|
| `[PERSONALITY_WORD1]` | personality 첫 번째 형용사 |
| `[PERSONALITY_WORD2]` | personality 두 번째 형용사 |
| `[PERSONALITY_WORD3]` | personality 세 번째 형용사 |

---

### [COMPONENT_HINTS] 렌더링 형식 (v6)

Card / Badge / Input 3열 레이아웃. Input은 하단 정렬(align-items:flex-end).

```html
<!-- component_hints 있을 때 치환 -->
<div style="display:flex; gap:10px; align-items:flex-end; margin-bottom:10px;">

  <!-- Card -->
  <div style="flex:1; display:flex; flex-direction:column; align-items:center; gap:4px;">
    <div style="width:100%; height:44px; background:[CARD_BG]; border:1px solid [CARD_BORDER]; border-radius:[CARD_RADIUS]; padding:5px 10px; box-shadow:0 1px 6px rgba(0,0,0,0.06); overflow:hidden;">
      <div style="font-size:9px; font-weight:700; color:[TEXT_MAIN]; line-height:1.3; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif; margin-bottom:2px;">[BRAND_NAME] 카드 제목</div>
      <div style="font-size:7.5px; color:[TEXT_SUB]; line-height:1.4; font-family:'[BODY_FONT_FAMILY]','Noto Sans KR',sans-serif;">본문 텍스트 한 줄입니다.</div>
      <div style="font-size:6.5px; color:[TEXT_CAPTION]; line-height:1.4; font-family:'[BODY_FONT_FAMILY]','Noto Sans KR',sans-serif;">캡션 · 보조 설명</div>
    </div>
    <div style="font-size:9px; color:[TEXT_CAPTION]; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif;">Card</div>
  </div>

  <!-- Badge -->
  <div style="flex:1; display:flex; flex-direction:column; align-items:center; gap:4px;">
    <div style="height:44px; display:flex; flex-direction:column; justify-content:space-between; align-items:center; width:100%; padding:3px 0;">
      <div style="background:[BADGE_BG]; color:[BADGE_TEXT]; font-size:9px; font-weight:700; padding:5px 16px; border-radius:100px; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif; white-space:nowrap;">Label</div>
      <div style="background:[PRIMARY]; color:#fff; font-size:9px; font-weight:700; padding:5px 16px; border-radius:100px; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif; white-space:nowrap;">Active</div>
    </div>
    <div style="font-size:9px; color:[TEXT_CAPTION]; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif;">Badge</div>
  </div>

  <!-- Input (하단 정렬) -->
  <div style="flex:1; display:flex; flex-direction:column; align-items:center; gap:4px;">
    <div style="width:100%; height:28px; border:1.5px solid [PRIMARY]; border-radius:[INPUT_RADIUS]; padding:0 10px; background:#FFFFFF; display:flex; align-items:center; box-shadow:0 0 0 3px [INPUT_FOCUS_RING];">
      <span style="font-size:9px; color:[TEXT_CAPTION]; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif;">텍스트를 입력하세요</span>
    </div>
    <div style="font-size:9px; color:[TEXT_CAPTION]; font-family:'[FONT_FAMILY]','Noto Sans KR',sans-serif;">Input</div>
  </div>

</div>
```

치환 대상 플레이스홀더:

| 플레이스홀더 | 소스 |
|------------|------|
| `[CARD_BG]` | `component_hints.card.bg` (보통 Surface.Card = #FFFFFF) |
| `[CARD_BORDER]` | `component_hints.card.border` (보통 Border.Default) |
| `[CARD_RADIUS]` | `component_hints.card.radius` (Named Radius box 값) |
| `[BADGE_BG]` | `component_hints.badge.bg` (보통 Primary-50) |
| `[BADGE_TEXT]` | `component_hints.badge.text` (보통 Primary-700) |
| `[INPUT_RADIUS]` | `component_hints.input.radius` (Named Radius table 값) |
| `[INPUT_FOCUS_RING]` | Primary 컬러 18% 투명도 (예: `rgba(122,155,128,0.18)`) — thumbnail.md에서 계산 |

> **PNG 다운로드**: card scale:2 캡처 후 40px 패딩 추가 → 1440×1440px 정사각형 PNG.
