```markdown id="q1x8vn"
# Gemini Skills (One-Click Workflows)

이 파일은 Gemini 에이전트에서 사용할 수 있는 슬래시 명령어(/) 기반의 워크플로를 정의합니다.

## 1. 고밀도 전략 슬라이드 파이프라인 (The 5-Step Pipeline)
... (기존 내용 유지)

---

## 2. 전략 보고서 마스터 템플릿 (The 12-Slide Gold Standard)

에이전트는 심층 분석 요청 시 아래 12슬라이드 구조를 기본 모델로 채택한다.

1.  **Slide 1: 표지 (Title)** - 명확한 제목 + 필요성을 강조한 부제 (삼성 블루 포인트)
2.  **Slide 2: 핵심 요약 (Exec Summary)** - "So What"에 대한 답을 우선 제시 (불렛 포인트)
3.  **Slide 3: 시장 동향 (Market Trends)** - 3개 축(기술/소비자/규제 등) 기반 타일 구조
4.  **Slide 4: 포지셔닝 (Landscape)** - 4분면 차트 기반 기호 영역 및 위협 시각화
5.  **Slide 5~6: 경쟁사 분석 (Deep Dive)** - 이미지 + 위협 요인 중심의 심층 분석
6.  **Slide 7: 비교표 (Matrix)** - 정성적 기호(◎ 매우 우수, ○ 우수, △ 보통, × 미흡) 활용
7.  **Slide 8: 데이터 시각화 (Quant)** - 거버닝 메시지(제목)가 수치를 해석하는 구조
8.  **Slide 9: 소비자 반응 (VOC)** - Pro/Con 대비 또는 키워드 클라우드 형태
9.  **Slide 10: 전략 진단 (SWOT)** - 단순 나열이 아닌 '교차 분석(SO/ST/WO/WT)' 결과 도출
10. **Slide 11: 실행 과제 (Action Plan)** - 분기별 로드맵(Timeline) 중심
11. **Slide 12: 클로징 (Q&A)**

---

## 3. 사용 가능한 스킬 목록
...
    3. **Qualitative Symbols**: 비교표 작성 시 정성적 기호(◎, ○, △, ×)를 적극 활용하여 직관성을 높인다.
    4. **Action Titling (강제)**: 모든 제목은 현상이 아닌 **결론**을 담는다.


### 🛠️ /heal - 슬라이드 렌더링 자가 치유 (Self-Healing)
- **목적**: 브라우저 보안 정책(CORS)으로 인한 '빈 화면' 또는 '데이터 로드 실패'를 즉시 해결.
- **실행 로직**:
    1. 대상 HTML 파일의 스크립트 영역을 분석한다.
    2. `data/slides_data.json`의 최신 내용을 추출한다.
    3. HTML 내의 `const slides = [...]` 부분을 최신 데이터로 전면 교체(Full Embedding)한다.
    4. 파일 인코딩을 **UTF-8 with BOM**으로 재저장하여 한글 깨짐을 원천 차단한다.

### 🚀 /ship - 문서 최종 업데이트 및 자동 푸시 (Auto-Sync)
- **목적**: 작업 완료 후 주요 문서(README.md, PRD, SRS 등)를 프로젝트의 최신 상태로 갱신하고 Git에 자동 푸시.
- **실행 로직**:
    1. **문서 동기화**: 
       - `README.md`의 '최근 생성된 슬라이드' 및 '주요 업데이트 내역' 섹션을 갱신한다.
       - `ImplementationPlan.md`의 진행률을 실제 파일 생성 여부에 따라 체크(v)한다.
    2. **스테이징**: 변경된 모든 소스 코드와 새로 생성된 HTML/JSON 결과물을 `git add` 한다.
    3. **자동 커밋**: "[Release] Update docs and sync slides [YYYYMMDD]" 형식으로 커밋 메시지를 생성한다.
    4. **원격 푸시**: 현재 브랜치를 `origin`으로 푸시한다.
- **강제 규칙**: 푸시 전 반드시 `index.html`이 `/heal` 상태인지 확인하여 렌더링 결함이 없는 상태로 배포한다.

---

## 2. 워크플로 운영 규칙

### 🔄 슬라이드 생성 및 변환 프로세스 (STRICT)
1. **슬라이드 생성 (/slide)**: 
   - 요청 시 `data/slides_data.json` (최신본) 및 `data/slides_data_[YYYYMMDD].json` (히스토리)을 생성합니다.
   - `[요약키워드]_[YYYYMMDD].html` 형식으로 HTML 파일을 생성합니다.
   - **중요 - 렌더링 검증 (Validation)**: 생성 직후 HTML 소스를 읽어 데이터가 정상적으로 임베딩되었는지 확인합니다. 만약 `fetch` 로직이 남아있거나 내용이 비어있다면 즉시 **`/heal` 스킬을 호출**하여 치료합니다.
2. **PPT 변환 (/ppt)**:
   - 사용자가 명시적으로 "PPT 만들어줘"라고 요청할 때만 실행합니다.

### 📁 파일명 생성 규칙
- **HTML 슬라이드**: `[주요_키워드]_[오늘날짜].html`
  - 예: `Gemini_vs_Codex_20260502.html`
- **데이터 소스**: 항상 `data/slides_data.json`을 최신본으로 유지합니다.

## 3. 슬라이드 데이터 스키마 규칙 (JSON 강제)
에이전트는 HTML 생성 전, 반드시 다음 형식을 갖춘 `slides_data.json`을 작성해야 한다.

```json
[
  {
    "id": "slide_1",
    "type": "hero",
    "title": "제목",
    "content": "상세 분석 내용 전체",
    "theme": "light/dark/parchment"
  },
  {
    "type": "kpi",
    "title": "수치 분석",
    "kpis": [{"value": "100", "label": "설명"}],
    "insights": ["인사이트 1", "인사이트 2"]
  },
  {
    "type": "table",
    "title": "정밀 비교",
    "headers": ["항목", "기존", "목표"],
    "rows": [["데이터", "값", "값"]]
  },
  {
    "type": "flow",
    "title": "로드맵",
    "steps": ["단계 1", "단계 2", "단계 3"]
  }
]
```

### ① KPI Block (수치 중심 분석)
```html
<div class="kpi-container">
  <div class="kpi-block">
    <div class="kpi-value">값 (단위)</div>
    <div class="kpi-label">수치에 대한 전략적 해석 및 근거 상세 기술</div>
  </div>
