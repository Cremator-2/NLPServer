
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
import textdistance
from .models import SimilarityRequest, example_response

from utils.logger import get_logger

logger = get_logger(__name__)

router = APIRouter(
    prefix="/similarity",
    tags=["Similarity"],
)


@router.post("/", status_code=status.HTTP_200_OK, response_class=JSONResponse, responses=example_response)
async def calculate_similarity(request: SimilarityRequest):
    """Calculates text similarity using a given method"""
    method = request.method.lower()
    available_methods = {
        "jaccard": textdistance.Jaccard(),
        "cosine": textdistance.Cosine(),
        "levenshtein": textdistance.Levenshtein(),
        "hamming": textdistance.Hamming(),
        "sorensen": textdistance.Sorensen(),
        "overlap": textdistance.Overlap(),
        "damerau_levenshtein": textdistance.DamerauLevenshtein(),
        "jaro": textdistance.JaroWinkler(),
        "strcmp95": textdistance.StrCmp95(),
        "needleman_wunsch": textdistance.NeedlemanWunsch(),
        "gotoh": textdistance.Gotoh(),
        "smith_waterman": textdistance.SmithWaterman()
    }

    if method not in available_methods:
        raise HTTPException(status_code=400, detail="Unsupported similarity method")

    similarity_score = available_methods[method].similarity(request.line1, request.line2)

    return {
        "method": request.method,
        "line1": request.line1,
        "line2": request.line2,
        "similarity": similarity_score
    }
