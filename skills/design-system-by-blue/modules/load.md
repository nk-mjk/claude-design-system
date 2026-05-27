# modules/load.md — 불러오기 플로우

> 진입 경로: A-2(참고 파일 기반 신규) / C갈래에서 파일 찾았을 때 / Type 1·2·3 파일 직접 불러올 때.
> 파일 종류(Type 1 / Type 2 / Type 3)에 따라 처리 방식이 달라진다.
> 마무리는 항상 bds_ 파일 저장. "적용할지" 묻지 않는다.

---

## 파일 입력 받기

아래 세 가지 방법 중 하나로 파일을 입력받는다:

- **방법 A**: 파일 업로드 (사용자가 직접 올림)
- **방법 B**: 경로 입력 → Claude가 Read 도구로 읽어옴
- **방법 C**: 텍스트를 채팅에 직접 붙여넣기

파일 입력 후 → 아래 타입 판별 실행.

---

## 타입 판별

- 파일 확장자가 `.zip`이면 → **Type 3** (Claude Design 패키지 여부 확인 후 처리)
- 파일명이 `bds_`로 시작하면 → **Type 1**
- 그 외 → **Type 2**

---

## Type 1 — 우리 스킬로 만든 bds_ 파일

구조가 정해진 파일 → 읽으면 바로 사용 가능, 변환 불필요.

1. 파일 읽기
2. **V3 마이그레이션 체크** — 아래 세 섹션이 없으면 V2 파일로 판단하고 자동 파생:

   | 없는 섹션 | 자동 파생 방법 |
   |----------|--------------|
   | `## Brand Personality` | Primary 색조 분석 → 분위기 방향 결정 → 형용사 3단어 + 한 줄 설명 생성 |
   | `## Token Hierarchy` | Primary 틴트·Accent·Text.Sub·Neutral 기반으로 6개 alias 매핑 자동 생성 |
   | `## Component Hints` | Named Radius + Surface 색상 + Shadow 수준 조합으로 Card/Badge/Input 스펙 생성 |

   - 하나 이상 없으면 → 파생 내용을 bds_ 파일 하단에 추가하고 저장 (기존 섹션 건드리지 않음)
   - 완료 후 한 줄 안내: "V3 형식으로 업그레이드했어요. Brand Personality · Token Hierarchy · Component Hints 섹션이 추가됐어요."
   - 세 섹션 모두 있으면 → 마이그레이션 생략, 바로 다음 단계

   > **ShowCase 생성 시에도 자동 적용**: `generate_ds_html.py`가 V3 필드가 없는 brand_config를 자동으로 채운다. bds_ 파일 업데이트 없이도 ShowCase는 항상 V3 포맷으로 출력됨.

3. show_widget으로 팔레트 mockup 표시 (컬러 스와치 + 타이포 샘플)
4. "수정하고 싶은 곳 있으면 말씀해주세요. 그대로면 완료예요."
   - 수정 원함 → modules/update.md 로드
   - 그대로 → 완료 (파일 이미 있으므로 별도 저장 불필요)

---

## Type 3 — Claude Design 패키지 (.zip)

Claude Design에서 export한 디자인 시스템 zip 파일. 유저 개입 없이 원샷 변환.

### Step 1 — 압축 해제 및 패키지 확인

bash로 zip 압축 해제 후 아래 세 파일이 모두 존재하는지 확인:
- `SKILL.md` (frontmatter `---` 포함)
- `README.md`
- `colors_and_type.css`

**확인됨** → "**[브랜드명]** 디자인 시스템 확인했어요. Cowork용으로 변환할게요!" (브랜드명은 README.md 첫 `# 제목`에서 읽어옴)

**확인 안 됨** → Claude Design 패키지가 아님 → **Type 2로 fallback** (일반 외부 문서 처리)

---

### Step 2 — 핵심 파일 파싱

**README.md에서 읽어올 것:**
- 브랜드명 (스타일 이름 기본값으로 사용)
- Primary / Accent / 기타 컬러 (HEX) — CSS 추출값 검증용
- 폰트명
- Tone & Voice (있으면 bds_ 파일 메타데이터로 저장)

**colors_and_type.css에서 읽어올 것 (CSS 변수 파싱):**

