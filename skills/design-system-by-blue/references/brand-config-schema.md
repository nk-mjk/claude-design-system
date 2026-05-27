# references/brand-config-schema.md — brand_config 키 매핑 명세

> showcase_a.md Step 3에서 bds_ 파일 → brand_config Python dict 변환 시 참조.

---

## 필수 키 매핑표

| brand_config 키 | bds_ 파일 출처 | 비고 |
|----------------|--------------|------|
| `name` | `# [이름] 디자인 토큰` 헤더의 이름 | 브랜드명 |
| `tagline` | 주요 색상 분위기 + 모드 + Named Radius 스타일을 조합해 생성 | 예: "미니멀 다크 · Light+Dark · Sharp" |
| `source` | bds_ 파일명 (예: `bds_mybrand.md`) | |
| `mode` | Surface 섹션의 모드 수 | Light만 → `'Light'`, 둘 다 → `'Light + Dark'`, Dark만 → `'Dark'` |
| `primary` | `Primary` HEX | |
| `secondary` | `Secondary` HEX | |
| `accent` | `Accent` HEX | |
| `primary_desc` | `Primary` 설명 텍스트 | |
| `secondary_desc` | `Secondary` 설명 텍스트 | |
| `accent_desc` | `Accent` 설명 텍스트 | |
| `page_bg` | `Surface.Page` (Light) HEX, 없으면 `#FFFFFF` | |
| `text_main` | `Text.Main` (Light) HEX, 없으면 `#111111` | |
| `text_sub` | `Text.Sub` (Light) HEX, 없으면 `#888888` | |
| `border` | `Border.Default` (Light) HEX, 없으면 `#E5E5E5` | |
| `heading_font` | Typography 섹션 "Heading Font:" 값 | Display~Heading 4에 적용 |
| `body_font` | Typography 섹션 "Body Font:" 값 | Body·Caption에 적용 |
| `font_name` | 자동 계산된 표시용 폰트명 | heading≠body → `"Heading / Body"`, 같으면 `"Heading"` |
| `font_badge_bg` | `primary-50` 틴트 HEX (Primary 가장 연한 단계) | |
| `font_files` | heading_font가 Pretendard 계열이 아닐 때만 지정 | 아래 참조 |
| `body_font_files` | body_font ≠ heading_font 이고 로컬 파일 필요 시 지정 | 아래 참조; CDN 사용 시 생략 |
| `primary_tints` | `primary-50` ~ `primary-900` HEX 10개 리스트 | |
| `neutral_tints` | `neutral-100` ~ `neutral-900` HEX 6개 리스트 | |
| `type_scale` | Typography 스케일 각 행 | 아래 형식 |
| `radii` | Named Radius 4개 | 아래 형식 |
| `buttons` | 버튼 토큰 (있으면 사용, 없으면 아래 기본값) | |
| `spacing_base` | Spacing 기본 단위 텍스트 | 예: `'8px (comfortable)'` |
| `shadow_level` | Shadow 레벨 텍스트 | 예: `'Shadow md'` |
| `dual_mode` | True if Light+Dark 둘 다 있음, False if 한 가지만 | |
| `surfaces` | Surface 토큰 | 아래 형식 |
| `text_tokens` | Text 토큰 4개 리스트 | 아래 형식 |
| `personality` | 브랜드 퍼스낼리티 3단어 리스트 | 아래 형식 |
| `token_hierarchy` | Primitive→Semantic→Alias 계층 매핑 리스트 | 아래 형식 |
| `component_hints` | Card/Badge/Input 컴포넌트 스타일 힌트 dict | 아래 형식 |

---

## 서브 형식 명세

### type_scale
```python
# (레이블, px값, font-weight, line-height, 샘플텍스트, 렌더pt)
'type_scale': [
    ('Display',   56, 800, '1.2', 'Display',   20),
    ('Heading 1', 38, 700, '1.3', 'Heading 1', 15),
    ('Heading 2', 28, 700, '1.3', 'Heading 2', 12),
    ('Heading 3', 22, 600, '1.35','Heading 3', 10.5),
    ('Heading 4', 18, 600, '1.4', 'Heading 4', 9),
    ('Body',      16, 400, '1.6', '샘플 본문 텍스트', 7.5),
    ('Caption',   13, 400, '1.5', '캡션 텍스트', 6.5),
]
# 최대 7행. bds_ 파일에 없는 단계는 생략해도 됨.
# 샘플텍스트: bds_ 파일의 한국어 샘플이 있으면 그대로, 없으면 레이블 이름 사용.
```

### radii
```python
# (이름, CSS값) — Named Radius 4개
'radii': [
    ('badge',   '100px'),  # badge는 항상 100px
    ('box',     '6px'),    # bds_ 파일의 box 값
    ('callout', '10px'),   # bds_ 파일의 callout 값
    ('table',   '4px'),    # bds_ 파일의 table 값
],
```

