from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.api import healthcheck_router
from app.logger import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(_):
    yield

app = FastAPI(lifespan=lifespan)


app.include_router(healthcheck_router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=44596,
        log_level="info",
        forwarded_allow_ips="*",
        proxy_headers=True,
    )
