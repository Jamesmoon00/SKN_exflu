# SKN03-FINAL-4TEAM

## Backend 구조

```
backend/
├── app/                       # 메인 애플리케이션 디렉토리
│   ├── auth/                  # 인증 관련 모듈
│   │   ├── token.py           # JWT 토큰 관리
│   │   └── oauth.py           # OAuth 인증
│   │   
│   ├── common/                # 공통 유틸리티
│   │   ├── config.py          # 공통 변수 관리
│   │   ├── consts.py          # 공통 상수 관리
│   │   └── utils.py           # 유틸리티 함수
│   │   
│   ├── database/              # 데이터베이스 설정 및 모델
│   │   ├── database.py        # DB 연결 설정
│   │   └── models.py          # SQLAlchemy 모델
│   │   
│   ├── router/                # API 엔드포인트
│   │   ├── biz_contacts.py    # 비즈니스 세부부정보 API
│   │   ├── biz_info.py        # 비즈니스 정보 API
│   │   ├── blog.py            # 블로그 관련 API
│   │   ├── core_check.py      # 핵심 기능 점검검 API
│   │   ├── core.py            # 핵심 기능 API
│   │   ├── google_auth.py     # Google 인증
│   │   ├── healthcheck.py     # AWS healthcheck 인증
│   │   ├── kakao_auth.py      # Kakao 인증
│   │   ├── sns.py             # SNS 통합 API
│   │   └── test.py            # 기능 테스트 API
│   │   
│   ├── schemas/               # Pydantic 모델/스키마
│   ├── services/              # 비즈니스 로직
│   ├── main.py                # 애플리케이션 진입점
│   ├── logger.py              # 로깅 설정
│   └── settings.py            # 환경 설정
│   
├── requirements.txt           # 의존성 패키지 목록
├── Dockerfile                 # Docker 빌드 설정
└── buildspec.yml              # AWS CodeBuild 설정
```

## Backend 기술 스택

- FastAPI: 고성능 웹 프레임워크
- PostgreSQL: 관계형 데이터베이스
- SQLAlchemy: ORM
- Alembic: 데이터베이스 마이그레이션
- PyJWT: JWT 인증
- WebSocket: 실시간 통신
- pytest: 테스트 프레임워크

### 사용 기술 스택
<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=SQLAlchemy&logoColor=white">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white">
  <img src="https://img.shields.io/badge/Google_OAuth-4285F4?style=for-the-badge&logo=Google&logoColor=white">
  <img src="https://img.shields.io/badge/Kakao_OAuth-FFCD00?style=for-the-badge&logo=Kakao&logoColor=black">
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=OpenAI&logoColor=white">
  <img src="https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=Amazon-AWS&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
  <img src="https://img.shields.io/badge/PyTest-0A9EDC?style=for-the-badge&logo=PyTest&logoColor=white">
</div>

## Backend 주요 기능

### 1. 사용자 인증
- JWT 기반 인증 시스템
- 회원가입/로그인
- 토큰 갱신

### 2. 채팅 기능
- WebSocket 기반 실시간 채팅
- 채팅방 생성 및 관리
- 메시지 저장 및 조회

### 3. 사용자 관리
- 사용자 프로필 관리
- 권한 관리

## Backend 설치 및 실행

### 사전 요구사항
- Python 3.9+
- PostgreSQL 13+

### 설치 방법
```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 환경변수 설정
cp .env.example .env
# .env 파일 수정

# 데이터베이스 마이그레이션
alembic upgrade head

# 서버 실행
uvicorn main:app --reload
```

### 환경변수 설정 (.env)
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## API 문서
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 테스트
```bash
# 테스트 실행
pytest
```

## 개발 가이드라인
- Python 코드 스타일: Black + isort
- 테스트 커버리지 유지
- 커밋 메시지: Conventional Commits 형식 사용


---

## Frontend 구조

