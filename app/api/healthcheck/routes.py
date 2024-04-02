from fastapi import APIRouter
from typing import Any


router = APIRouter(
    prefix="/healthcheck",
    tags=["Healthcheck"],
)


@router.get("/ping", status_code=200)
async def ping() -> str:
    """
    Health ping-pong endpoint
    """
    return "pong"


@router.post("/echo", status_code=200)
async def echo(request: Any) -> Any:
    """
    Health echo endpoint
    """
    return request
