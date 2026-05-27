# 폰트 레퍼런스 — design-system-by-blue

> 조사일: 2026-05-20  
> 소스: Google Fonts / jsDelivr·GitHub / 눈누(noonnu.cc)  
> 기준: 한국어 지원 + 무료 상업 사용 가능 + CDN 로드 가능 우선  
> 용도 표기: H = 헤드라인/타이틀, B = 본문, D = 디스플레이(대형), H+B = 겸용

---

## 범례

| 컬럼 | 설명 |
|------|------|
| 폰트명 | `font-family` 값으로 쓸 이름 |
| 소스 | Google / jsDelivr / 눈누CDN / 눈누DL(다운로드) |
| 웨이트 | 사용 가능한 weight 목록 |
| 용도 | H·B·D |
| CDN | `@import` 또는 `<link>` URL |
| 특성 | 한 줄 설명 |

---

## 1. 미니멀 / 클린

깔끔, 현대, 여백 중시, 기업 UI, 스타트업

| 폰트명 | 소스 | 웨이트 | 용도 | CDN | 특성 |
|--------|------|--------|------|-----|------|
| Noto Sans KR | Google | 100–900 | H+B | `https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700&display=swap` | 범용 안전패, 가독성 최우선 현대 고딕 |
| Gothic A1 | Google | 100–900 | H+B | `https://fonts.googleapis.com/css2?family=Gothic+A1:wght@400;700;900&display=swap` | 기하학적 현대 고딕, 9단계 웨이트 |
| IBM Plex Sans KR | Google | 100–700 | H+B | `https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@300;400;700&display=swap` | IBM 디자인 언어 기반, 테크 기업 느낌 |
| Gowun Dodum | Google | 400 | B | `https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap` | 균형감 있는 돋움 계열, 고요하고 단정 |
| Pretendard | jsDelivr | 100–900 | H+B | `https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard-dynamic-subset.min.css` | 한국 UI 표준 de facto, Inter+본고딕 기반 |
| Pretendard Variable | jsDelivr | Variable | H+B | `https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css` | Pretendard Variable 버전, 최신 브라우저 권장 |
| SUITE | jsDelivr | Variable | H | `https://cdn.jsdelivr.net/gh/sun-typeface/SUITE@2/fonts/variable/woff2/SUITE-Variable.css` | 직각+사선 기하학 조형, 간결한 UI 헤드라인 |
| Wanted Sans | jsDelivr | 100–900 | H+B | `https://cdn.jsdelivr.net/gh/wanteddev/wanted-sans@v1.0.3/packages/wanted-sans/fonts/webfonts/variable/split/WantedSansVariable.min.css` | "기하학적이지만 인간미 있는" 스타트업 감성 |
| LINE Seed Sans KR | npm/jsDelivr | Regular·Bold | H+B | `https://cdn.jsdelivr.net/npm/@kfonts/line-seed-sans-kr@latest/index.css` | LINE 자체 서체, 편의성·친근함 기반 기하학 |
| Spoqa Han Sans Neo | jsDelivr | 100–700 | H+B | `https://cdn.jsdelivr.net/npm/spoqa-han-sans@latest/css/SpoqaHanSansNeo.css` | Noto 기반 경량화, 한/영/일 트리링궐 |
| NanumSquare Neo | jsDelivr | Light–Black | H+B | `https://cdn.jsdelivr.net/gh/moonspam/NanumSquareNeo@1.0/nanumsquareneovar.css` | 나눔스퀘어 후속, 정교한 곡선 |
| Seoul Namsan | jsDelivr | Regular–Bold | H+B | `https://cdn.jsdelivr.net/gh/fonts-archive/SeoulNamsan/subsets/SeoulNamsan-dynamic-subset.css` | 서울시 공식 고딕, 단정하고 현대적 |

---

## 2. 따뜻 / 내추럴

온기, 유기적, 핸드메이드, 자연 소재, 소규모 브랜드

