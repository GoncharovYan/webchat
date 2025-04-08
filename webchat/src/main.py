from fastapi import FastAPI
import uvicorn

from contextlib import asynccontextmanager
from webchat.common.database import create_tables, drop_tables
from webchat.common.config import settings
from webchat.src.router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    await create_tables()
    yield


app = FastAPI(
    lifespan=lifespan
)
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.FASTAPI_HOST,
        port=settings.FASTAPI_PORT
    )
