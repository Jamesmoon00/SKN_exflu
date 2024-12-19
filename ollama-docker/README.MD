# Ollama Docker 설정

이 디렉토리는 Ollama를 Docker 컨테이너에서 실행하기 위한 설정 파일들을 포함하고 있습니다. Ollama는 로컬 환경에서 대규모 언어 모델을 실행할 수 있게 해주는 도구입니다.

## 구조
```
ollama-docker/
├── Dockerfile      # Docker 이미지 빌드 설정
├── requirements.txt # Python 패키지 의존성
├── start.sh        # 컨테이너 시작 스크립트
└── README.MD       # 프로젝트 문서
```

## 주요 구성 요소

### Dockerfile
- 기본 이미지: Python 3.9-slim
- 시스템 패키지 설치: curl, unzip
- Ollama CLI 자동 설치
- Python 패키지 설치 환경 구성
- 컨테이너 실행 환경 설정

### requirements.txt
Python 애플리케이션 실행에 필요한 의존성 패키지 목록을 포함합니다.

### start.sh
- 컨테이너 시작 시 자동으로 실행되는 스크립트
- Ollama 서비스 시작 및 초기화 담당

## 환경 설정

### 기본 설정
- `OLLAMA_HOST`: http://0.0.0.0:11434
- 기본 포트: 11434
- 작업 디렉토리: /app

### 시스템 요구사항
- Docker가 설치된 환경
- 최소 8GB RAM 권장
- 충분한 디스크 공간 (모델 크기에 따라 다름)

## 사용 방법

### 1. 이미지 빌드
```bash
docker build -t ollama-custom .
```

### 2. 컨테이너 실행
```bash
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -v ollama-data:/root/.ollama \
  ollama-custom
```

### 3. 상태 확인
```bash
docker ps
docker logs ollama
```

## 모델 관리

### 기본 모델 다운로드
```bash
docker exec -it ollama ollama pull llama2
```

### 모델 실행
```bash
docker exec -it ollama ollama run llama2
```

## 문제 해결

### 일반적인 문제
1. 포트 충돌
   - 11434 포트가 이미 사용 중인 경우 다른 포트로 매핑
   - `docker run -p 11435:11434 ...` 와 같이 변경

2. 메모리 부족
   - Docker 컨테이너 메모리 제한 확인
   - 시스템 리소스 모니터링

3. 네트워크 연결 문제
   - 방화벽 설정 확인
   - Docker 네트워크 설정 확인

## 보안 고려사항
- 프로덕션 환경에서는 적절한 보안 설정 필요
- API 엔드포인트 보호
- 컨테이너 권한 제한