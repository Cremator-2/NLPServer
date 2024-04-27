from fastapi import APIRouter, status, HTTPException
from fastapi.responses import PlainTextResponse


from utils.logger import get_logger
from .preprocessing import TextPreprocessor
from .models import text_request, example_response

logger = get_logger(__name__)

router = APIRouter(
    prefix="/preprocessing",
    tags=["Preprocessing"],
)


@router.post("/", status_code=status.HTTP_200_OK, response_class=PlainTextResponse, responses=example_response)
async def preprocessing_text(text: str = text_request):
    if not text:
        raise HTTPException(status_code=400, detail="No text provided for preprocessing")

    preprocessor = TextPreprocessor()
    processed_text = preprocessor.preprocess(text)
    return processed_text
