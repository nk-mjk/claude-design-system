# references/docx-mapping.md — Word 문서 토큰 적용

---

## 폰트 가용성 주의사항

Word 문서에서는 사용자 컴퓨터에 폰트가 설치돼 있어야 정상 표시됩니다.
적용 전 아래 안내를 사용자에게 제공할 것:

> "이 폰트가 컴퓨터에 설치돼 있지 않으면 다른 폰트로 보일 수 있어요. 아래 링크에서 미리 설치해두세요."
> - Noto Sans KR: https://fonts.google.com/noto/specimen/Noto+Sans+KR
> - Pretendard: https://github.com/orioncactus/pretendard/releases
> - 나눔고딕: https://fonts.google.com/specimen/Nanum+Gothic

---

## 토큰 → Word 문서 매핑 테이블

| 문서 요소 | 적용 토큰 |
|----------|----------|
| 페이지 배경 | Surface.Background.Page (기본 흰색 또는 라이트 배경) |
| 표지·히어로 제목 | Text.Main + Primary + Heading Font + **Display** 사이즈 |
| 제목 (H1) | Text.Main + Primary + Heading Font + H1 사이즈 |
| 제목 (H2) | Text.Main + Secondary + Heading Font + H2 사이즈 |
| 제목 (H3) | Text.Sub + Heading Font + H3 사이즈 |
| 본문 | Text.Main + Body Font + Body 사이즈 |
| 캡션 | Text.Muted + Body Font + Caption 사이즈 |
| 강조 텍스트 | Accent (볼드 또는 색상 강조) |
| 배지·레이블 (도형) | Radius.badge (항상 pill) — ⚠️ 표 셀 미적용, 도형 요소에만 적용 |
| 구분선 | Border.Light |
| 표 헤더 배경 | Primary |
| 표 헤더 텍스트 | 흰색 또는 Surface.Background.Page |
| 표 본문 배경 | Surface.Card (짝수 행) / Surface.Background.Page (홀수 행) |
| 표 테두리 | Border.Default |
| 표 모서리 (Radius.table) | ⚠️ Word 표 셀은 라운드 미지원 — 적용 안 함 |
| 텍스트 박스 (도형) | Radius.box — 도형 요소에 적용 |
| 콜아웃 박스 배경 | Surface.Card + Radius.callout (도형 요소에 적용) |
| 콜아웃 박스 테두리 | Alias.interactive 또는 Border.Default |

---

## 적용 패턴

**제목 페이지:**
- 문서 제목: Primary 색 + Heading Font + H1 사이즈
- 부제목: Text.Sub + H3 사이즈
- 날짜·작성자: Text.Muted + Caption 사이즈

**본문 구성:**
- 섹션 구분: H2 (Secondary 색) + 하단 Border.Light 구분선
- 핵심 내용 박스: Surface.Card 배경 + 좌측 Accent 세로선
- 일반 본문: Text.Main + Line Height normal