| 폰트명 | 소스 | 웨이트 | 용도 | CDN | 특성 |
|--------|------|--------|------|-----|------|
| Gowun Batang | Google | 400·700 | B | `https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&display=swap` | 온기 있는 바탕체, 긴 글 읽기 편안 |
| Gaegu | Google | 300·400·700 | H | `https://fonts.googleapis.com/css2?family=Gaegu:wght@300;400;700&display=swap` | 노트에 쓴 듯한 친근한 손글씨 |
| Poor Story | Google | 400 | H | `https://fonts.googleapis.com/css2?family=Poor+Story&display=swap` | 꾸밈없이 편안한 손글씨 |
| Gamja Flower | Google | 400 | H | `https://fonts.googleapis.com/css2?family=Gamja+Flower&display=swap` | 감자꽃처럼 동글동글한 손글씨 |
| Nanum Pen Script | Google | 400 | H | `https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap` | 나눔 펜 필기체, 감성적인 손글씨 |
| Nanum Brush Script | Google | 400 | H | `https://fonts.googleapis.com/css2?family=Nanum+Brush+Script&display=swap` | 나눔 붓 필기체, 자연스러운 붓 터치 |
| 빙그레체 | 눈누CDN | Regular | H | `@font-face { font-family: 'Binggrae'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/Binggrae.woff') format('woff'); }` | 빙그레 브랜드 특유의 둥글둥글한 손글씨 고딕 |
| 빙그레 싸만코체 | 눈누CDN | Regular | H | `@font-face { font-family: 'BinggraeSamanco'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-10@1.0/BinggraeSamanco.woff') format('woff'); }` | 쫀득하게 눌린 동글동글 손글씨, 레트로 감성 |
| KCC간판체 | 눈누CDN | Regular | H | `@font-face { font-family: 'KCCGanpan'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/KCC-Ganpan.woff2') format('woff2'); }` | 동네 간판 같은 따뜻하고 귀여운 손글씨 고딕 |
| 카페24 빛나는별 | 눈누CDN | Regular | H | `@font-face { font-family: 'Cafe24Shiningstar'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.1/Cafe24Shiningstar.woff') format('woff'); }` | 기울어진 캘리그라피, 감성 손글씨 |
| 교보손글씨2024 박서우 | 눈누CDN | Regular | H | `@font-face { font-family: 'KyoboHandwriting2024psw'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/2507-1@1.0/KyoboHandwriting2024psw.woff2') format('woff2'); }` | 교보 손글씨 공모전 수상작, 자연스러운 필체 |

---

## 3. 강렬 / 다이나믹

임팩트, 에너지, 대담, 스포츠, 이벤트, 프로모션

| 폰트명 | 소스 | 웨이트 | 용도 | CDN | 특성 |
|--------|------|--------|------|-----|------|
| Black Han Sans | Google | 900 | H·D | `https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap` | 두꺼운 임팩트 고딕, 헤드라인 전용 |
| Gasoek One | Google | 400 | H·D | `https://fonts.googleapis.com/css2?family=Gasoek+One&display=swap` | 강한 가로폭, 강렬한 타이틀용 |
| Do Hyeon | Google | 400 | H | `https://fonts.googleapis.com/css2?family=Do+Hyeon&display=swap` | 에너제틱하고 활기찬 고딕 |
| Sunflower | Google | 300·500·700 | H+B | `https://fonts.googleapis.com/css2?family=Sunflower:wght@300;500;700&display=swap` | 활기찬 해바라기 고딕, 제목·본문 겸용 |
| BM 한나체 Pro | npm/jsDelivr | Regular | H·D | `https://cdn.jsdelivr.net/npm/@kfonts/bm-hanna-pro-otf@latest/index.css` | 두꺼운 획, 경쾌한 배민 대표 디스플레이 |
| BM 한나에어 | npm/jsDelivr | Regular | H | `https://cdn.jsdelivr.net/npm/@kfonts/bm-hanna-air-otf@latest/index.css` | 한나체보다 가볍고 경쾌한 버전 |
| 카페24 아네모네 | 눈누CDN | Regular | H·D | `@font-face { font-family: 'Cafe24Ohsquare'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/Cafe24Ohsquare.woff') format('woff'); }` | 기울어진 강렬한 제목용 장식 고딕 |
| 강원특별자치도체 | 눈누CDN | Regular | H·D | `@font-face { font-family: 'GangwonState'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2307-2@1.0/GangwonState.woff2') format('woff2'); }` | 강원도 자연 모티프, 독특한 제목용 장식체 |

