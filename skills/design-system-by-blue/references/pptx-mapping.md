# references/pptx-mapping.md — PPT 토큰 적용

---

## 폰트 가용성 주의사항

PPT에서는 사용자 컴퓨터에 폰트가 설치돼 있어야 정상 표시됩니다.
적용 전 아래 안내를 사용자에게 제공할 것:

> "이 폰트가 컴퓨터에 설치돼 있지 않으면 다른 폰트로 보일 수 있어요. 아래 링크에서 미리 설치해두세요."
> - Noto Sans KR: https://fonts.google.com/noto/specimen/Noto+Sans+KR
> - Pretendard: https://github.com/orioncactus/pretendard/releases
> - 나눔고딕: https://fonts.google.com/specimen/Nanum+Gothic

---

## 토큰 → PPT 매핑 테이블

| PPT 요소 | 적용 토큰 |
|----------|----------|
| 슬라이드 배경 | Surface.Background.Page |
| 표지 타이틀 (히어로) | Text.Main + Heading Font + **Display** 사이즈 |
| 제목 텍스트 | Text.Main + Heading Font + H1/H2 사이즈 |
| 본문 텍스트 | Text.Sub + Body Font |
| 강조 텍스트 / 포인트 | Alias.destructive (Accent) |
| 도형 채우기 (메인) | Primary |
| 도형 채우기 (서브) | Secondary |
| 도형 채우기 (틴트) | Primary-100 또는 Primary-50 (연한 강조 배경에 활용) |
| 도형 테두리 | Border.Default |
| 캡션 / 설명 텍스트 | Alias.placeholder + Caption 사이즈 |
| 구분선 | Border.Light |
| 카드형 박스 배경 | Surface.Card |
| 배지·레이블 도형 | Primary-50 배경 + Primary 텍스트 + **Radius.badge** (pill) |
| 일반 텍스트 박스 / 도형 | **Radius.box** |
| 강조 박스 / 콜아웃 | Surface.Card + **Radius.callout** |
| 표 모서리 | **Radius.table** |

> Named Radius (badge/box/callout/table) 모두 PPT 도형에 적용 가능 ✅

---

## 적용 패턴

**표지 슬라이드:**
- 배경: Surface.Background.Page
- 메인 타이틀: Text.Main + **Display** 사이즈 + Heading Font
- 서브타이틀: Text.Sub (H3 사이즈)
- 포인트 요소 (선·도형): Alias.interactive (Primary)

**콘텐츠 슬라이드:**
- 슬라이드 제목: Primary 배경 + 흰 텍스트 (또는 Text.Main + 언더라인 Accent)
- 본문: Text.Main / Text.Sub, Body Font
- 강조 박스: Surface.Card 배경 + Radius.callout
- 배지·레이블: Primary-50 배경 + Radius.badge

**Named Radius 적용:**
- PPT 도형 서식 → 모서리 둥글기에서 각 radius 값 직접 입력
- badge(pill), box(일반), callout(강조박스), table(표) 구분해서 적용
