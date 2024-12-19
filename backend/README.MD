# SKN03-FINAL-4Team Backend

## 기술 스택 개요
<div align="center">
  <h3>🛠 Backend Framework & Language</h3>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=SQLAlchemy&logoColor=white">
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=Pydantic&logoColor=white">
  <img src="https://img.shields.io/badge/Uvicorn-4051B5?style=for-the-badge&logo=Uvicorn&logoColor=white">
  <br>
  
  <h3>💾 Database</h3>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white">
  <br>
  
  <h3>🔐 Authentication</h3>
  <img src="https://img.shields.io/badge/Google_OAuth-4285F4?style=for-the-badge&logo=Google&logoColor=white">
  <img src="https://img.shields.io/badge/Kakao_OAuth-FFCD00?style=for-the-badge&logo=Kakao&logoColor=black">
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white">
  <br>
  
  <h3>🤖 AI Integration</h3>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=OpenAI&logoColor=white">
  <img src="https://img.shields.io/badge/LangChain-121212?style=for-the-badge&logo=Chain&logoColor=white">
  <img src="https://img.shields.io/badge/Ollama-FF4B4B?style=for-the-badge&logo=Ollama&logoColor=white">
  <br>
  
  <h3>☁️ Cloud & Deploy</h3>
  <img src="https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=Amazon-AWS&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white">
  <br>
  
  <h3>⚙️ Development Tools</h3>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
  <img src="https://img.shields.io/badge/PyTest-0A9EDC?style=for-the-badge&logo=PyTest&logoColor=white">
</div>



## 상세 기술 스택

### 주요 프레임워크 및 라이브러리 <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=FastAPI&logoColor=white"> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white">
- **FastAPI**: 고성능 비동기 웹 프레임워크
  - CORS 미들웨어 지원
  - 세션 관리
  - 로깅 미들웨어
  - OpenAPI (Swagger) 문서 자동 생성
  - 비동기 요청 처리
  - 의존성 주입 시스템
- **SQLAlchemy**: Python SQL 툴킷 및 ORM
  - 비동기 데이터베이스 작업 지원
  - 모델 기반 데이터베이스 관리
  - 마이그레이션 도구 (Alembic)
  - 트랜잭션 관리
- **Uvicorn**: 고성능 ASGI 서버
- **Pydantic**: 데이터 검증 및 설정 관리
  - JSON 스키마 생성
  - 타입 검증
  - 환경 변수 관리
- **OpenAI & LangChain**: AI 기능 구현
  - GPT 모델 통합
  - AI 기반 컨텐츠 생성
  - Ollama 모델 통합

### 데이터베이스 <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white">
- **MySQL**: 메인 데이터베이스
  - asyncmy: 비동기 MySQL 드라이버
  - pymysql: 동기 MySQL 드라이버
  - 트랜잭션 관리
  - 연결 풀링
  - 인덱스 최적화

### 인증 및 보안 <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=JSON%20web%20tokens&logoColor=white"> <img src="https://img.shields.io/badge/OAuth-4285F4?style=flat-square&logo=Google&logoColor=white">
- **소셜 로그인**:
  - Google OAuth2.0 인증
  - Kakao OAuth 인증
- **JWT**: JSON Web Token 기반 인증
  - PyJWT
  - python-jose
- **Passlib**: 비밀번호 해싱 (bcrypt)
- **Session Middleware**: 세션 기반 상태 관리

### 클라우드 및 인프라 <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white"> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white">
- **AWS 서비스**:
  - AWS SDK (boto3)
  - AWS CodeBuild
  - CI/CD 파이프라인
- **Docker**: 컨테이너화
  - 멀티스테이지 빌드
  - 환경 변수 관리

### 개발 도구 <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=white"> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"> <img src="https://img.shields.io/badge/PyTest-0A9EDC?style=flat-square&logo=pytest&logoColor=white">
- **Loguru**: 구조화된 로깅
  - 로그 레벨 관리
  - 로그 포맷팅
  - 파일 로깅
- **Pytest**: 테스트 프레임워크
- **Python-dotenv**: 환경 변수 관리