---

## 4. 고급 / 엘레강스

럭셔리, 세련, 정제, 프리미엄, 브랜딩, 패션

| 폰트명 | 소스 | 웨이트 | 용도 | CDN | 특성 |
|--------|------|--------|------|-----|------|
| Noto Serif KR | Google | 200–900 | H+B | `https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300;400;700&display=swap` | 정제된 세리프, 고급스러운 본문·헤드라인 |
| Hahmlet | Google | 100–900 | H+B | `https://fonts.googleapis.com/css2?family=Hahmlet:wght@300;400;700&display=swap` | 대비 강한 현대적 명조, 9단계 웨이트 |
| Nanum Myeongjo | Google | 400·700·800 | B | `https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700;800&display=swap` | 나눔 명조, 품격 있는 본문 세리프 |
| KoPub Batang | Google | 300·500·700 | B | `https://fonts.googleapis.com/css2?family=KoPub+Batang:wght@300;500;700&display=swap` | 출판 전용 바탕체, 긴 글 최적화 |
| KoPubWorld Batang | npm/jsDelivr | Light–Bold | B | `https://cdn.jsdelivr.net/npm/font-kopubworld@1.0/batang.min.css` | KoPub Batang 업그레이드판, 출판 세리프 |
| KoPubWorld Dotum | npm/jsDelivr | Light–Bold | H+B | `https://cdn.jsdelivr.net/npm/font-kopubworld@1.0/dotum.min.css` | 출판용 고딕, 정갈하고 신뢰감 있음 |
| 조선궁서체 | 눈누CDN | Regular | H | `@font-face { font-family: 'ChosunGs'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-04@1.0/ChosunGs.woff') format('woff'); }` | 전통 궁서체, 격조 높은 고전 세리프 |
| 조선일보명조체 | 눈누CDN | Regular | B | `@font-face { font-family: 'ChosunilboMyungjo'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/Chosunilbo_myungjo.woff') format('woff'); }` | 신뢰감 있는 전통 명조 |

---

## 5. 발랄 / 귀여운

캐릭터, 친근, 유머, 아동, 게임, 키즈 브랜드

| 폰트명 | 소스 | 웨이트 | 용도 | CDN | 특성 |
|--------|------|--------|------|-----|------|
| Jua | Google | 400 | H | `https://fonts.googleapis.com/css2?family=Jua&display=swap` | 동글동글 귀여운 고딕, 키즈 대표 서체 |
| Hi Melody | Google | 400 | H | `https://fonts.googleapis.com/css2?family=Hi+Melody&display=swap` | 사랑스럽고 여성스러운 손글씨 |
| Single Day | Google | 400 | H | `https://fonts.googleapis.com/css2?family=Single+Day&display=swap` | 개성 있는 단발머리 손글씨 |
| Cute Font | Google | 400 | H | `https://fonts.googleapis.com/css2?family=Cute+Font&display=swap` | 이름처럼 귀엽고 가벼운 서체 |
| Kirang Haerang | Google | 400 | H | `https://fonts.googleapis.com/css2?family=Kirang+Haerang&display=swap` | 기랑해랑, 장난스럽고 튀는 개성체 |
| 빙그레 싸만코체 | 눈누CDN | Regular | H | (2번 따뜻/내추럴과 동일 URL) | 쫀득하게 눌린 동글동글 레트로 귀여움 |
| KCC간판체 | 눈누CDN | Regular | H | (2번 따뜻/내추럴과 동일 URL) | 간판 손글씨, 귀여운 동네 브랜드 느낌 |
| 만화진흥원체 | 눈누CDN | Regular | H | `@font-face { font-family: 'KOMACON'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_seven@1.2/KOMACON.woff') format('woff'); }` | 만화 말풍선 전용 개발, 또박또박 손글씨 |
| 야놀자야체 | 눈누CDN | Regular | H | `@font-face { font-family: 'YanoljaYache'; src: url('https://gcore.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/YanoljaYacheR.woff') format('woff'); }` | 탈네모꼴 에너제틱, 여행·레저 브랜드 |
| 주아체 | 눈누CDN | Regular | H | `@font-face { font-family: 'BMJUA'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/BMJUA.woff') format('woff'); }` | 둥근 획 안에 강한 에너지, 배민 대표 손글씨 |

