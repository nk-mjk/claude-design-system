# references/svg-mapping.md — SVG 토큰 적용

---

## 폰트 가용성 주의사항

SVG에서 한글 폰트 처리 방식:
- **브라우저에서 열 경우**: Google Fonts CDN 링크 사용 가능
- **이미지로 변환(PNG 등) 시**: 사용자 컴퓨터 설치 폰트 필요. 미설치 시 □□□(tofu)로 깨질 수 있음.
  → korean-svg 스킬 참조 (폰트 임베딩 처리)

> "SVG를 이미지로 저장할 때 한글이 깨질 수 있어요. 폰트를 미리 설치해두세요."
> - Noto Sans KR: https://fonts.google.com/noto/specimen/Noto+Sans+KR
> - Pretendard: https://github.com/orioncactus/pretendard/releases
> - 나눔고딕: https://fonts.google.com/specimen/Nanum+Gothic

---

## 토큰 → SVG 속성 매핑

| SVG 속성 | 적용 토큰 |
|----------|----------|
| `background` / `rect fill` (배경) | Surface.Background.Page |
| `fill` (메인 요소) | Primary |
| `fill` (서브 요소) | Secondary |
| `fill` (포인트 요소) | Accent |
| `fill` (텍스트 — 메인) | Text.Main |
| `fill` (텍스트 — 보조) | Text.Sub |
| `fill` (텍스트 — 캡션) | Text.Muted |
| `stroke` (테두리) | Border.Default |
| `rx` (모서리 둥글기) | Border Radius 값 |
| `font-family` (제목) | Heading Font |
| `font-family` (본문) | Body Font |
| `font-size` (Display~Caption) | 각 사이즈 스케일 px 값 (Display → 히어로 텍스트·배너 타이틀) |

---

## 적용 패턴

**카드/배지형 SVG:**
```svg
<rect fill="[Surface.Card]" rx="[Border Radius]" stroke="[Border.Default]"/>
<text font-family="[Heading Font]" fill="[Text.Main]" font-size="[H3]"/>
<text font-family="[Body Font]" fill="[Text.Sub]" font-size="[Body]"/>
```

**배너/헤더형 SVG:**
```svg
<rect fill="[Primary]"/>
<text font-family="[Heading Font]" fill="white" font-size="[Display]" font-weight="800"/>
<line stroke="[Accent]"/>
```

**아이콘/일러스트 SVG:**
- 메인 색상: Primary
- 포인트 색상: Accent
- 배경/여백: Surface.Background.Page 또는 투명