```
frontend/
├── public/                    # 정적 파일
├── src/
│   ├── components/           # 재사용 가능한 컴포넌트
│   │   ├── chat/            # 채팅 관련 컴포넌트
│   │   │   ├── ChatBox.tsx
│   │   │   ├── MessageList.tsx
│   │   │   └── InputBox.tsx
│   │   ├── common/          # 공통 컴포넌트
│   │   │   ├── Button.tsx
│   │   │   ├── Input.tsx
│   │   │   └── Modal.tsx
│   │   └── layout/          # 레이아웃 컴포넌트
│   │       ├── Header.tsx
│   │       └── Sidebar.tsx
│   │
│   ├── pages/               # 페이지 컴포넌트
│   │   ├── auth/
│   │   │   ├── LoginPage.tsx
│   │   │   └── RegisterPage.tsx
│   │   ├── chat/
│   │   │   └── ChatPage.tsx
│   │   └── Home.tsx
│   │
│   ├── services/            # API 서비스
│   │   ├── api.ts
│   │   ├── authService.ts
│   │   └── chatService.ts
│   │
│   ├── store/              # Redux 상태관리
│   │   ├── slices/
│   │   │   ├── authSlice.ts
│   │   │   └── chatSlice.ts
│   │   └── store.ts
│   │
│   ├── utils/             # 유틸리티 함수
│   │   ├── axios.ts
│   │   └── websocket.ts
│   │
│   ├── App.tsx
│   └── main.tsx
│
├── package.json
└── vite.config.ts
```

## Frontend 기술 스택

### 핵심 기술
- React 18
- TypeScript
- Vite (빌드 도구)
- TailwindCSS (스타일링)

### 상태 관리
- Redux Toolkit
- React Query (서버 상태 관리)

### 통신
- Axios (HTTP 클라이언트)
- Socket.io-client (웹소켓)

### UI/UX
- TailwindCSS
- HeadlessUI
- React Icons

### 사용 기술 스택
<div align="center">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=React&logoColor=black">
  <img src="https://img.shields.io/badge/Redux-764ABC?style=for-the-badge&logo=Redux&logoColor=white">
  <img src="https://img.shields.io/badge/React_Query-FF4154?style=for-the-badge&logo=React-Query&logoColor=white">
  <img src="https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=Axios&logoColor=white">
  <img src="https://img.shields.io/badge/Socket.io-010101?style=for-the-badge&logo=Socket.io&logoColor=white">
  <img src="https://img.shields.io/badge/ESLint-4B32C3?style=for-the-badge&logo=ESLint&logoColor=white">
  <img src="https://img.shields.io/badge/Prettier-F7B93E?style=for-the-badge&logo=Prettier&logoColor=black">
  <img src="https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white">
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=Node.js&logoColor=white">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
</div>

## Frontend 주요 기능

### 1. 인증 시스템
- 로그인/회원가입 페이지
- JWT 토큰 관리
- 인증 상태 유지

### 2. 블로그 인터페이스
- 게시글 작성 및 수정
- 댓글 및 좋아요 기능
- 마크다운 에디터 지원

### 3. 반응형 디자인
- 모바일 대응 레이아웃 
- 동적 이벤트 효과
  - 눈 내리는 효과
  - 스크롤 애니메이션
  - 호버 인터랙션

## Frontend 설치 및 실행

### 사전 요구사항
- Node.js 16+
- npm 또는 yarn

### 설치 방법
```bash
# 의존성 설치
npm install

# 개발 서버 실행
npm run dev
```

### 환경변수 설정 (.env)
```
VITE_API_URL=http://localhost:3000
VITE_WS_URL=ws://localhost:3000
```

## 개발 가이드라인

### 코드 스타일
- ESLint + Prettier 설정 준수
- TypeScript strict 모드 사용
- 컴포넌트 단위 테스트 작성

### 컴포넌트 작성 규칙
- 함수형 컴포넌트 사용
- Props 타입 명시
- 재사용 가능한 컴포넌트 분리

