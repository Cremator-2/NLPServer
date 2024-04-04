import json
from typing import Dict

from fastapi import APIRouter, Request, status, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from models import successful_response_example_dict


router = APIRouter(
    tags=["Webhook viewer"]
)


@router.post("/webhook", deprecated=True, response_model=Dict, responses=successful_response_example_dict)
async def webhook(request: Request, body: Dict = Body(..., example={"key": "value"})) -> JSONResponse:
    request_data = await request.json()
    print(json.dumps(request_data, indent=4, ensure_ascii=False))
    return JSONResponse(content=jsonable_encoder(request_data), status_code=status.HTTP_200_OK)
