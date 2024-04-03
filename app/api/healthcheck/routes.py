from fastapi import APIRouter
from typing import Any

from app.utils.logger import get_logger

logger = get_logger(__name__)

router = APIRouter(
    prefix="/healthcheck",
    tags=["Healthcheck"],
)


@router.get("/ping", status_code=200)
async def ping() -> str:
    """
    Health ping-pong endpoint
    """
    logger.info("The ping pong endpoint was called")
    return "pong"


@router.post("/echo", status_code=200)
async def echo(request: Any) -> Any:
    """
    Health echo endpoint
    """
    logger.info("The echo endpoint was called")
    return request
