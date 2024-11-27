from app.common.config import Base
from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

# BlogPost 모델 정의
class BlogPost(Base):
    __tablename__ = "blog_posts"

    post_id = Column(Integer, primary_key=True, index=True)  # 블로그 ID
    title = Column(String(255), nullable=False)  # 블로그 제목
    created_at = Column(DateTime, default=datetime.utcnow)

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