### 상태 관리
- 전역 상태: Redux Toolkit
- 서버 상태: React Query
- 로컬 상태: React useState

## 빌드 및 배포
```bash
# 프로덕션 빌드
npm run build

# 빌드 미리보기
npm run preview
```

---

# LLMCore 구조

```
LLMcore/
├── openai_chatbot/
│   ├── main.py                   # 메인 애플리케이션 진입점
│   ├── pages/
│   │   ├── llm_model.py          # LLM 챗봇 인터페이스
│   │   └── DB_Data_Search.py     # 데이터베이스 검색 인터페이스
│   │
│   ├── langchain_openai_api/      # LangChain 관련 모듈
│   │   ├── langgraph/
│   │   │   ├── agent.py          # langgraph agent 설정
│   │   │   ├── graph.py          # langgraph compile 로직 설정
│   │   │   ├── nodes.py          # langgraph nodes 정의
│   │   │   ├── state.py          # langgraph state 정의
│   │   │   └── tools.py          # langgraph tools 정의의
│   │   └── taviny/
│   │       └──taviny.py          # 검색 엔진 모듈듈
│   │ 
│   ├── chat.py                   # 챗봇 핵심 로직
│   ├── chain.py                  # LangChain 체인 구현
│   ├── constant.py               # 상수 정의
│   ├── model.py                  # 모델 설정
│   ├── prompt.py                 # 프롬프트 템플릿
│   └── utils.py                  # 유틸리티 함수
│ 
├── dockerfile                    # Docker 컨테이너 설정
├── requirements.txt              # 프로젝트 의존성
└── buildspec.yml                 # AWS 빌드 설정
```

## LLMCore 기술 스택

### 핵심 기술
- OpenAI GPT API
- LangChain
- Python 3.9+

### 데이터 처리
- NumPy
- Pandas
- FAISS (벡터 데이터베이스)

### 유틸리티
- python-dotenv
- tiktoken (토큰 계산)
- logging

### 사용 기술 스택
<div align="center">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=OpenAI&logoColor=white">
  <img src="https://img.shields.io/badge/LangChain-339933?style=for-the-badge&logo=Chain&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=NumPy&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=Pandas&logoColor=white">
  <img src="https://img.shields.io/badge/FAISS-00ADD8?style=for-the-badge&logo=Meta&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white">
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=Amazon%20AWS&logoColor=white">
  <img src="https://img.shields.io/badge/PyTest-0A9EDC?style=for-the-badge&logo=PyTest&logoColor=white">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
</div>

## LLMCore 주요 기능

### 1. 챗봇 엔진
- GPT 모델 기반 대화 처리
- 컨텍스트 관리
- 프롬프트 엔지니어링

### 2. 메모리 관리
- 대화 히스토리 관리
- 컨텍스트 윈도우 최적화
- 토큰 사용량 모니터링

### 3. 프롬프트 관리
- 다양한 페르소나 템플릿
- 동적 프롬프트 생성
- 프롬프트 최적화

## LLMCore 설치 및 실행

### 사전 요구사항
- Python 3.9+
- OpenAI API 키

### 설치 방법
```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

### 환경변수 설정 (.env)
```
OPENAI_API_KEY=your_openai_api_key
MODEL_NAME=gpt-3.5-turbo
MAX_TOKENS=4096
TEMPERATURE=0.7
VECTOR_DB_PATH=./vector_db
```

## 개발 가이드라인

### 코드 스타일
- Black 포맷팅
- Type hints 사용
- 문서화 (Docstring)

### 모델 관리
- 모델 버전 관리
- 프롬프트 템플릿 버전 관리
- 성능 메트릭 모니터링

### 에러 처리
- API 오류 처리
- 토큰 제한 관리
- 재시도 메커니즘

## 테스트
```bash
# 단위 테스트 실행
pytest tests/

# 통합 테스트 실행
pytest tests/integration/
```

## 모니터링 및 로깅
- API 사용량 모니터링
- 응답 시간 측정
- 에러 로깅