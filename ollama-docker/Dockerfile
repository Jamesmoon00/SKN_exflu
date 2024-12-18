# 1. Python Slim 이미지 기반
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# 4. Ollama CLI 설치
RUN curl -fsSL https://ollama.com/install.sh | sh

# 5. OLLAMA_HOST 환경 변수 설정 (리스닝 주소 변경)
ENV OLLAMA_HOST=http://0.0.0.0:11434

# 6. Python 패키지 설치 (필요하면 requirements.txt를 사용)
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 7. 실행 스크립트 복사 및 실행 권한 추가
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# 8. 컨테이너 시작 시 start.sh 실행
CMD ["/app/start.sh"]
