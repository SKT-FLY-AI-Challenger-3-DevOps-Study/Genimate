import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.user import user_router
from app.email import email_router
from app.generate import generate_router

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix='/user')
app.include_router(email_router, prefix='/email')
app.include_router(generate_router, prefix='/generate')

@app.get("/")
async def index():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False) # 개발 시에만 reload