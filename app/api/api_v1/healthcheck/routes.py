from typing import Any
from fastapi import APIRouter, status
from fastapi.responses import PlainTextResponse

from .models import example_ping
from utils.logger import get_logger

logger = get_logger(__name__)

router = APIRouter(
    prefix="/healthcheck",
    tags=["Healthcheck"],
)


@router.get("/ping", status_code=status.HTTP_200_OK, response_class=PlainTextResponse, responses=example_ping)
async def ping() -> str:
    """
    Health ping-pong endpoint
    """
    logger.info("The ping pong endpoint was called")
    return "Pong"


@router.post("/echo", status_code=status.HTTP_200_OK)
async def echo(request: Any) -> Any:
    """
    Health echo endpoint
    """
    logger.info("The echo endpoint was called")
    return request