</div>
```

### ② Data Table (정밀 분석)
```html
<table class="apple-table">
  <thead><tr><th>분석 지표</th><th>현재 상태 (Before)</th><th>전략적 목표 (After)</th><th>기대 효과</th></tr></thead>
  <tbody>...</tbody>
</table>
```

### ③ Flow Diagram (전략 로드맵)
```html
<div class="flow-container">
  <div class="flow-step">전략 수립</div><div class="flow-arrow">→</div>
  <div class="flow-step">자원 배치</div><div class="flow-arrow">→</div>
  <div class="flow-step">실행 및 최적화</div>
</div>
```

### ④ Comparison (전략적 대비)
```html
<div class="comparison-layout">
  <div class="comp-box light"><h3>Legacy / Risk</h3><p>방치 시 발생할 정량적 손해 상술</p></div>
  <div class="comp-box dark"><h3>Innovation / Gain</h3><p>도입 시 얻게 될 재무적/전략적 이득 상술</p></div>
</div>
```

---

## 3. 슬라이드 생성 규칙

### 1. Context First
- 반드시 `design.md` 선확인

---

### 2. Document Analysis (핵심 엔진)

#### Step 1. 정보 추출
- 수치 / 주장 / 기술 / 리스크 / 로드맵
→ **원문 유지 상태로 분해**

#### Step 2. 의미 재배치
- 삭제 금지 / 요약 금지
- **슬라이드 목적에 맞게 재배열**

#### Step 3. 타입 매핑
- Type A ~ E 자동 분류

---

## 3-1. Type A (Strategic Pitch)

→ 설득형 구조

강화:
- KPI 카드 필수
- 메시지 + 수치 결합
- 최소 10슬라이드

---

## 3-2. Type B (Insight Analytics)

→ 데이터 분석 구조

강화:
- KPI 카드 + 비교 테이블 필수
- Insight 최소 3개

---

## 3-3. Type C (Tech Showcase)

→ 기술 구조

강화:
- Architecture 다이어그램 필수
- Feature → 문제 해결 연결

---

## 3-4. Type D (Problem-Solution)

→ 문제 해결 구조

강화:
- Before/After 필수
- Impact 수치화

---

## 3-5. Type E (Executive Briefing)

→ 임원 보고

강화:
- 3초 이해 구조
- KPI + Risk 포함

---

## 4. Visual Structuring Engine (핵심 추가)

### ⚠️ 강제 규칙 (절대 위반 금지)
- 모든 슬라이드는 반드시 아래 중 최소 1개 포함:
  - KPI Block
  - Table
  - Flow Diagram
  - Comparison Layout
- **텍스트만 있는 슬라이드 생성 금지**
- **설명문 단독 구조 금지**
- 위 조건 미충족 시 슬라이드 생성 실패로 간주

---

### 4-1. Table 자동 생성

조건:
- 비교 / 항목 ≥ 3

출력:

```

