from pydantic import BaseModel

# 요청 데이터 모델 정의
class ItemRequests(BaseModel):
    name: str
    value: int