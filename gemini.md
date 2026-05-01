```markdown id="q1x8vn"
# Gemini Skills (One-Click Workflows)

이 파일은 Gemini 에이전트에서 사용할 수 있는 슬래시 명령어(/) 기반의 워크플로를 정의합니다.

## 1. 사용 가능한 스킬 목록

### 🎬 /slide - 고밀도 전문가 슬라이드 생성 (ULTRA-STRICT)
- **핵심 원칙**: 단순 요약은 실패다. 모든 슬라이드는 **심층 분석**과 **구체적 수치**를 기반으로 작성하라.
    1. **Content Depth (필수)**: 각 슬라이드 본문은 단순 개조식이 아닌, **인과관계와 정량적 임팩트**가 포함된 최소 3~5개의 고밀도 인사이트로 구성한다.
    2. **STRICT Components**: 모든 슬라이드는 반드시 [KPI, Table, Flow, Comparison] 중 하나를 메인으로 하며, 주변 텍스트는 이를 보조하는 상세 분석이어야 한다.
    3. **Expert Voice**: 선택된 페르소나(투자 심사역, CTO 등)의 전문 용어와 날카로운 통찰을 그대로 녹여낸다.
    4. **UI Inclusion**: 모든 `index.html`은 반드시 [PREV, NEXT, ZOOM] 버튼과 Auto-Fit Scaling 로직을 포함해야 한다.

## 💡 Hyperframes 제작 및 운영 가이드
- **Data-Driven Sync (Mandatory)**: 모든 슬라이드 제작 시, 먼저 `slides_data.json`에 슬라이드별 **모든 상세 데이터(KPI 값, 테이블 행/열, Flow 단계, 본문 문장 전체)**를 구조화하여 저장합니다. 
- **1:1 Mirroring**: `index.html`과 `presentation.pptx`는 반드시 이 동일한 JSON 파일을 소스로 사용하여 생성되어야 하며, 단 한 줄의 내용 누락도 허용하지 않습니다.
- **PPT Export (Component-Aware)**: `scripts/export_ppt.py`는 JSON의 `type` 필드를 분석하여 KPI는 강조 도형으로, 테이블은 네이티브 PPT 표로, Flow는 프로세스 다이어그램으로 변환하여 HTML과 100% 동일한 서사를 유지합니다.

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

