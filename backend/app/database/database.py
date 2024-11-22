from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import boto3

def get_parameter(name, with_decryption=True):
    """
    AWS Parameter Store에서 값을 가져오는 함수.
    :param name: Parameter Store의 키 이름
    :param with_decryption: 암호화된 값을 복호화 여부 (기본: True)
    :return: Parameter Store에 저장된 값
    """
    client = boto3.client('ssm', region_name="ap-northeast-2")  # AWS 리전 설정
    response = client.get_parameter(
        Name=name,
        WithDecryption=with_decryption
    )
    return response['Parameter']['Value']


# Parameter Store에서 값을 가져옴
db_username = get_parameter("/MYAPP/DB/USERNAME")
db_password = get_parameter("/MYAPP/DB/PASSWORD")
db_host = get_parameter("/MYAPP/DB/HOST")
db_port = get_parameter("/MYAPP/DB/PORT")
db_name = get_parameter("/MYAPP/DB/DB_NAME")

# DATABASE_URL 구성
DATABASE_URL = f"mysql+asyncmy://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

# 비동기 엔진 및 세션 생성
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
