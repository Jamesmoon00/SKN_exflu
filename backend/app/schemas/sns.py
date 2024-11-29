from pydantic import BaseModel
from typing import Literal, List
from datetime import datetime

class TitleCreate(BaseModel): # DB에서 sns 제목 저장
    title: str
    
class ContentBlock(BaseModel): # DB에서 sns 글 본문 저장
    post_id: int
    block_type: str
    content: str
    block_order: int


class CommentCreate(BaseModel): # 댓글 저장
    post_id: int
    comment_name: str
    comment_password: str
    comment_content: str

class CommentResponse(BaseModel): # 댓글 응답
    comment_id: int
    post_id: int
    comment_name: str
    comment_content: str

    class Config:
        from_attribures = True

class Block(BaseModel):
    block_type: Literal["text", "image"]  # 블록 유형: "text" 또는 "image"
    content: str  # 텍스트 내용 또는 이미지 URL
    block_order: int  # 블록 순서

class SNSContent(BaseModel):
    post_id: int
    is_ad: bool = False  # 광고 여부 기본값 False
    blocks: List[Block]  # 블록들의 리스트
    
class SNSCommentCountReapone(BaseModel):
    post_id: int
    comments_count: int