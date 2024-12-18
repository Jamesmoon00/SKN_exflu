#!/bin/bash

# Ollama 서버 시작
ollama serve &
SERVER_PID=$!

# 서버가 완전히 시작될 때까지 대기
echo "Waiting for Ollama server to start..."
sleep 10  # 서버 초기화 시간을 충분히 확보

# 모델 다운로드
ollama pull exaone3.5

# 서버 유지
wait $SERVER_PID