| 항목 | 현재 | 개선 | 효과 |
| -- | -- | -- | -- |

```

---

### 4-2. Card Grid

조건:
- 핵심 포인트 ≥ 3

구성:
- Title
- KPI (필수)
- 설명 1줄

---

### 4-3. Infographic (Flow)

조건:
- 흐름 존재 시

출력:

```

Problem → Solution → Impact

```

---

### 4-4. KPI Highlight (강제 적용)

조건:
- 수치 존재 시 무조건 적용

출력 예시:

```

<div class="kpi">
  <h1>100조</h1>
  <p>수주잔고</p>
</div>
```

---

### 4-5. Comparison Block (강제 적용)

조건:

* Before/After 또는 경쟁 구조 존재 시

출력 예시:

```
<table>
<tr><th>Before</th><th>After</th></tr>
</table>
```

---

## 5. Slide Composition Rule (강제)

모든 슬라이드는 반드시 아래 중 하나 포함:

1. KPI Block
2. Table
3. Card Grid
4. Flow Diagram
5. Comparison Layout

추가 규칙:

* 텍스트 only 슬라이드 생성 금지
* 5줄 이상 문단 금지
* 수치 없는 주장 금지

---

## 6. Content → Visual 자동 변환 (강제 매핑)

* 수치 포함 → KPI Block 생성 (필수)
* 비교 문장 → Table 생성 (필수)
* 전략/항목 ≥3 → Card Grid 생성
* 단계/프로세스 → Flow Diagram 생성
* 문제 vs 결과 → Comparison Layout 생성

→ 변환 미적용 시 생성 실패 처리

---

## 7. Visual Rhythm

* Light → 정보
* Dark → 메시지
* Parchment → 전환

---

## 8. Pill Action

* CTA는 반드시 행동 유도형

---

## 9. Rendering Flow

```mermaid
graph TD
    Input([/]Command) --> Logic{문서 분석}
    Logic --> Structure[구조 재배치]
    Structure --> Visual[시각 구조 생성 (강제 규칙 적용)]
    Visual --> SlideGen[슬라이드 생성]
    SlideGen --> Output[최종 결과]
```

---

## 10. 금지 규칙

* 텍스트만 슬라이드 금지
* 수치 없는 주장 금지
* 시각 요소 없는 슬라이드 금지

---

*참고: Chrome Skills 기반*

```

