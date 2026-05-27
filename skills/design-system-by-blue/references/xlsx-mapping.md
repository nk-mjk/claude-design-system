# references/xlsx-mapping.md — Excel 토큰 적용

> Excel은 디자인 비중이 낮은 포맷. 헤더 색상·폰트 정도를 적용한다.

---

## 폰트 가용성 주의사항

Excel에서는 사용자 컴퓨터에 폰트가 설치돼 있어야 정상 표시됩니다.

> "이 폰트가 설치돼 있지 않으면 다른 폰트로 보일 수 있어요."
> - Noto Sans KR: https://fonts.google.com/noto/specimen/Noto+Sans+KR
> - Pretendard: https://github.com/orioncactus/pretendard/releases
> - 나눔고딕: https://fonts.google.com/specimen/Nanum+Gothic

---

## 토큰 → Excel 요소 매핑 테이블

| Excel 요소 | 적용 토큰 |
|-----------|----------|
| 시트 탭 / 상단 타이틀 | Primary |
| 표 헤더 배경 | Primary |
| 표 헤더 텍스트 | 흰색 또는 Surface.Background.Page + Heading Font |
| 짝수 행 배경 | Surface.Card (연한 배경) |
| 홀수 행 배경 | Surface.Background.Page |
| 본문 텍스트 | Text.Main + Body Font |
| 합계/강조 행 배경 | Secondary (연하게) |
| 강조 셀 | Alias.destructive 배경 또는 텍스트 (Accent) |
| 테두리 | Border.Default |
| 표 모서리 (Radius.table) | ⚠️ Excel 셀은 라운드 미지원 — 적용 안 함 |
| 도형/콜아웃 박스 | Radius.box / Radius.callout — 셀이 아닌 도형 삽입 시에만 적용 |

---

## 적용 패턴

**기본 데이터 테이블:**
- 헤더: Primary 배경 + 흰 텍스트 + Heading Font (볼드)
- 데이터 행: 짝/홀 교차 (Surface.Card / Surface.Background.Page)
- 합계 행: Secondary 연한 배경 + 볼드

**대시보드/요약 시트:**
- 타이틀 셀: Primary 배경 + 흰 텍스트 + H2 사이즈
- KPI 박스: Surface.Card 배경 + Accent 강조 숫자
- 섹션 구분: Border.Light 테두리
