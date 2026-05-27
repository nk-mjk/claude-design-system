# references/token-rules.md — 토큰 자동 매핑 규칙

> create.md Step 3에서 Named Radius·Spacing·Shadow 생성 시 참조.
> 분위기·용도 기반 자동 매핑 규칙 전체를 정의한다.

---

## Named Radius — 용도별 반경 시스템

Step 1-a 분위기에서 base 스타일 결정 (생성 과정에서만 사용, bds_ 파일에 저장 안 함):
- 미니멀 → **sharp**
- 따뜻한·발랄한 → **round**
- 그 외 → **soft**

base 스타일에서 아래 4개 값을 파생해 bds_ 파일에 저장:

| 요소 | 역할 | sharp | soft | round |
|------|------|-------|------|-------|
| `badge` | 태그·레이블 | 100px (pill) | 100px (pill) | 100px (pill) |
| `box` | 일반 도형·텍스트 박스 | 2px | 6px | 12px |
| `callout` | 강조 박스·인용 박스 | 4px | 10px | 16px |
| `table` | 표 모서리 | 2px | 4px | 8px |

> badge는 스타일 무관 항상 pill. box값이 기존 Border Radius 단일값과 동일 (하위호환).

---

## Spacing — 용도 기반 기본 단위

| 용도 | 기본 단위 |
|------|---------|
| PPT / 문서 / 인쇄물(Other 입력 포함) | 8px (comfortable) |
| SNS / 웹 | 4px (compact) |

---

## Shadow — 분위기 기반 수준

| 분위기 | Shadow 수준 |
|--------|------------|
| 미니멀 | 없음 또는 sm |
| 고급스러운 | md |
| 강렬한 / 발랄한 | lg |
| 그 외 | sm |

---

> Named Radius·Spacing·Shadow는 자동 생성. Step 4에서 한꺼번에 조정 가능.
