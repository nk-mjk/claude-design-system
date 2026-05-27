# modules/apply.md — 적용 플로우

> 진입점 ②에서 로드. 토큰 파일을 읽어 실제 결과물에 디자인을 입힌다.

---

## 전제 확인

같은 대화에서 방금 생성/수정한 경우:
→ 토큰 데이터 이미 메모리에 있음 → 파일 탐색 없이 바로 모드 선택으로 진행.

그렇지 않은 경우:
→ modules/common.md의 bds_ 탐색 로직 실행.

---

## 모드 선택 (다크/라이트)

- 라이트 / 다크 명시된 경우 → 해당 토큰 사용
- 명시 없음 → AskUserQuestion으로 선택: 라이트 / 다크
- bds_ 파일이 싱글 모드(하나만)인 경우 → 질문 없이 해당 모드 사용

---

## 포맷 감지 → reference 로드

사용자 요청에서 결과물 포맷을 감지하고 해당 reference 파일을 로드한다.

| 요청 키워드 | 로드할 파일 |
|------------|------------|
| PPT, 발표, 슬라이드 | `references/pptx-mapping.md` |
| 문서, Word, 보고서 | `references/docx-mapping.md` |
| 위젯, HTML, 카드뉴스, SNS, 인스타그램, 소셜 | `references/html-mapping.md` |
| PDF | `references/pdf-mapping.md` |
| 엑셀, 스프레드시트 | `references/xlsx-mapping.md` |
| SVG, 이미지 | `references/svg-mapping.md` |

포맷 불명확 시: AskUserQuestion 1차 — 문서(PPT/Word/엑셀/PDF) / SNS·카드뉴스 / SVG·이미지
- "문서" 선택 시 → AskUserQuestion 2차 — PPT / Word / 엑셀 / PDF

---

## 적용 실행

로드한 reference 파일의 매핑 테이블에 따라 토큰 값을 결과물에 적용한다.

**적용 원칙:**
- HEX 직접 주입 (CSS 변수 대신 inline 값 사용)
- 폰트가 적용 포맷(PPT, DOCX)에서 깨질 수 있음 → 적용 전 안내 + 다운로드 링크 제공 (references/[포맷]-mapping.md 참조)

**적용 후 확인:**
- "라이트 모드로 적용했어요. 수정할 곳 있으면 말씀해주세요."
- 수정 요청 시 → modules/update.md 로드
