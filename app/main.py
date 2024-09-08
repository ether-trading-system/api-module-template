import uvicorn
from fastapi import FastAPI
from .routes import *

app: FastAPI = FastAPI()

app.include_router(health_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
