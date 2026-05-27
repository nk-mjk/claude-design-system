# modules/create.md — 신규 생성 플로우

> Step 1-a ~ Step 6 순서대로 진행.
> A-2(참고 파일 기반 신규) 진입 시: 추출된 색·폰트가 각 Step의 추천값으로 미리 채워진 상태로 시작.

---

## Step 1-a — 색상 방향 선택

AskUserQuestion으로 분위기 선택:

- question: "어떤 분위기로 만들까요? (건너뛰면 색+폰트 세트 3가지를 추천해드려요)"
- 선택지 4개: 미니멀 / 따뜻한 / 강렬한 / 고급스러운
- Other 옵션: "발랄한", "코랄 블루톤으로" 같은 자유 입력, 또는 "건너뛸게요" 입력
- 건너뛰기 입력 시 → Step 1-b 생략, 무드보드 3종 제안으로 바로 이동

색을 선택한 경우 → Step 1-b 진행.

---

## Step 1-b — 폰트 선택

(Step 1-a에서 색을 선택한 경우에만 진행. 건너뛰기 시 생략.)

AskUserQuestion으로 폰트 스타일 선택:

- question: "폰트는 어떤 스타일로 할까요?"
- 선택지 4개:
  - **고딕/모던** — 깔끔하고 현대적인 고딕 계열 (Pretendard, Noto Sans KR, SUITE 등)
  - **명조/세리프** — 고급스럽고 품격 있는 세리프 계열 (Hahmlet, Noto Serif KR, KoPub Batang 등)
  - **손글씨/감성** — 따뜻하고 인간미 있는 필기 폰트 (Gaegu, 빙그레 싸만코체, 교보손글씨 등)
  - **추천해줘** — 분위기·이미지·설명 기반 자동 매핑 (아래 규칙 적용)
- Other 옵션: 폰트명 직접 입력 가능. "을지로 느낌", "픽셀 폰트", "레트로", "궁서체" 같은 자유 설명도 OK → 아래 매핑 적용

### 추천해줘 — 자동 매핑 규칙

Step 1-a 분위기 + 사용자 추가 입력을 아래 10개 카테고리에 매핑 후 추천한다.
CDN URL이 필요하면 스킬 폴더의 `references/font-reference.md`를 Read한다.

| 카테고리 | 해당 분위기 · 키워드 | 고딕 추천 | 명조 추천 | 개성 서체 옵션 |
|---------|-------------------|---------|---------|--------------|
| 미니멀/클린 | 깔끔, 현대, 기업, IT, 스타트업 | Pretendard | KoPubWorld Batang | SUITE |
| 따뜻/내추럴 | 온기, 자연, 핸드메이드, 소규모 브랜드 | LINE Seed Sans KR | Gowun Batang | 빙그레 싸만코체 |
| 강렬/다이나믹 | 임팩트, 에너지, 스포츠, 이벤트 | Black Han Sans | — | BM 한나체 Pro |
| 고급/엘레강스 | 럭셔리, 패션, 프리미엄, 웨딩 | KoPubWorld Dotum | Hahmlet | 조선궁서체 |
| 발랄/귀여운 | 캐릭터, 키즈, 게임, 친근함 | Jua | — | 주아체 |
| 레트로/빈티지 | 복고, 뉴트로, 7080, 아날로그 | Gugi | Song Myung | BM 을지로체 |
| 테크/미래적 | 첨단, 디지털, SF, 개발자 | Pretendard | — | Orbit |
| 클래식/문학적 | 전통, 출판, 역사, 신문 | KoPubWorld Dotum | Noto Serif KR | KCC김훈체 |
| 아트/인디 | 독창적, 갤러리, 작가주의, 감성 | — | — | KCC환기체 |
| 스트리트/엣지 | 도시, 힙합, 서브컬처, 언더그라운드 | Black Han Sans | — | 기랑해랑체 |

**매핑 규칙:**
- Step 1-a 분위기가 명확하면 해당 카테고리 직접 적용
- Step 1-a가 "Other" 자유 입력이면 → 텍스트에서 키워드 추출 후 가장 가까운 카테고리 선택
- 이미지 업로드 시 → 색온도·질감·시대감에서 카테고리 판단
- 복수 카테고리 해당 시 → 고딕은 주 카테고리, 개성 옵션은 인접 카테고리에서 선택