## 프로젝트 구조

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
│   │   ├── biz_contacts.py    # 비즈니스 세부정보 API
│   │   ├── biz_info.py        # 비즈니스 정보 API
│   │   ├── blog.py            # 블로그 관련 API
│   │   ├── core_check.py      # 핵심 기능 점검 API
│   │   ├── core.py            # 핵심 기능 API
│   │   ├── ollama.py          # ollama API
│   │   ├── google_auth.py     # Google 인증
│   │   ├── healthcheck.py     # AWS healthcheck 인증
│   │   ├── kakao_auth.py      # Kakao 인증
│   │   ├── sns.py             # SNS 통합 API
│   │   └── test.py            # 기능 테스트 API
│   │   
│   ├── schemas/               # Pydantic 모델/스키마
│   │   ├── blog.py            # 블로그 관련 스키마
│   │   ├── biz_contacts.py    # 비즈니스 연락처 스키마
│   │   ├── biz_info.py        # 비즈니스 정보 스키마
│   │   ├── core.py            # 핵심 기능 스키마
│   │   ├── exaone.py          # ExaOne 관련 스키마
│   │   ├── healthcheck.py     # 헬스체크 스키마
│   │   ├── process_check.py   # 프로세스 체크 스키마
│   │   ├── sns.py             # SNS 관련 스키마
│   │   ├── test.py            # 테스트 관련 스키마
│   │   └── user.py            # 사용자 관련 스키마
│   │
│   ├── services/              # 비즈니스 로직
│   │   ├── blog_service.py    # 블로그 서비스
│   │   ├── biz_contacts_service.py  # 비즈니스 연락처 서비스
│   │   ├── biz_info_service.py      # 비즈니스 정보 서비스
│   │   ├── core_service.py          # 핵심 기능 서비스
│   │   ├── core_check_service.py    # 핵심 기능 체크 서비스
│   │   ├── exaone_service.py        # ExaOne 서비스
│   │   ├── google_auth.py           # Google 인증 서비스
│   │   ├── healthcheck_service.py   # 헬스체크 서비스
│   │   ├── process_check_service.py # 프로세스 체크 서비스
│   │   ├── sns_service.py           # SNS 서비스
│   │   └── test_service.py          # 테스트 서비스
│   │
│   ├── main.py                # 애플리케이션 진입점
│   ├── logger.py              # 로깅 설정
│   └── settings.py            # 환경 설정
│   
├── app.log                    # 애플리케이션 로그 파일
├── requirements.txt           # 의존성 패키지 목록
├── Dockerfile                 # Docker 빌드 설정
└── buildspec.yml              # AWS CodeBuild 설정
```

## API 엔드포인트

### 1. 인증 관련
- `/auth/google`: Google OAuth2.0 인증
- `/auth/kakao`: Kakao OAuth 인증
- `/auth/token`: JWT 토큰 발급/갱신

### 2. 비즈니스 기능
- `/blog`: 블로그 관련 CRUD 작업
- `/sns`: SNS 통합 및 관리
- `/biz-info`: 비즈니스 정보 관리
- `/biz-contacts`: 비즈니스 연락처 관리

### 3. 시스템 관리
- `/healthcheck`: 시스템 상태 확인
- `/process-check`: 프로세스 모니터링
- `/core-check`: 핵심 기능 상태 확인

## 주요 기능

1. **API 서버**
   - RESTful API 설계
   - 비동기 처리
   - 미들웨어 기반 로깅
   - CORS 지원

2. **데이터베이스 관리**
   - ORM 기반 데이터 모델링
   - 비동기 쿼리 처리
   - 트랜잭션 관리
   - 마이그레이션 지원

3. **인증 시스템**
   - 소셜 로그인 (Google, Kakao)
   - JWT 기반 인증
   - 세션 관리
   - 보안 토큰 관리

4. **로깅 시스템**
   - 구조화된 로그 관리
   - 요청/응답 로깅
   - 에러 트래킹
   - 성능 모니터링

5. **AI 통합**
   - OpenAI API 활용
   - Ollama API 활용
   - 컨텐츠 생성
   - 자연어 처리

6. **클라우드 통합**
   - AWS 서비스 연동
   - 클라우드 스토리지 관리
   - 서버리스 기능 통합

## 설치 및 실행

1. 의존성 설치:
```bash
pip install -r requirements.txt
```

2. 환경 변수 설정:
`.env` 파일 생성:
```env
DATABASE_URL=mysql+asyncmy://user:password@localhost:3306/dbname
JWT_SECRET_KEY=your-secret-key
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
KAKAO_CLIENT_ID=your-kakao-client-id
OPENAI_API_KEY=your-openai-api-key
```

3. 데이터베이스 설정:
```bash
# MySQL 데이터베이스 생성
mysql -u root -p
CREATE DATABASE dbname;
```

4. 서버 실행:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 배포

### Docker 배포
```bash
# 이미지 빌드
docker build -t backend-app .

# 컨테이너 실행
docker run -d -p 8000:8000 --env-file .env backend-app
```

### AWS 배포
- CodeBuild를 통한 자동 배포
- `buildspec.yml`에 정의된 파이프라인 실행
- 환경 변수는 AWS Systems Manager Parameter Store에서 관리

## 모니터링

- 헬스체크 엔드포인트: `/healthcheck`
- 프로세스 모니터링: `/process-check`
- 로그 확인: `app.log` 파일
- AWS CloudWatch 통합 모니터링

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

## 로깅 시스템

### 로그 레벨
- **DEBUG**: 개발 중 상세 정보
- **INFO**: 일반적인 작동 정보
- **WARNING**: 주의가 필요한 상황
- **ERROR**: 오류 상황
- **CRITICAL**: 심각한 오류 상황

### 로그 형식
```
[시간] [로그레벨] [모듈] - 메시지
```

### 로그 저장
- 파일명: `app.log`
- 로그 순환: 일일 단위
- 최대 보관 기간: 30일

## 성능 최적화

### 데이터베이스
- 커넥션 풀링 설정
- 인덱스 최적화
- 쿼리 캐싱

### API 응답
- 비동기 처리
- 응답 압축
- 캐시 헤더 설정

### 메모리 관리
- 메모리 누수 방지
- 가비지 컬렉션 최적화
- 리소스 제한 설정

## 보안 설정

### API 보안
- Rate Limiting
- IP 화이트리스팅
- Request Validation

### 데이터 보안
- 암호화 전송 (HTTPS)
- 데이터 암호화 저장
- SQL Injection 방지

### 인증 보안
- 토큰 만료 관리
- 세션 보안
- CSRF 방지