import uvicorn
from fastapi import FastAPI

from app.user import user_router

app = FastAPI()

app.include_router(user_router, prefix='/user')

@app.get("/")
async def index():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) # 개발 시에만 reload