# LLMcore - AI 챗봇 프로젝트

<div align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
<img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white">
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white">
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/LangChain-339933?style=for-the-badge&logo=Chain&logoColor=white">
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=NumPy&logoColor=white">
<img src="https://img.shields.io/badge/FAISS-00ADD8?style=for-the-badge&logo=Meta&logoColor=white">
<img src="https://img.shields.io/badge/PyTest-0A9EDC?style=for-the-badge&logo=PyTest&logoColor=white">
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white">
<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
</div>

## 프로젝트 개요
이 프로젝트는 OpenAI와 LangChain을 활용한 고급 AI 챗봇 애플리케이션입니다. Streamlit을 사용하여 사용자 친화적인 웹 인터페이스를 제공하며, Docker를 통한 컨테이너화를 지원합니다. 

## 주요 기능

### 1. 멀티페이지 웹 애플리케이션
- **메인 페이지**: 애플리케이션 진입점 및 네비게이션
- **LLM 모델 페이지**: 
  - OpenAI 기반 대화형 챗봇 인터페이스
  - 대화 내용 저장 및 관리 기능
  - 이미지 업로드 지원
  - 광고 설정 기능
- **DB 데이터 검색 페이지**:
  - UUID 또는 Order ID 기반 데이터 조회
  - 데이터 삭제 기능
  - 비즈니스 컨택트 정보 업데이트
  - 실시간 데이터 관리

### 2. LangChain 통합
- 고급 프롬프트 엔지니어링
- 대화 기록 관리
- LangGraph를 활용한 대화 흐름 제어
- 커스텀 체인 구현

### 3. API 통합
- FastAPI 백엔드 연동
- RESTful API 엔드포인트 활용
- 데이터 CRUD 작업 지원

## 기술 스택
### 프론트엔드 ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
- Streamlit
- Streamlit-extras

### 백엔드 ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
- Python 3.10
- FastAPI
- LangChain
- OpenAI ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)

### 데이터베이스 ![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white)
- AWS 서비스 연동 (boto3)

### 인프라 ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
- Docker
- AWS 클라우드 서비스

## 프로젝트 구조
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

## 설치 및 실행 방법

### 로컬 환경에서 실행
1. 저장소 클론:
```bash
git clone [repository-url]
cd LLMcore
```

2. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

3. 애플리케이션 실행:
```bash
cd openai_chatbot
streamlit run main.py
```

### Docker를 통한 실행
1. Docker 이미지 빌드:
```bash
docker build -t llmcore .
```

2. Docker 컨테이너 실행:
```bash
docker run -p 8502:8502 llmcore
```

## API 엔드포인트
- 기본 URL: `https://backdocsend.jamesmoon.click`
- 주요 엔드포인트:
  - `/blog/add`: 블로그 포스트 추가
  - `/bizcontacts`: 비즈니스 컨택트 관리
  - `/process`: 데이터 처리

## 포트 정보
- 기본 포트: 8502 (Streamlit 웹 서버)

## 의존성 패키지
### 웹 프레임워크 ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
- streamlit
- streamlit-extras

### AI/ML ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
- openai
- langchain
- langchain_core
- langchain_openai
- langchain-community
- langgraph

### 클라우드/데이터베이스 ![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white)
- boto3

### 유틸리티 ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
- datetime
- pandas

## 보안 및 환경 설정
- OpenAI API 키 필요
- AWS 자격 증명 설정 필요 (boto3 사용 시)
- 환경 변수를 통한 설정 관리

## 기여 방법
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request