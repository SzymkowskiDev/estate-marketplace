from fastapi import FastAPI
"""
uvicorn main:app --reload
"""

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
