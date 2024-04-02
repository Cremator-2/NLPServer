from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/healthcheck",
    tags=["healthcheck"],
)


@router.get("/ping")
async def ping():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"answer": "pong"})


@router.post("/echo")
async def echo(request: Request):
    return JSONResponse(status_code=status.HTTP_200_OK, content=await request.json())
