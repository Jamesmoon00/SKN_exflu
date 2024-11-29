from app.router import blog, core, core_check, process_check, healthcheck, test, sns, biz_info, biz_contacts
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import base64


app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST, DELETE 등)
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)
# 라우터 등록
app.include_router(healthcheck.router)
app.include_router(process_check.router)
app.include_router(blog.router)
app.include_router(sns.router)
app.include_router(core.router)
app.include_router(biz_info.router)
app.include_router(biz_contacts.router)
app.include_router(core_check.router)
app.include_router(test.router)

# 실행
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)