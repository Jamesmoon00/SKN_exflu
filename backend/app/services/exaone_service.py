from fastapi import HTTPException
from app.schemas.exaone import PromptRequest
from app.common.config import OLLAMA_API_URL
import requests
import json

def generate_ollama_exaone_service(payload: dict):
    """
    Ollama 서버에 스트리밍 요청을 보내고 'response' 필드를 실시간으로 yield 합니다.
    """
    try:
        # timeout=(connect timeout, read timeout) 설정 추가
        response = requests.post(OLLAMA_API_URL, 
                            json=payload, 
                            stream=True, 
                            timeout=(20, 300))  # 연결 10초, 읽기 300초
        if 400 <= response.status_code < 600:
            yield json.dumps({"error": "Failed to fetch response from Ollama server"})
            return
        
        for line in response.iter_lines():
            if line:  # 빈 줄 제외
                try:
                    data = json.loads(line.decode("utf-8"))  # 각 라인을 JSON으로 파싱
                    response_text = data.get("response", "")  # 'response' 필드 추출
                    yield response_text  # 청크 단위로 반환
                except json.JSONDecodeError:
                    continue  # JSON 파싱 에러는 무시
    except Exception as e:
        yield json.dumps({"error": str(e)})