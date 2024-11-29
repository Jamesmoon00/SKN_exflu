from app.common.config import Base
from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, DateTime, Boolean
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship

# BlogPost 모델 정의
class BlogPost(Base):
    __tablename__ = "blog_posts"

    post_id = Column(Integer, primary_key=True, index=True)  # 블로그 ID
    title = Column(String(255), nullable=False)  # 블로그 제목
    created_at = Column(DateTime, default=datetime.now() + timedelta(hours=9))
    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    is_ad = Column(Boolean, default=False)  # 광고 여부
    comments_count = Column(Integer, default=0)  # 댓글 수 필드
    product_id = Column(Integer, ForeignKey("Products.product_id"))

    # 블록 관계 설정
    blocks = relationship("ContentBlock", back_populates="blog_post")

class ContentBlock(Base):
    __tablename__ = "content_blocks"
    
    block_id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("blog_posts.post_id"), nullable=False)  # 블로그 ID
    block_type = Column(Enum("text", "image"), nullable=False)
    content = Column(Text, nullable=False)
    block_order = Column(Integer, nullable=False)

    # BlogPost 관계
    blog_post = relationship("BlogPost", back_populates="blocks")

class BlogComment(Base):
    __tablename__="blogcomments"
    
    comment_id = Column(Integer,primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("blog_posts.post_id"), nullable=False)
    comment_name = Column(String(50), nullable=False)
    comment_password = Column(String(50), nullable=False)
    comment_content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now() + timedelta(hours=9))
    


# SNSPost 모델 정의
class SNSPost(Base):
    __tablename__ = "sns_posts"

    post_id = Column(Integer, primary_key=True, index=True)  # SNS ID
    title = Column(String(255), nullable=False)  # SNS 제목
    created_at = Column(DateTime, default=datetime.now() + timedelta(hours=9))
    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    is_ad = Column(Boolean, default=False)  # 광고 여부
    comments_count = Column(Integer, default=0)  # 댓글 수 필드
    product_id = Column(Integer, ForeignKey("Products.product_id"))

    # 블록 관계 설정
    blocks = relationship("ContentBlockForSNS", back_populates="sns_post")

class ContentBlockForSNS(Base):
    __tablename__ = "content_blocks_for_sns"
    
    block_id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("sns_posts.post_id"), nullable=False)  # SNS ID
    block_type = Column(Enum("text", "image"), nullable=False)
    content = Column(Text, nullable=False)
    block_order = Column(Integer, nullable=False)

    # SNSPost 관계
    sns_post = relationship("SNSPost", back_populates="blocks")

class SNSComment(Base):
    __tablename__="snscomments"
    
    comment_id = Column(Integer,primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("sns_posts.post_id"), nullable=False)
    comment_name = Column(String(50), nullable=False)
    comment_password = Column(String(50), nullable=False)
    comment_content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now() + timedelta(hours=9))

class ProductCategories(Base):
    __tablename__='ProductCategories'

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(50), unique=True)

class Products(Base):
    __tablename__ = 'Products'

    product_id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer)
    product_name = Column(String(50))
    brand = Column(String(50))
    model = Column(String(50))

class Specifications_laptop(Base):
    __tablename__ = 'Specifications_laptop'

    spec_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    spec_name = Column(String(100))
    spec_value = Column(String(100))

class Specifications_smartphone(Base):
    __tablename__ = 'Specifications_smartphone'

    spec_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    spec_name = Column(String(100))
    spec_value = Column(String(100))

class Specifications_tabletpc(Base):
    __tablename__ = 'Specifications_tabletpc'

    spec_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    spec_name = Column(String(100))
    spec_value = Column(String(100))