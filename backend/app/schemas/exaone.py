from pydantic import BaseModel

# Pydantic 모델: 입력 데이터 정의
class PromptRequest(BaseModel):
    model: str = "exaone3.5"
    prompt: str