---

## 6. 레트로 / 빈티지

복고, 아날로그, 7080, 향수, 뉴트로, 옛 감성

| 폰트명 | 소스 | 웨이트 | 용도 | CDN | 특성 |
|--------|------|--------|------|-----|------|
| Yeon Sung | Google | 400 | H | `https://fonts.googleapis.com/css2?family=Yeon+Sung&display=swap` | 붓글씨 느낌의 복고 고딕 |
| Song Myung | Google | 400 | H+B | `https://fonts.googleapis.com/css2?family=Song+Myung&display=swap` | 옛 활자 느낌, 노스탤지어 명조 |
| Gugi | Google | 400 | H | `https://fonts.googleapis.com/css2?family=Gugi&display=swap` | 레트로 감성의 둥근 고딕 |
| BM 을지로체 | npm/jsDelivr | Regular | H·D | `https://cdn.jsdelivr.net/npm/@kfonts/bm-euljiro@latest/index.css` | 1970년대 을지로 간판 레터링, 거칠고 힘있는 |
| BM 을지로10년후체 | npm/jsDelivr | Regular | H·D | `https://cdn.jsdelivr.net/npm/@kfonts/bm-euljiro-10years-later@latest/index.css` | 을지로체의 세련된 업그레이드 버전 |
| Galmuri11 | npm/jsDelivr | Regular | H·D | `https://cdn.jsdelivr.net/npm/galmuri/dist/galmuri.css` | NDS 닌텐도 DS 픽셀 폰트, 고품질 비트맵 |
| 을지로오래오래체 | 눈누CDN | Regular | H·D | `@font-face { font-family: 'BMEuljirooraeorae'; src: url('https://gcore.jsdelivr.net/gh/projectnoonnu/noonfonts_2110@1.0/BMEuljirooraeorae.woff2') format('woff2'); }` | 마모된 간판 질감, 낡고 오래된 느낌 |
| 도스고딕 | 눈누CDN | Regular | H·D | `@font-face { font-family: 'DOSGothic'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_eight@1.0/DOSGothic.woff') format('woff'); }` | 90년대 PC DOS 화면 감성의 픽셀 고딕 |
| 둥근모꼴Fixedsys | 눈누CDN | Regular | H·D | `@font-face { font-family: 'DungGeunMo'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/DungGeunMo.woff') format('woff'); }` | 둥글게 처리된 픽셀 서체, 옛 전광판 느낌 |

---

## 7. 테크 / 미래적

첨단, 디지털, SF, 스타트업, 코딩, 테크 브랜드

| 폰트명 | 소스 | 웨이트 | 용도 | CDN | 특성 |
|--------|------|--------|------|-----|------|
| Orbit | Google | 400 | H·D | `https://fonts.googleapis.com/css2?family=Orbit&display=swap` | JAMO 제작, 코딩 미학을 한글에 적용한 최신 서체 |
| Nanum Gothic Coding | Google | 400·700 | B | `https://fonts.googleapis.com/css2?family=Nanum+Gothic+Coding:wght@400;700&display=swap` | 나눔 기반 코딩 폰트, 개발자 감성 |
| D2Coding | jsDelivr | Regular·Bold | B | `https://cdn.jsdelivr.net/gh/Joungkyun/font-d2coding/d2coding.css` | 네이버 개발자 코딩 폰트, 한글 특수문자 최적화 |
| Pretendard | jsDelivr | 100–900 | H+B | (1번 미니멀/클린과 동일 URL) | 테크 UI에 가장 많이 쓰이는 한국 오픈소스 |
| IBM Plex Sans KR | Google | 100–700 | H+B | (1번 미니멀/클린과 동일 URL) | IBM 디자인 시스템, 테크 기업 분위기 |

---

## 8. 클래식 / 문학적

전통, 품격, 학문, 출판, 신문, 역사적 콘텐츠

