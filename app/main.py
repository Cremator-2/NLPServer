from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.api import healthcheck_router
from app.settings import settings
from app.utils.logger import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(_):
    logger.info(f"Start {settings.PROJECT_NAME}")
    yield

app = FastAPI(lifespan=lifespan)


app.include_router(healthcheck_router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        log_level=settings.LOGGING_LEVEL.lower(),
        forwarded_allow_ips=settings.FORWARDED_ALLOW_IPS,
        proxy_headers=settings.PROXY_HEADERS,
    )
