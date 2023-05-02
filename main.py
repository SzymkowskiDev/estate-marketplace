from fastapi import FastAPI
"""
uvicorn main:app --reload

open in: http://127.0.0.1:8000
"""

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