| 폰트명 | 소스 | 웨이트 | 용도 | CDN | 특성 |
|--------|------|--------|------|-----|------|
| Noto Serif KR | Google | 200–900 | H+B | (4번 고급/엘레강스와 동일 URL) | 정통 세리프, 출판·학문적 콘텐츠 기본 |
| Nanum Myeongjo | Google | 400–800 | B | (4번 고급/엘레강스와 동일 URL) | 전통 명조, 긴 글 전용 |
| KoPub Batang | Google | 300–700 | B | (4번 고급/엘레강스와 동일 URL) | 전자책 최적화 바탕체 |
| Jeju Myeongjo | Google | 400 | B | `https://fonts.googleapis.com/css2?family=Jeju+Myeongjo&display=swap` | 제주 명조, 소박하고 전통적인 세리프 |
| Jeju Gothic | Google | 400 | H+B | `https://fonts.googleapis.com/css2?family=Jeju+Gothic&display=swap` | 제주 고딕, 따뜻한 지역 전통 고딕 |
| KoPubWorld Batang | npm/jsDelivr | Light–Bold | B | (4번 고급/엘레강스와 동일 URL) | 출판 세리프 업그레이드 버전 |
| Seoul Namsan | jsDelivr | Regular–Bold | H+B | (1번 미니멀/클린과 동일 URL) | 서울시 공식 서체, 공공 문서 신뢰감 |
| 조선궁서체 | 눈누CDN | Regular | H | (4번 고급/엘레강스와 동일 URL) | 전통 궁서체, 역사·문화 콘텐츠 |
| 조선일보명조체 | 눈누CDN | Regular | B | (4번 고급/엘레강스와 동일 URL) | 신문 명조, 정론 신뢰감 |
| 조선100년체 | 눈누CDN | Regular | H | `@font-face { font-family: 'ChosunCentennial'; src: url('https://gcore.jsdelivr.net/gh/projectnoonnu/noonfonts_2206-02@1.0/ChosunCentennial.woff2') format('woff2'); }` | 100년 세월을 담은 전통 붓글씨 세리프 |
| KCC김훈체 | 눈누CDN | Regular | H | `@font-face { font-family: 'KCCKimHoon'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/KCCKimHoon.woff2') format('woff2'); }` | 소설가 김훈 필체 기반, 강한 문학적 개성 |
| KCC안중근체 | 눈누CDN | Regular | H | `@font-face { font-family: 'KCCAnJungGeun'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/KCCAnJungGeun.woff2') format('woff2'); }` | 안중근 의사 친필 기반, 강직한 붓글씨 |

---

## 9. 아트 / 인디

독창적, 실험적, 갤러리, 감성, 작가주의, 독립 브랜드

| 폰트명 | 소스 | 웨이트 | 용도 | CDN | 특성 |
|--------|------|--------|------|-----|------|
| Nanum Brush Script | Google | 400 | H | (2번 따뜻/내추럴과 동일 URL) | 나눔 붓, 자유로운 붓 터치 |
| Jeju Hallasan | Google | 400 | H·D | `https://fonts.googleapis.com/css2?family=Jeju+Hallasan&display=swap` | 제주 한라산, 독특한 수작업 느낌 |
| Galmuri11 | npm/jsDelivr | Regular | H·D | (6번 레트로/빈티지와 동일 URL) | 픽셀 아트 미학, 게임·인디 감성 |
| KCC환기체 | 눈누CDN | Regular | H | `@font-face { font-family: 'KCCHwangi'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/KCCHwangi.woff2') format('woff2'); }` | 화가 김환기 이름 딴 예술적 서체 |
| 카페24 빛나는별 | 눈누CDN | Regular | H | (2번 따뜻/내추럴과 동일 URL) | 기울어진 캘리그라피 스타일 |
| 마포마포나루 | 눈누CDN | Regular | H | `@font-face { font-family: 'MapoMaponaruA'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/MapoMaponaruA.woff') format('woff'); }` | 마카로 쓴 각진 손글씨, 홍대 로컬 감성 |
| 가비아 봄바람체 | 눈누CDN | Regular | H | `@font-face { font-family: 'GabiaBombaram'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/GabiaBombaram.woff') format('woff'); }` | 봄 느낌의 부드러운 붓글씨 장식체 |
| BM 을지로10년후체 | npm/jsDelivr | Regular | H | (6번 레트로/빈티지와 동일 URL) | 낡은 간판 미학, 아트 프로젝트 감성 |

