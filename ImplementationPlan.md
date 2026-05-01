# Implementation Plan: Gemini Skills

## 1. 단계별 로드맵
### Phase 1: 기본 인프라 구축
- `gemini.md` 파일 구조 설계
- 슬래시 명령어 파싱 로직 구현

### Phase 2: 핵심 스킬 구현
- `/review`, `/test`, `/doc` 스킬 정의 및 테스트
- 프롬프트 엔지니어링을 통한 품질 최적화

### Phase 3: 시각화 및 자동화
- Mermaid 다이어그램 자동 생성 스킬 추가
- 코드 변경 사항 자동 감지 및 문서화 워크플로 구축

## 2. 기술 스택
- **Language**: Markdown (Documentation), Python (Logic), HTML/CSS (Slides)
- **Tooling**: Gemini CLI, Mermaid.js, Hyperframes, PandasToPowerpoint
- **Environment**: Windows (win32), Node.js v22+, FFmpeg, Python 3.12+

## 3. 구현 일정 (Mermaid)
```mermaid
gantt
    title Gemini Skills Implementation Schedule
    dateFormat  YYYY-MM-DD
    section 인프라
    설계 및 환경 설정       :a1, 2026-05-01, 1d
    명령어 파서 구현       :a2, after a1, 2d
    section 스킬 개발
    핵심 스킬 (/review 등) :b1, after a2, 3d
    PPT 수출 기능 통합    :b2, after b1, 1d
    section Hyperframes
    슬라이드 템플릿 설계   :c1, after b2, 2d
    렌더링 워크플로 자동화 :c2, after c1, 2d
```
