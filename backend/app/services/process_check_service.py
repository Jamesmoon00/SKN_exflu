from app.schemas.process_check import ItemRequests

async def process_item(item: ItemRequests):
    # 클라이언트에서 받은 데이터를 처리 후 반환
    return {"message": f"Received {item.name} with value {item.value}"}