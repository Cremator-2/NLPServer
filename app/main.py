from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(_):
    yield

app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001,
        log_level="info",
        forwarded_allow_ips="*",
        proxy_headers=True,
    )
