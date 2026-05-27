# references/html-mapping.md — show_widget / HTML 토큰 적용

---

## 폰트 가용성 주의사항

HTML / show_widget에서는 Google Fonts CDN으로 자동 로드 → 별도 설치 불필요.

```html
<!-- Noto Sans KR -->
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">

<!-- Pretendard -->
<link href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css" rel="stylesheet">

<!-- 나눔고딕 -->
<link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&display=swap" rel="stylesheet">
```

---

## 토큰 → CSS 변수 매핑

HTML 적용 시 CSS 변수로 선언 후 inline 사용:

```css
:root {
  /* Brand */
  --color-primary: [Primary HEX];
  --color-secondary: [Secondary HEX];
  --color-accent: [Accent HEX];

  /* Brand 틴트 스케일 */
  --color-primary-50: [Primary-50 HEX];
  --color-primary-100: [Primary-100 HEX];
  --color-primary-500: [Primary HEX];    /* base */
  --color-primary-900: [Primary-900 HEX];
  --color-accent-50: [Accent-50 HEX];
  --color-accent-500: [Accent HEX];      /* base */

  /* Semantic Alias */
  --color-interactive: var(--color-primary);
  --color-destructive: var(--color-accent);
  --color-positive: [Success HEX];          /* 웹 용도 선택 시에만 생성 */
  --color-placeholder: [Text.Sub HEX];
  --color-disabled-bg: [Neutral 가장 밝은 단계 HEX];
  --color-disabled-text: [Neutral 중간 단계 HEX];

  /* Surface */
  --color-bg: [Surface.Background.Page HEX];
  --color-card: [Surface.Card HEX];

  /* Text */
  --color-text-main: [Text.Main HEX];
  --color-text-sub: [Text.Sub HEX];
  --color-text-muted: [Text.Muted HEX];

  /* Border */
  --color-border: [Border.Default HEX];

  /* Typography */
  --font-heading: '[Heading Font]', sans-serif;
  --font-body: '[Body Font]', sans-serif;
  --text-display-size: [Display px];
  --text-display-weight: 800;

  /* Named Radius */
  --radius-badge: 100px;
  --radius-box: [Radius.box]px;
  --radius-callout: [Radius.callout]px;
  --radius-table: [Radius.table]px;

  /* Spacing */
  --spacing-base: [Spacing 기본단위]px;
}
```

---

## 토큰 → 요소 매핑 테이블

| HTML 요소 | 적용 토큰 |
|----------|----------|
| body 배경 | Surface.Background.Page |
| 카드/박스 배경 | Surface.Card |
| 메인 제목 | Text.Main + Heading Font + H1 사이즈 |
| 서브 제목 | Text.Main + Heading Font + H2/H3 사이즈 |
| 본문 텍스트 | Text.Main + Body Font + Body 사이즈 |
| 캡션 | Text.Muted + Caption 사이즈 |
| 버튼 (메인) | Primary 배경 + 흰 텍스트 + Radius |
| 버튼 (서브) | Secondary 배경 + 흰 텍스트 + Radius |
| 강조 요소 | Accent |
| 테두리 | Border.Default |
| 구분선 | Border.Light |

---

## 카드뉴스 / SNS 콘텐츠 패턴

```
배경: Surface.Background.Page
헤더 배색: Primary (또는 Accent)
제목: Heading Font + H2 사이즈 + 흰색 (헤더 위)
본문: Body Font + Text.Main
포인트 요소: Accent
카드 테두리: Border Radius 적용
```
