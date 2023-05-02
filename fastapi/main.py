from fastapi import FastAPI
"""
uvicorn fastapi\main:app --reload
"""

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