| CSS 변수 | bds_ 토큰 |
|---------|-----------|
| `--color-primary` | Brand.Primary |
| `--color-secondary` | Brand.Secondary (없으면 Step 3에서 Primary 보색 계열로 자동 파생) |
| `--color-accent` | Brand.Accent |
| `--color-success` | Semantic.Success (웹 용도로 간주) |
| `--color-text-main` | Text.Main |
| `--color-text-sub` | Text.Sub |
| `--color-bg` | Surface.Background.Page |
| `--color-surface` | Surface.Card |
| `--color-border` | Border.Default |
| `--color-primary-50` ~ `--color-primary-900` | Primary 틴트 스케일 (이미 있으면 그대로 사용) |
| `--color-accent-50` ~ `--color-accent-900` | Accent 틴트 스케일 (이미 있으면 그대로 사용) |
| `--color-interactive` | Alias.interactive |
| `--color-destructive` | Alias.destructive |
| `--color-positive` | Alias.positive |
| `--color-placeholder` | Alias.placeholder |
| `--color-disabled-bg` | Alias.disabled-bg |
| `--color-disabled-text` | Alias.disabled-text |
| `--text-display-size/weight/line` | Typography.Display |
| `--text-h1-size/weight/line` | Typography.H1 |
| `--text-h2-size/weight/line` | Typography.H2 |
| `--text-body-size/weight/line` | Typography.Body |
| `--text-caption-size/weight/line` | Typography.Caption |
| `--font-family` | Heading Font / Body Font (동일 폰트면 둘 다 동일하게) |
| `--space-1` ~ `--space-10` | Spacing scale |
| `--radius-pill` | Radius.badge (100px) |
| `--radius-card` | Radius.box |
| `--radius-sheet` | Radius.callout |
| `--radius-sm` | Radius.table |
| `--shadow-sheet` 또는 `--shadow-modal` | Shadow 수준 판별용 참고값 |

> `--radius-btn`, `--radius-input` 등 웹 전용 항목은 무시.
> CSS 변수가 없는 항목은 create.md의 분위기 기반 자동 매핑 규칙으로 채움.

---

### Step 3 — bds_ 포맷으로 원샷 변환

위 파싱 결과를 토대로 bds_ 파일 내용을 한 번에 생성한다.

**추가로 자동 생성할 항목 (CSS에 없어도):**
- 틴트 스케일이 CSS에 없는 경우 → create.md 방식으로 자동 산출
- Neutral 컬러 단계 → `--color-text-main` / `--color-text-sub` / `--color-bg` 기반으로 추정
- Secondary 컬러 → CSS에 없으면 Primary 보색 계열로 자동 파생
- H3 / H4 → H2와 Body 사이에서 비례 계산으로 자동 삽입
- Named Radius 중 누락된 항목 → 존재하는 값에서 비례 계산

**bds_ 파일 헤더 형식:**
```markdown
# [브랜드명] 디자인 토큰
> 스타일 이름: [브랜드명]
> 출처: Claude Design 패키지
> 생성일: YYYY-MM-DD | 버전: 1.0
```

---

### Step 4 — 미리보기

show_widget으로 변환 결과 표시:
- 컬러 팔레트 스와치 (Primary·Accent·Neutral)
- 타이포그래피 샘플 (Display ~ Caption)
- Named Radius · Spacing · Shadow 값
- CSS에 없어서 자동으로 채운 항목 목록 (있을 경우)

> **[중요] 테마 독립 렌더링 원칙**: 타이포그래피 샘플·텍스트가 올라가는 영역은 CSS 변수(`var(--color-background-*)`) 대신 **브랜드 HEX를 직접 지정**한다. 앱의 다크/라이트 테마와 무관하게 브랜드 실제 색상이 정확히 보여야 하기 때문. 타이포그래피 샘플 컨테이너 → `background: [Surface.Card HEX]` 고정, 텍스트 → `color: [Text.Main HEX]` 고정.

"이렇게 변환했어요. 바꾸고 싶은 곳 있으면 말씀해주세요."
- 수정 요청 있으면 반영 후 미리보기 재렌더링
- 없으면 Step 5 진행

---

### Step 5 — 저장

- 파일명 기본값: 브랜드명 기반 자동 제안 (예: `bds_blooming.md`)
- 저장 위치: "어디에 저장할까요?" 한 번만 확인. 기본 제안: 현재 대화 작업 폴더
- 저장 완료 메시지: "저장했어요! 이제 '[브랜드명] 스타일로 PPT 만들어줘' 처럼 부르면 바로 적용할 수 있어요."

---

## Type 2 — 외부 디자인 시스템 문서

형태가 자유로움 (PDF, 워드, 일반 MD, 이미지, 브랜드 가이드 등).
색상 코드·폰트명 등을 추출 → bds_ 포맷으로 변환.

**추출 항목:**
- Primary / Secondary / Accent 컬러 (HEX)
- 배경색 / 텍스트색
- 폰트명 (Heading / Body 구분)
- 있으면 추가로: Border Radius, Shadow 수준

**변환 규칙:**

| 상황 | 처리 |
|------|------|
| **부족한 경우** | 빈 토큰은 추출된 값 기반으로 자동 생성 (예: Shadow 없으면 분위기에 맞게 자동 매핑) |
| **넘치는 경우** | 우리 포맷에 없는 토큰은 무시 (예: Breakpoint, Z-index 등) — 형식 일관성 유지 |

**변환 완료 후:**
1. show_widget으로 팔레트 mockup 표시
2. 자동으로 채운 항목을 명시해서 사용자에게 확인 요청
   - 예: "Shadow는 문서에 없어서 분위기에 맞게 'sm'으로 설정했어요. 바꾸고 싶으면 말씀해주세요."
3. 확인 완료 → Step 5 저장 (modules/create.md의 Step 5 절차 그대로 적용)