---

## 10. 스트리트 / 엣지

도시, 힙합, 반항, 서브컬처, 언더그라운드, 젊음

| 폰트명 | 소스 | 웨이트 | 용도 | CDN | 특성 |
|--------|------|--------|------|-----|------|
| Black Han Sans | Google | 900 | H·D | (3번 강렬/다이나믹과 동일 URL) | 압도적 두께, 최강 임팩트 고딕 |
| BM 을지로체 | npm/jsDelivr | Regular | H·D | (6번 레트로/빈티지와 동일 URL) | 을지로 거리 감성, 거칠고 날 것의 서체 |
| BM 한나체 Pro | npm/jsDelivr | Regular | H·D | (3번 강렬/다이나믹과 동일 URL) | 두텁고 경쾌한 거리 감성 |
| 기랑해랑체 | 눈누CDN | Regular | H·D | `@font-face { font-family: 'BMKIRANGHAERANG'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/BMKIRANGHAERANG.woff') format('woff'); }` | 삐뚤빼뚤 불규칙 장식체, 압도적인 개성 |
| 야놀자야체 | 눈누CDN | Regular | H | (5번 발랄/귀여운과 동일 URL) | 탈네모꼴 에너지, 젊고 자유로운 감성 |
| 마포마포나루 | 눈누CDN | Regular | H | (9번 아트/인디와 동일 URL) | 마포·홍대 로컬 스트리트 감성 |
| 강원특별자치도체 | 눈누CDN | Regular | H·D | (3번 강렬/다이나믹과 동일 URL) | 독특한 형태, 강한 지역 개성 |

---

## 다운로드 전용 추천 (CDN 없음, 별도 안내 필요)

CDN이 없어서 스킬에서 직접 로드 불가. 사용자에게 다운로드 후 업로드 안내 필요.

| 폰트명 | 배포처 | 다운로드 | 카테고리 | 특성 |
|--------|--------|---------|---------|------|
| 도스명조 | leedheo (GitHub) | github.com/hurss/fonts | 레트로/문학 | 도스 환경 픽셀 명조 |
| 도스손글씨 | leedheo (GitHub) | github.com/hurss/fonts | 레트로/아트 | 도트 손글씨 느낌 픽셀 서체 |
| 마포 홍대자유체 | 마포구청 | mapo.go.kr | 스트리트/아트 | 홍대 거리 감성 자유로운 손글씨 |
| 교보손글씨 2023 우선아 | 교보문고 | store.kyobobook.co.kr/handwriting/font | 따뜻/아트 | 개성 있는 공모전 수상 필체 |
| 조선가는고딕 | 조선일보 | event.chosun.com | 미니멀/고급 | 날카롭고 세련된 가는 고딕 |

---

## 빠른 참조 — 카테고리별 TOP 픽

| 카테고리 | 고딕/산세리프 1순위 | 명조/세리프 1순위 | 개성 서체 1순위 |
|---------|-----------------|----------------|--------------|
| 미니멀/클린 | Pretendard | KoPubWorld Batang | SUITE |
| 따뜻/내추럴 | LINE Seed Sans KR | Gowun Batang | 빙그레 싸만코체 |
| 강렬/다이나믹 | Black Han Sans | — | BM 한나체 Pro |
| 고급/엘레강스 | KoPubWorld Dotum | Hahmlet | 조선궁서체 |
| 발랄/귀여운 | Jua | — | 주아체 |
| 레트로/빈티지 | Gugi | Song Myung | BM 을지로체 |
| 테크/미래적 | Pretendard | — | Orbit |
| 클래식/문학적 | KoPubWorld Dotum | Noto Serif KR | KCC김훈체 |
| 아트/인디 | — | — | KCC환기체 |
| 스트리트/엣지 | Black Han Sans | — | 기랑해랑체 |
