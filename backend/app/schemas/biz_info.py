from pydantic import BaseModel
from typing import Literal, List
from datetime import datetime

class BizInfoDataRequests(BaseModel): # DB에서 블로그 제목 저장
    biz_name: str 
    biz_mail: str
    biz_address: str
    biz_phone: str
    biz_manager: str
    category_id: int = 999
    Q1:str
    Q2:str
    Q3:str
    Q4:str
    Q5:str
    
class BizInfoResponse(BaseModel):
    biz_key: int
    biz_name: str 
    biz_mail: str
    biz_address: str
    biz_phone: str
    biz_manager: str
    category_id: int = 999
    Q1:str
    Q2:str
    Q3:str
    Q4:str
    Q5:str
    class Config:
        from_attributes = True