**추천 결과 형식 (반드시 2개 제시):**
- **Heading Font (제목용)**: Display~Heading 4에 적용 — 임팩트·개성 위주로 선택
- **Body Font (본문용)**: Body·Caption·UI 텍스트에 적용 — 가독성 위주로 선택
- heading = body로 같은 폰트 사용도 가능하지만, 다를 때 더 풍부한 분위기 연출 가능
- 제안 후 사용자 확정. 확정된 두 폰트가 Step 3 타이포그래피 토큰으로 저장됨.

- 색과 폰트는 자유롭게 조합 가능 (강제 연결 없음)

→ 색·폰트 확정 후 Step 2 진행.

---

## [건너뛰기 경로] 무드보드 3종 제안

Step 1-a 건너뛰기 시 진입. 색+폰트 세트로 구성된 무드보드 3종을 show_widget으로 제시:

예시 (실제 생성 시 분위기 다양하게 구성):
- ① 미니멀 — 딥네이비 + 화이트 + Pretendard
- ② 따뜻한 — 테라코타 + 베이지 + 나눔고딕
- ③ 모던 — 차콜 + 라이트그레이 + Noto Sans KR

하나 고르면 색·폰트 동시 확정 → Step 2 진행.

---

## Step 2 — 용도 확인

AskUserQuestion으로 복수 선택 (multiSelect: true):

- question: "주로 어떤 곳에 쓸 예정인가요? (건너뛰면 PPT + 문서 + SNS 기본값으로 진행해요)"
- 선택지 4개: PPT / 문서 / SNS / 웹
- Other 옵션: "인쇄물" 직접 입력 또는 "기본값으로" 입력 → **PPT + 문서 + SNS** 자동 적용 (Semantic 컬러 미생성, 기본 토큰 세트)
  - Other에 "인쇄물" 포함 시 → 인쇄물 용도 추가 (Spacing 8px 적용)
- 용도가 **웹** 포함 시 → Semantic 컬러 토큰 추가 생성

→ Step 2-b 진행.

---

## Step 2-b — 다크/라이트 모드 선택

AskUserQuestion으로 모드 선택:

- 선택지: 밝은 버전만(라이트) / 어두운 버전만(다크) / 둘 다 만들기
- 용도가 웹 포함 시: description에 "웹은 보통 두 가지 다 쓰는데, 한 쌍으로 만들면 편해요" 추천 안내 추가
- 선택 결과가 Step 3 토큰 생성에 바로 반영

→ Step 3 진행.

---

## Step 3 — 토큰 자동 생성

선택한 색상·폰트·용도·모드를 기반으로 아래 토큰을 자동 생성한다.

### 컬러 토큰

**Brand (항상 생성)**
- Primary / Secondary / Accent

**Brand 틴트 스케일 (항상 생성)**
- Primary, Secondary, Accent 각각 50~900 단계 자동 산출 (총 10단계)
- 500 = base 색상, 50~400 = 밝아지는 방향(흰색 혼합), 600~900 = 어두워지는 방향(명도 감소)
- 예: Primary `#5C67F2` → primary-50 `#EEEFFE` … primary-500 `#5C67F2` … primary-900 `#1E2680`
- 용도: hover 상태, 배지 배경, 비활성 요소, 강조 변형 등

**Neutral (항상 생성)**
- 배경~텍스트 단계 4~5단계 (100~900)

**Semantic (웹 용도 선택 시에만 생성)**
- Success / Warning / Error / Info

