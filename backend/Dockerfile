# 베이스 이미지 선택 (Python 3.10 사용)
FROM python:3.10-slim

# 작업 디렉토리 생성
WORKDIR /app

# 필요 패키지 설치 (리눅스 종속성)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 종속성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 소스 코드 복사
COPY . .

# FastAPI 애플리케이션 실행 포트 설정 (ECS에서는 8000 사용)
EXPOSE 8020

# Define the Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s CMD curl -f http://localhost:8020/health || exit 1

# FastAPI 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8020"]
