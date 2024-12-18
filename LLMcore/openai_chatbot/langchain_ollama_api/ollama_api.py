import requests
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from typing import List
import random

# FastAPI 서버와 통신하는 Ollama 모델용 함수
def fetch_ollama_response(model_id: str, prompt: str, api_url: str):
    payload = {"model": model_id, "prompt": prompt}
    with requests.post(api_url, json=payload, stream=True) as response:
        if response.status_code == 200:
            for chunk in response.iter_lines():
                if chunk:
                    yield chunk.decode("utf-8")
        else:
            raise Exception(f"Error: {response.status_code}")

# LangChain Tools 정의
@tool("upper_case", return_direct=True)
def to_upper_case(input: str) -> str:
    """Converts the input to uppercase."""
    return input.upper()

@tool("random_number", return_direct=True)
def random_number_maker(_: str) -> int:
    """Returns a random number between 0 and 100."""
    return random.randint(0, 100)

# Tools 목록 반환 함수
def get_langchain_tools():
    return [to_upper_case, random_number_maker]

# LangChain ChatPromptTemplate 생성 함수
def create_ollama_prompt():
    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", "Your name is AdI."),
        ("user", "{input}"),
        ("system", "현재 진행 상태: {agent_scratchpad}")
    ])
    return chat_prompt
