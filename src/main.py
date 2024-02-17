from fastapi import FastAPI
from src.routes.student import router

app = FastAPI()


@app.get("/")
async def home():
    return "Home"


app.include_router(router, prefix="/api/v1")