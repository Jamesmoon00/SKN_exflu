from pydantic import BaseModel
from typing import Literal, List

class TitleCreate(BaseModel): # DB에서 블로그 제목 저장
    title: str
    
class ContentBlock(BaseModel): # DB에서 블로그 글 본문 저장
    block_id: int
    post_id: int
    block_type: str
    content: str
    block_order: int
    
class Content(BaseModel):
    block_type: Literal["text", "image"]  # 블록 유형: "text" 또는 "image"
    content: str  # 텍스트 내용 또는 이미지 URL
    block_order: int  # 블록 순서

class BlogContent(BaseModel):
    post_id: int
    blocks: List[Content]  # 블록들의 리스트