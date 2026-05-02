# 🍏 High-Fidelity Slide Maker with Hyperframes

이 프로젝트는 **Apple의 미니멀리즘 디자인**과 **Hyperframes의 비디오 기술**을 결합하여, 단순한 슬라이드를 넘어 전문가 수준의 **비디오 프레젠테이션**과 **파워포인트 문서**를 자동으로 생성하는 지능형 시스템입니다.

## ✨ 핵심 기능

- **Apple 디자인 시스템**: `design.md`에 정의된 Apple의 미학(Photography-first, Minimal UI)을 100% 준수합니다.
- **Paperlogy 타이포그래피**: 국문/영문에 최적화된 Paperlogy 폰트와 'Apple tight' 자간을 적용하여 전문성을 높였습니다.
- **지능형 자동 분류 (/auto-slide)**: 입력된 문서를 분석하여 투자 제안(Type A), 데이터 분석(Type B), 기술 명세(Type C) 등 5가지 전문 양식 중 최적의 타입을 선택하여 슬라이드를 구성합니다.
- **데이터 기반 동기화**: 단일 JSON 마스터 데이터를 소스로 사용하여 Hyperframes 비디오와 파워포인트(PPTX) 문서를 100% 동일한 내용으로 생성합니다.
- **Strict Compliance**: KPI Block, Table, Flow Diagram, Comparison Layout 등 전문 보고용 컴포넌트 사용을 강제하여 콘텐츠의 밀도를 보장합니다.

## 📁 폴더 구조

```text
.
├── src/                # 자동화 스크립트 (PPT 변환, 서버 가동 등)
├── data/               # 슬라이드 마스터 데이터 (JSON)
├── assets/             # 이미지 및 디자인 자산
├── renders/            # 비디오 렌더링 결과물 (MP4)
├── index.html          # Hyperframes 마스터 슬라이드 소스
├── design.md           # 디자인 가이드라인 및 토큰
├── gemini.md           # 에이전트 스킬 및 운영 가이드
└── README.md           # 프로젝트 가이드
```

## 🚀 시작하기

### 1. 환경 설정
- **Node.js**: v22 이상 필수
- **Python**: 3.12+ (pandas, python-pptx 라이브러리 필요)
- **FFmpeg**: 시스템 경로에 설치 필수 (비디오 렌더링용)

### 2. 주요 명령어
- **슬라이드 프리뷰**: `powershell -File src/preview.ps1` (항상 3000번 포트에서 실행)
- **비디오 렌더링**: `npx hyperframes render`
- **PPT 변환**: `python src/export_ppt.py data/slides_data.json`
- **자동 배포**: `/ship` (문서 업데이트 + Git 푸시)

## 📊 최근 생성된 슬라이드 (Latest)
- **AI 에이전트 도입 전략 (2026-05-02)**: Gemini CLI 기반의 개발 생산성 혁신 보고서 ([Gemini_Strategic_Master_20260502.html](./Gemini_Strategic_Master_20260502.html))
- **Gemini vs Codex 비교 (2026-05-02)**: 차세대 에이전트와 레거시 도구의 기술적 격차 분석 ([Gemini_vs_Codex_20260502.html](./Gemini_vs_Codex_20260502.html))

## 🍏 슬라이드 생성 규칙 (Ultra-Strict)
모든 슬라이드는 반드시 아래 중 하나 이상의 컴포넌트를 포함해야 합니다:
1. **KPI Block**: 수치 및 핵심 지표 시각화
2. **Data Table**: 정밀 비교 및 분석 테이블
3. **Flow Diagram**: 전략 로드맵 및 프로세스
4. **Comparison**: Legacy vs Innovation 대비 레이아웃

---
*Built with Gemini CLI & Hyperframes*
