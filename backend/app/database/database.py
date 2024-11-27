from app.common.config import AsyncSessionLocal

# 세션 생성 함수
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()  # 세션이 반드시 닫히도록 설정
