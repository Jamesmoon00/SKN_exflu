from app.common.config import Base
from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, DateTime, Boolean
from datetime import datetime, timedelta
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    kakao_id = Column(String, unique=True, index=True, nullable=True)  # Kakao 고유 ID 추가
    created_at = Column(DateTime, default=datetime.now() + timedelta(hours=9))
    refresh_token = Column(String, nullable=True)  # Refresh Token 저장


# B2B 비즈니스 모델 정의
class BizInfo(Base):
    __tablename__ = "biz_info"
    
    biz_key = Column(Integer, primary_key=True, index=True)
    biz_name = Column(String(50), nullable=False)
    biz_mail = Column(String(50), nullable=False)
    biz_address = Column(String(255), nullable=False)
    biz_phone = Column(String(255), nullable=False)
    biz_manager = Column(String(50), nullable=False)
    category_id = Column(Integer, ForeignKey("ProductCategories.category_id"), default=999)
    
class BizContacts(Base):
    __tablename__ = "biz_contacts"
    
    order_id = Column(Integer, primary_key=True, index = True)
    biz_key = Column(Integer, ForeignKey("biz_info.biz_key"))
    order_date = Column(DateTime, nullable=False, default=datetime.now() + timedelta(hours=9))
    service_name = Column(String(50), nullable=False)
    service_info = Column(String(255), nullable=False)
    budget = Column(Integer, nullable=False)
    period = Column(Integer, nullable=False)
    platform = Column(String(50), nullable=False)
    promo_info = Column(String(255))
    service_target = Column(String(45), nullable=False)
    service_charactors = Column(String(45))
    category_id = Column(Integer, ForeignKey("ProductCategories.category_id"), default = 999)

# blogpost 간편 버전
class BlogPostSimple(Base):
    __tablename__ = "blog_posts_1"

    post_id = Column(Integer, primary_key=True, index=True)  # 블로그 ID
    title = Column(String(255), nullable=False)  # 블로그 제목
    created_at = Column(DateTime, default=datetime.now() + timedelta(hours=9))
    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    is_ad = Column(Boolean, default=False)  # 광고 여부
    comments_count = Column(Integer, default=0)  # 댓글 수 필드
    product_id = Column(Integer, ForeignKey("Products.product_id"))
    content = Column(String(1000), nullable=False)
    image = Column(String(100), nullable=True)
    
    # BlogCommentSimple 관계 설정
    comments = relationship("BlogCommentSimple", back_populates="blog_post")
    

class BlogCommentSimple(Base):
    __tablename__="blogcomment_1"
    
    comment_id = Column(Integer,primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("blog_posts_1.post_id"), nullable=False)
    comment_name = Column(String(50), nullable=False)
    comment_password = Column(String(50), nullable=False)
    comment_content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.now() + timedelta(hours=9))
    
    # BlogPost 관계 설정
    blog_post = relationship("BlogPostSimple", back_populates="comments")

# # BlogPost 모델 정의
# class BlogPost(Base):
#     __tablename__ = "blog_posts"

#     post_id = Column(Integer, primary_key=True, index=True)  # 블로그 ID
#     title = Column(String(255), nullable=False)  # 블로그 제목
#     created_at = Column(DateTime, default=datetime.now() + timedelta(hours=9))
#     views = Column(Integer, default=0)
#     likes = Column(Integer, default=0)
#     is_ad = Column(Boolean, default=False)  # 광고 여부
#     comments_count = Column(Integer, default=0)  # 댓글 수 필드
#     product_id = Column(Integer, ForeignKey("Products.product_id"))

#     # 블록 관계 설정
#     blocks = relationship("ContentBlock", back_populates="blog_post")
    
#     # BlogComment 관계 설정
#     comments = relationship("BlogComment", back_populates="blog_post")

# class ContentBlock(Base):
#     __tablename__ = "content_blocks"
    
#     block_id = Column(Integer, primary_key=True, index=True)
#     post_id = Column(Integer, ForeignKey("blog_posts.post_id"), nullable=False)  # 블로그 ID
#     block_type = Column(Enum("text", "image"), nullable=False)
#     content = Column(Text, nullable=False)
#     block_order = Column(Integer, nullable=False)

#     # BlogPost 관계
#     blog_post = relationship("BlogPostSimple", back_populates="blocks")
    

# class BlogComment(Base):
#     __tablename__="blogcomments"
    
#     comment_id = Column(Integer,primary_key=True, index=True)
#     post_id = Column(Integer, ForeignKey("blog_posts.post_id"), nullable=False)
#     comment_name = Column(String(50), nullable=False)
#     comment_password = Column(String(50), nullable=False)
#     comment_content = Column(Text, nullable=False)
#     created_at = Column(DateTime, default=datetime.now())
    
#     # BlogPost 관계 설정
#     blog_post = relationship("BlogPost", back_populates="comments")


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
    
    # BlogComment 관계 설정
    comments = relationship("SNSComment", back_populates="sns_post")

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
    # SNSPost 관계 설정
    sns_post = relationship("SNSPost", back_populates="comments")

class ProductCategories(Base):
    __tablename__ = 'ProductCategories'

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(50), unique=True)

    # Products 관계 설정
    products = relationship("Products", back_populates="category")


class Products(Base):
    __tablename__ = 'Products'

    product_id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("ProductCategories.category_id"))
    product_name = Column(String(50))
    brand = Column(String(50))
    model = Column(String(50))

    # Categories 관계 설정
    category = relationship("ProductCategories", back_populates="products")

    # Specifications 관계 설정
    laptop_specs = relationship("Specifications_laptop", back_populates="product")
    smartphone_specs = relationship("Specifications_smartphone", back_populates="product")
    tablet_specs = relationship("Specifications_tabletpc", back_populates="product")


class Specifications_laptop(Base):
    __tablename__ = 'Specifications_laptop'

    spec_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("Products.product_id"))
    spec_name = Column(String(100))
    spec_value = Column(String(100))

    # Products 관계 설정
    product = relationship("Products", back_populates="laptop_specs")


class Specifications_smartphone(Base):
    __tablename__ = 'Specifications_smartphone'

    spec_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("Products.product_id"))
    spec_name = Column(String(100))
    spec_value = Column(String(100))

    # Products 관계 설정
    product = relationship("Products", back_populates="smartphone_specs")


class Specifications_tabletpc(Base):
    __tablename__ = 'Specifications_tabletpc'

    spec_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("Products.product_id"))
    spec_name = Column(String(100))
    spec_value = Column(String(100))

    # Products 관계 설정
    product = relationship("Products", back_populates="tablet_specs")