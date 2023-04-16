"""Dummy FastAPI app for testing."""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Return a simple message."""
    return {"message": "Hello World"}