**Semantic Alias (항상 생성)**
- 이미 생성된 컬러에 용도 이름을 부여하는 것. 새 색상이 아님.
- `interactive` → Primary
- `destructive` → **Accent 명도 판별 후 결정**
  - Accent가 흰 배경(#FFFFFF) 기준 대비율 **3:1 이상**이면 → Accent 사용
  - 대비율 **3:1 미만** (매우 밝거나 파스텔 톤) → Accent는 배경 틴트 용도이므로 `destructive`에 부적합. 분위기에 맞는 위험 색을 별도 생성:
    - 따뜻한 / 발랄한 계열 → 코랄 레드 계열 (예: `#E8524A`)
    - 미니멀 / 고급스러운 계열 → 딥 레드 계열 (예: `#C0392B`)
    - 강렬한 / 기타 → 진한 오렌지-레드 계열 (예: `#D94F3D`)
  - 생성한 색은 토큰 표에 `color-destructive`로 별도 추가하고 명시
- `positive` → Success (웹 용도 선택 시에만 생성. 그 외 용도에서는 생략)
- `placeholder` → Text 보조색
- `disabled-bg` → Neutral 가장 밝은 단계
- `disabled-text` → Neutral 중간 단계
- 용도: 컴포넌트·문서 적용 시 일관된 의미 기반 참조

**Surface/Background (다크·라이트 각각)**
- 페이지 배경 / 카드 배경 / 오버레이

**Text (다크·라이트 각각)**
- 메인 / 보조 / 흐린(캡션) / 비활성

**Border (다크·라이트 각각)**
- 진한 / 기본 / 연한

### 타이포그래피 토큰

- **Heading Font** (제목용): Display~Heading 4에 적용 — Step 1-b에서 확정한 heading font
- **Body Font** (본문용): Body·Caption에 적용 — Step 1-b에서 확정한 body font
  - heading_font == body_font이면 두 필드에 같은 값 저장
- 사이즈 스케일: **Display** / H1 / H2 / H3 / H4 / Body / Caption (px 단위)
  - Display = H1 × 1.45 (올림), weight 800, line-height tight (1.2) — 표지·히어로 배너용
  - H1 이하는 기존 방식 유지
- 줄간격(Line Height): 제목용(tight) / 본문용(normal) / 넓은(relaxed)
- Google Fonts URL: heading font URL (body font가 다르면 두 URL 모두 기재)

### 기타 토큰 (분위기·용도 기반 자동 매핑)

**Named Radius / Spacing / Shadow** — `references/token-rules.md`를 읽고 분위기·용도 기반 자동 매핑 규칙에 따라 생성한다.

토큰 생성 결과는 텍스트 테이블로 표시 (show_widget 사용 안 함):
- 컬러 토큰 표 (토큰명 | HEX | 역할)
- 타이포그래피 토큰 표 (토큰명 | 값) — Display 포함
- 기타 토큰 표 (Named Radius / Spacing / Shadow)

### 자동 추론 — Brand Personality

위에서 확정된 분위기(Step 1-a)와 실제 색상 톤을 조합해 퍼스낼리티 3단어를 자동 생성한다.

| 분위기 | 기본 방향 |
|--------|----------|
| 미니멀 | 명확한 · 절제된 · 현대적인 |
| 따뜻한 | 친근한 · 포용적인 · 따뜻한 |
| 강렬한 | 대담한 · 에너지있는 · 직접적인 |
| 고급스러운 | 세련된 · 신뢰있는 · 격식있는 |
| 발랄한(Other) | 유쾌한 · 생동감있는 · 가벼운 |

- Primary 색의 채도·명도로 미세 조정 (예: 저채도 미니멀 → '절제된' 강조, 고채도 강렬한 → '에너지있는' 강조)
- 각 단어에 한 줄 설명 생성 (PDF 섹션 A 용도)
- 결과를 `personality` 키로 brand_config에 포함 (형식: `references/brand-config-schema.md` 참조)

### 자동 추론 — Token Hierarchy

Step 3에서 생성한 Semantic Alias 매핑을 바탕으로 Primitive→Semantic→Alias 계층을 자동 파생한다.

- Primary 500 → `interactive` (클릭 가능한 모든 요소)
- Primary 500 → `focus-ring` (포커스 표시)
- Accent / destructive → `destructive` (되돌릴 수 없는 액션)
- Text.Sub → `placeholder` (비활성 텍스트)
- Neutral-100 → `disabled-bg` (비활성 배경)
- 결과를 `token_hierarchy` 키로 brand_config에 포함 (형식: `references/brand-config-schema.md` 참조)

### 자동 추론 — Component Hints

Surface.Card + Named Radius(box) + shadow_level + primary_tints 조합으로 카드·배지·입력 필드 스타일을 자동 생성한다.

- **Card**: Surface.Card(Light) 배경 + Named Radius box + Border.Default + shadow_level
- **Badge**: primary-50 배경 + primary-700 텍스트 + Named Radius badge (항상 pill)
- **Input**: Border.Default 테두리 + Named Radius box + interactive(= Primary) 포커스 색
- 결과를 `component_hints` 키로 brand_config에 포함 (형식: `references/brand-config-schema.md` 참조)

→ Step 4 진행.

---

## Step 4 — 미리보기 & 조정

1. **어드바이스 내부 평가** (modules/common.md 참조) — 렌더링 전 실행, UI 없음
2. **show_widget으로 미리보기 렌더링**:
   - ✅ → 일반 미리보기 (컬러 팔레트 스와치 / 타이포그래피 샘플(Display 포함) / Named Radius·Spacing·Shadow 값)
   - ⚠️/🚨 → 미리보기 상단에 경고 영역 포함 (문제 토큰 + 대안값 + 유지/교체 버튼)

   > **[중요] 테마 독립 렌더링 원칙**: 타이포그래피 샘플·텍스트 위에 색을 올리는 영역은 CSS 변수(`var(--color-background-*)`) 대신 **브랜드 HEX를 직접 지정**한다. 앱의 다크/라이트 테마와 무관하게 브랜드 실제 색상이 정확히 보여야 하기 때문. 구체적으로: 타이포그래피 샘플 컨테이너 → `background: [Surface.Card HEX]` 고정, 텍스트 → `color: [Text.Main HEX]` 고정. 컬러 스와치는 색 자체가 결과물이므로 그대로 HEX 적용.

   > **[중요] Primary 틴트 스케일 렌더링 규칙**: 반드시 아래 형식을 고정으로 사용한다.
   > - **연속 스트립**: 10칸을 gap 없이 이어 붙인다 (`border-radius: 8px; overflow: hidden; height: 44px`)
   > - **500 base 표시**: `box-shadow: inset 0 0 0 3px #fff` (흰 테두리)
   > - **라벨**: 스트립 바로 아래에 50·100·200·300·400·**500**·600·700·800·900 표시. 500 라벨만 `font-weight: 700`으로 굵게 처리
   > - 다른 스타일(알약형, 개별 스와치, 어두운 배경 등)로 변형하지 않는다.

조정 요청 받기:
- "바꾸고 싶은 거 있으면 말씀해주세요" 한 번만 물어봄 (항목별 개별 질문 없음)
- 수정 요청 있으면 반영 후 미리보기 재렌더링
- 없으면 품질 체크 후 Step 5 진행

---

## 품질 체크 (저장 직전)

토큰이 최종 확정된 시점에 아래 3가지를 내부적으로 체크한다. **수식 계산 없이 Claude 판단으로.**

**체크 항목:**
1. **명도 대비** — Primary 500이 흰 배경 위에서 읽히는가 (WCAG AA 4.5:1 기준)
2. **색 충돌** — Primary·Secondary·Accent 세 색이 서로 싸우거나 구분이 안 되는가 (셋 다 강한 보색이거나 셋 다 비슷한 색상)
3. **Neutral 이탈** — Brand 컬러 톤(웜/쿨)과 Neutral 100·900 방향이 정반대인가

**발동 조건:** 3개 중 **2개 이상** 걸릴 때만. 1개는 통과.

**출력:**
```
⚠️ 한 가지만요.
[문제 한 줄 — 예: "Primary가 흰 배경에서 거의 안 보여요"]
이대로 저장할까요, 아니면 한 번 손볼까요?
```

**반응별 처리:**
- "손봐줘" → 해당 항목만 수정 제안 후 미리보기 재렌더링 → 다시 저장 진행
- "그냥 써" → 군말 없이 Step 5 진행

---

## Step 5 — 저장

**스타일 이름 확정**
- **창의적 이름 제안 (필수)**: 선택한 분위기·색상·폰트를 바탕으로 어울리는 이름 1개를 먼저 제안한다.
  - 예: 소프트 핑크+발랄한 → "사쿠라", 딥네이비+미니멀 → "미드나잇", 테라코타+따뜻한 → "어텀"
  - 한 단어, 부르기 쉽고 기억하기 좋은 이름으로. 브랜드명처럼 느껴지게.
- **기본값 병행 제시**: 창의적 이름과 함께 "Design System - N" (기존 bds_ 파일 수 기준 자동 증가)도 옵션으로 알려준다.
- 자유 변경 가능: 사용자가 원하는 이름으로 언제든 바꿀 수 있다.

파일 헤더 형식:
```markdown
# [스타일 이름] 디자인 토큰
> 스타일 이름: [이름]
> 생성일: YYYY-MM-DD | 버전: 1.0
```

**Typography 섹션 저장 형식 (bds_ 파일 내):**
```markdown
## Typography

- Heading Font: [heading_font명]
- Body Font: [body_font명]
  (heading == body이면 두 줄에 같은 값)
- Google Fonts URL: [heading_font CDN URL]
  (body_font가 다르면 다음 줄에 추가)
  - Body Font URL: [body_font CDN URL]
- ※ 온라인 환경에서만 웹폰트 적용됨

| 단계 | 크기 | 굵기 | 행간 | 샘플 |
|------|------|------|------|------|
| Display | ...
```

**bds_ 파일 저장 시 포함할 신규 섹션 3개** (기존 섹션 다음에 순서대로 추가):

```markdown
## Brand Personality
[형용사1] · [형용사2] · [형용사3]

## Token Hierarchy
[primitive_hex] ([primitive_name]) → [alias_name] → "[alias_description}"
... (5~6개)

## Component Hints
Card: bg=[Surface.Card HEX], radius=[box radius], border=[Border.Default HEX], shadow=[shadow_level]
Badge: bg=[primary-50 HEX], text=[primary-700 HEX], radius=100px
Input: border=[Border.Default HEX], radius=[box radius], focus=[Primary HEX]
```

> **하위 호환**: 구 버전 bds_ 파일(신규 섹션 없음)을 load할 때, personality/token_hierarchy/component_hints 키가 없으면 showcase_a.md와 thumbnail.md는 해당 섹션을 생략하고 정상 진행한다.

**저장 위치 확인**
- "어디에 저장할까요?" 한 번 확인
- 기본 제안: 현재 대화 작업 폴더

**파일명 자동 변환 후 저장**
- 스타일 이름 → `bds_[변환된이름].md` (변환 규칙: 영문소문자·한글 유지, 공백·특수문자 제거)
- 저장 완료 메시지: "저장했어요! 이제 'bds_xxx로 PPT 만들어줘' 처럼 부르면 언제든 적용할 수 있어요."

**PPT·문서 사용 시 폰트 설치 안내 (조건부)**
PPT 또는 문서 용도가 선택된 경우, 저장 완료 직후 안내:
```
💡 PPT나 Word 문서에서 이 폰트를 쓰려면 컴퓨터에 설치가 필요해요.
→ Heading: [폰트 다운로드: fonts.google.com/specimen/{heading_font_url}]
→ Body: [폰트 다운로드: fonts.google.com/specimen/{body_font_url}]
   (heading == body이면 한 줄만 표시)
```
- URL 변환: 폰트명 스페이스 → `+`
- Pretendard: `https://github.com/orioncactus/pretendard/releases`
- SUIT: `https://sun.fo/suit/`
- 웹 전용 폰트(쇼케이스용)는 별도 설치 불필요 — 안내 없이 생략

→ Step 6 진행.

---

## Step 6 — 쇼케이스 제안

저장 완료 직후, 딱 한 번만 제안한다:

AskUserQuestion으로 선택지 제시:
- question: "쇼케이스도 만들어드릴까요?"
- 선택지:
  - **ShowCase A — 상세 가이드** — A4 가로 2페이지 HTML. 색상·타이포·토큰과 실사용 예시. PNG/PDF 저장 가능
  - **ShowCase B — 썸네일** — 680×680 카드 HTML. 색상 팔레트·폰트·버튼이 한눈에 보이는 미리보기 이미지
  - **둘 다** — ShowCase A + ShowCase B 순서로 생성
- Other 옵션: "괜찮아요" 등 거절 입력

실행 규칙:
- **ShowCase A** 선택 → `modules/showcase_a.md` 로드 후 실행 (bds_ 파일 탐색 불필요 — 방금 저장한 파일 사용)
- **ShowCase B** 선택 → `modules/thumbnail.md` 로드 후 실행 (동일)
- **둘 다** 선택 → showcase_a.md 실행 완료 후 → thumbnail.md 실행
- **거절** → 종료. "나중에 '썸네일 만들어줘' 또는 '쇼케이스 만들어줘'로 언제든 요청할 수 있어요." 짧게 안내.