### surfaces
```python
# dual_mode=True (Light+Dark)
'surfaces': {
    'light': {'page': '#FAFAFA', 'card': '#FFFFFF'},
    'dark':  {'page': '#13141F', 'card': '#1E2030'},
},

# dual_mode=False (단일 모드)
'surfaces': {
    'stack': [
        ('Surface.Page',  '#000000'),
        ('Surface.AppBg', '#121212'),
        ('Surface.Card',  '#282828'),
    ]
},
```

### text_tokens
```python
# (토큰명, HEX, 샘플텍스트) — 4개
'text_tokens': [
    ('Text.Main',     '#111111', '기본 본문 텍스트'),
    ('Text.Sub',      '#6D6D6D', '보조 텍스트'),
    ('Text.Caption',  '#999999', '캡션 · 주석'),
    ('Text.Disabled', '#B3B3B3', '비활성 상태'),
],
```

### personality
```python
# 브랜드 퍼스낼리티 3단어 + 한 줄 설명
# create.md Step 3에서 분위기·색상·폰트 조합 기반으로 자동 추론
'personality': [
    ('명확한',     '복잡함 없이 핵심을 전달하는 스타일'),
    ('신뢰있는',   '일관된 시각 언어로 신뢰를 쌓는 브랜드'),
    ('절제된',     '과하지 않고 딱 필요한 만큼만 강조'),
]
# 각 항목: (형용사, 한 줄 설명)
```

### token_hierarchy
```python
# Primitive → Semantic → Alias 계층 매핑. 주요 5~6개만 포함.
# create.md Step 3 Semantic Alias 생성 결과에서 자동 파생
'token_hierarchy': [
    ('#5C67F2',   'primary-500',  'interactive',  '클릭 가능한 모든 요소'),
    ('#5C67F2',   'primary-500',  'focus-ring',   '포커스 표시'),
    ('#F25C5C',   'accent',       'destructive',  '되돌릴 수 없는 액션'),
    ('#888888',   'neutral-500',  'placeholder',  '비활성 텍스트'),
    ('#F0F0F0',   'neutral-100',  'disabled-bg',  '비활성 배경'),
]
# 각 항목: (primitive_hex, primitive_name, alias_name, alias_description)
```

### component_hints
```python
# Card / Badge / Input 컴포넌트 스타일 힌트 — 자동 추론
# Surface.Card + Named Radius + Shadow + Primary 틴트 조합에서 파생
'component_hints': {
    'card':  {
        'bg':       '#FFFFFF',    # Surface.Card (Light)
        'radius':   '6px',        # Named Radius box 값
        'border':   '#E5E5E5',    # Border.Default
        'shadow':   'Shadow sm',  # shadow_level 기반
    },
    'badge': {
        'bg':       '#ECEEFE',    # primary-50
        'text':     '#3039B2',    # primary-700
        'radius':   '100px',      # Named Radius badge (항상 pill)
    },
    'input': {
        'border':   '#E5E5E5',    # Border.Default
        'radius':   '6px',        # Named Radius box 값
        'focus':    '#5C67F2',    # interactive (= Primary)
    },
}
```

### font_files (heading 폰트 로컬 파일)
```python
# heading_font가 Pretendard 계열이 아닐 때만 지정.
# CDN 웹폰트 사용 시에는 family만 넣고 regular/bold를 None으로 설정.
'font_files': {
    'family':  'Jua',   # CSS font-family 이름 (= heading_font 값)
    'regular': None,    # 로컬 파일 없음 → CDN 폰트 사용
    'bold':    None,
},
# Pretendard 계열이면 font_files 키 자체를 생략
# (스크립트가 Pretendard-Regular.otf / Pretendard-Bold.otf를 기본 사용)
```

### body_font_files (body 폰트 로컬 파일)
```python
# body_font ≠ heading_font 이고 로컬 파일이 필요할 때만 지정.
# CDN 웹폰트 사용 시에는 family만 넣고 regular/bold를 None으로 설정.
# CDN 전용이면 이 키를 생략해도 됨 (showcase_a.md, thumbnail.md에서 CDN URL만 주입).
'body_font_files': {
    'family':  'Gaegu',  # CSS font-family 이름 (= body_font 값)
    'regular': None,     # 로컬 파일 없음 → CDN 폰트 사용
    'bold':    None,
},
```

### buttons 기본값 (bds_ 파일에 버튼 없을 때)
```python
'buttons': [
    ('Primary CTA',  primary,        on_color(primary), 'none'),
    ('Secondary',    'transparent',  primary,           f'0.4mm solid {primary}'),
    ('Ghost',        'transparent',  text_sub,          f'0.4mm solid {border}'),
],
```
