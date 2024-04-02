from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api import healthcheck_router


@asynccontextmanager
async def lifespan(_):
    yield

app = FastAPI(lifespan=lifespan)


app.include_router(healthcheck_router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001,
        log_level="info",
        forwarded_allow_ips="*",
        proxy_headers=True,
    )
