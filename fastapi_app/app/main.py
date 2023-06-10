from fastapi import FastAPI

from app.api.routes.conversations import router as conversations_router
from app.api.routes.auth import router as auth_router

app = FastAPI()
app.include_router(conversations_router)
app.include_router(auth_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
