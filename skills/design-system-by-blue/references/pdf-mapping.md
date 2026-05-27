# references/pdf-mapping.md — PDF 토큰 적용

---

## 폰트 가용성 주의사항

PDF 생성 방식에 따라 달라짐:
- **HTML → PDF 변환** 시: Google Fonts CDN 사용 가능 → html-mapping.md 참조 후 변환
- **직접 PDF 생성** 시: 사용자 컴퓨터 폰트 필요

> "이 폰트가 설치돼 있지 않으면 다른 폰트로 보일 수 있어요."
> - Noto Sans KR: https://fonts.google.com/noto/specimen/Noto+Sans+KR
> - Pretendard: https://github.com/orioncactus/pretendard/releases
> - 나눔고딕: https://fonts.google.com/specimen/Nanum+Gothic

---

## 토큰 → PDF 요소 매핑 테이블

| PDF 요소 | 적용 토큰 |
|----------|----------|
| 페이지 배경 | Surface.Background.Page |
| 헤더 영역 배경 | Primary |
| 헤더 텍스트 | 흰색 또는 Surface.Background.Page + Heading Font |
| 표지 타이틀 (히어로) | Text.Main + Heading Font + **Display** 사이즈 |
| 제목 (H1/H2) | Text.Main + Primary + Heading Font |
| 본문 텍스트 | Text.Main + Body Font + Body 사이즈 |
| 캡션 | Text.Muted + Caption 사이즈 |
| 강조 색상 | Accent |
| 섹션 구분선 | Border.Light |
| 박스/콜아웃 배경 | Surface.Card |
| 박스 테두리 | Border.Default + Border Radius |
| 푸터 텍스트 | Text.Muted + Caption 사이즈 |

---

## 적용 패턴

**표지:**
- 배경: Primary (전면) 또는 Surface.Background.Page
- 메인 타이틀: Heading Font + **Display** 사이즈 + 흰색 (Primary 배경 위)
- 하단 포인트 선: Accent

**내지:**
- 좌측 섹션 레이블: Primary 컬러 + Heading Font
- 본문: Body Font + Text.Main + Line Height normal
- 핵심 내용 박스: Surface.Card 배경 + 좌측 Accent 세로선 (3-4px)
