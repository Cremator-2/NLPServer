from typing import Optional
from fastapi import APIRouter, status, HTTPException, Query, Request
from fastapi.responses import PlainTextResponse, JSONResponse


from utils.logger import get_logger
from .processing import TextPreprocessor
from .models import text_request, example_response, example_classificator_response

logger = get_logger(__name__)

router = APIRouter(
    prefix="/processing",
    tags=["Preprocessing and classifying"],
)


@router.post("/preprocessing", status_code=status.HTTP_200_OK, response_class=PlainTextResponse, responses=example_response)
async def preprocessing_text(
        text: str = Query(
            default=text_request,
            description="Text to preprocess"),
        methods: Optional[str] = Query(
            default=None,
            description="""List of preprocessing methods to apply. Possible methods include: 
            'html', 'lowercase', 'urls', 'punctuation', 'stopwords', 'stemming'.
            Example: lowercase,punctuation
            """)):
    if not text:
        raise HTTPException(status_code=400, detail="No text provided for preprocessing")

    preprocessor = TextPreprocessor()

    if methods:
        methods = methods.split(",")
        preprocessed_text = preprocessor.preprocess(text, methods=methods)
    else:
        preprocessed_text = preprocessor.preprocess(text)

    return preprocessed_text


@router.post("/classifying", status_code=status.HTTP_200_OK, response_class=JSONResponse, responses=example_classificator_response)
async def classifying(
        request: Request,
        text: str = Query(
            default=text_request,
            description="Text to classify")):
    if not text:
        raise HTTPException(status_code=400, detail="No text provided for classifying")

    preprocessor = TextPreprocessor()
    preprocessed_text = preprocessor.preprocess(text)

    classificator = request.app.state.classificator
    vectorizer = request.app.state.vectorizer

    preprocessed_text_vectorized = vectorizer.transform([preprocessed_text])

    prediction = classificator.predict(preprocessed_text_vectorized)

    return {"Reference text": text, "Preprocessed text": preprocessed_text, "Prediction": prediction.tolist()[0]}

