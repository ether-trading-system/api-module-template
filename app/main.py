import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI
from core import init_models, engine
from core.db.seed import is_database_empty, seed_database
from .routes import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    if await is_database_empty(engine):
        await init_models()
        await seed_database()
    yield


app: FastAPI = FastAPI(lifespan=lifespan)

app.include_router(health_router)
app.include_router(wines_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
