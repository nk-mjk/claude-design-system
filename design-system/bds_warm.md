# bds_warm — 따뜻한 테라코타 디자인 스타일

> 생성일: 2026-05-18
> 버전: V3
> 분위기: 따뜻한 / 폰트: Pretendard / 테마: Light + Dark

---

## Colors

### Primary Tints (50 → 900)
| Token | Hex |
|-------|-----|
| primary-50 | #FBF1EE |
| primary-100 | #F5DECE |
| primary-200 | #EDBD9E |
| primary-300 | #E39A75 |
| primary-400 | #D88060 |
| primary-500 | #C96A4E |
| primary-600 | #A85038 |
| primary-700 | #82382A |
| primary-800 | #5E2319 |
| primary-900 | #4F2B1D |

### Brand Colors — Light Mode
| Role | Name | Hex |
|------|------|-----|
| Primary | 테라코타 | #C96A4E |
| Secondary | 로즈우드 | #A17D6A |
| Accent | 웜 골드 | #D4A853 |
| Destructive | 코랄 레드 | #E8524A |

### Brand Colors — Dark Mode
| Role | Name | Hex |
|------|------|-----|
| Primary | 밝은 테라코타 | #E39A75 |
| Secondary | 밝은 로즈우드 | #C4A898 |
| Accent | 밝은 웜 골드 | #E8C07A |
| Destructive | 밝은 코랄 레드 | #F07B74 |

### Neutrals (Warm)
| Token | Light | Dark |
|-------|-------|------|
| neutral-50 | #F9F5F3 | #2C1F1A |
| neutral-100 | #EDE4DF | #3D2820 |
| neutral-200 | #D6C7BF | #5A3D33 |
| neutral-400 | #B8A49A | #7A5A4E |
| neutral-500 | #9A7F74 | #9A7F74 |
| neutral-600 | #7A5A4E | #B8A49A |
| neutral-800 | #3D2820 | #D6C7BF |
| neutral-900 | #2C1F1A | #F9F5F3 |

### Surface
| Role | Light | Dark |
|------|-------|------|
| Page | #FDFAF8 | #1C1410 |
| Card | #FFFFFF | #2A1F1A |

### Text
| Role | Light | Dark |
|------|-------|------|
| Main | #2C1F1A | #F9F5F3 |
| Sub | #7A5A4E | #C4A898 |

---

## Typography

| 항목 | 값 |
|------|-----|
| Font Family | Pretendard |
| Scale | 12 / 14 / 16 / 20 / 24 / 32 / 40px |
| Weight | Regular 400 / Medium 500 / Bold 700 |
| Line Height | Body 1.7 / Heading 1.3 |
| Letter Spacing | Default 0 / Caption -0.01em |

---

## Named Radius

| Name | Value | 용도 |
|------|-------|------|
| badge | 100px | 태그, 뱃지, 라벨 |
| box | 10px | 카드, 패널 |
| callout | 14px | 콜아웃, 알림 박스 |
| table | 6px | 테이블, 인풋 |

---

## Spacing

| 항목 | 값 |
|------|-----|
| Base Unit | 8px |
| Scale | 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64px |
| Density | Comfortable (기본) |

---

## Shadow

| Name | Value |
|------|-------|
| Shadow sm | 0 1px 3px rgba(44,31,26,0.10), 0 1px 2px rgba(44,31,26,0.06) |

---

## Brand Personality

브랜드를 설명하는 핵심 단어 3개:

| 단어 | 설명 |
|------|------|
| 친근한 | 어렵지 않고 쉽게 다가갈 수 있는 분위기 |
| 포용적인 | 다양한 사람을 편안하게 받아들이는 느낌 |
| 따뜻한 | 온기 있는 컬러와 부드러운 형태로 전달되는 감성 |

---

## Token Hierarchy

Primitive → Semantic → Alias (사용 목적명) 순으로 연결:

| Primitive (HEX) | Semantic | Alias | 사용 설명 |
|-----------------|----------|-------|-----------|
| #C96A4E | primary-500 | interactive | 클릭 가능한 모든 요소 |
| #C96A4E | primary-500 | focus-ring | 포커스 표시 |
| #E8524A | destructive | destructive | 되돌릴 수 없는 액션 |
| #9A7F74 | neutral-500 | placeholder | 비활성 텍스트 |
| #F9F5F3 | neutral-50 | disabled-bg | 비활성 배경 |

---

## Component Hints

컴포넌트별 권장 토큰 조합:

### Card
| 속성 | 값 |
|------|-----|
| Background | #FFFFFF (Light) / #2A1F1A (Dark) |
| Border | #EDE4DF |
| Border Radius | 10px (box) |
| Shadow | Shadow sm |

### Badge
| 속성 | 값 |
|------|-----|
| Background | #FBF1EE |
| Text Color | #A85038 |
| Border Radius | 100px (badge) |

### Input
| 속성 | 값 |
|------|-----|
| Border | #EDE4DF |
| Border Radius | 6px (table) |
| Focus Ring | #C96A4E |
