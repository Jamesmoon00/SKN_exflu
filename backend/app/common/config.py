from app.common.consts import REGION_NAME
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
import boto3

# def get_parameter(name, with_decryption=True):
#     """
#     AWS Parameter Store에서 값을 가져오는 함수.
#     :param name: Parameter Store의 키 이름
#     :param with_decryption: 암호화된 값을 복호화 여부 (기본: True)
#     :return: Parameter Store에 저장된 값
#     """
#     client = boto3.client('ssm', region_name="ap-northeast-2")  # AWS 리전 설정
#     response = client.get_parameter(
#         Name=name,
#         WithDecryption=with_decryption
#     )
#     return response['Parameter']['Value']

def get_parameter(name, with_decryption=True):
    client = boto3.client('ssm', region_name="ap-northeast-2")
    try:
        response = client.get_parameter(
            Name=name,
            WithDecryption=with_decryption
        )
        return response['Parameter']['Value']
    except client.exceptions.ParameterNotFound:
        raise ValueError(f"Parameter '{name}' not found in AWS SSM.")
    except Exception as e:
        raise ValueError(f"AWS SSM 요청 중 오류 발생: {str(e)}")



# Parameter Store에서 값을 가져옴
db_username = get_parameter("/MYAPP/DB/USERNAME")
db_password = get_parameter("/MYAPP/DB/PASSWORD")
db_host = get_parameter("/MYAPP/DB/HOST")
db_port = get_parameter("/MYAPP/DB/PORT")
db_name = get_parameter("/MYAPP/DB/DB_NAME")
s3_name = get_parameter("/MYAPP/S3/NAME")
s3_key = get_parameter("/MYAPP/S3/KEY")

# DATABASE_URL 구성
DATABASE_URL = f"mysql+asyncmy://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

# KAKAO AUTH

kakao_id = get_parameter("/MYAPP/KAKAO/AUTH/NAME")
kakao_pwd = get_parameter("/MYAPP/KAKAO/AUTH/PWD")
kakao_redirect_url = "http://127.0.0.1:8000/auth/kakao/callback"
#"https://backdocsend.jamesmoon.click/auth/kakao/callback"

# S3 클라이언트 생성
s3_client = boto3.client(
    "s3",
    aws_access_key_id=s3_name,
    aws_secret_access_key=s3_key,
    region_name=REGION_NAME,
)

# 비동기 엔진 및 세션 생성
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
Base = declarative_base()