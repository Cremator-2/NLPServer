from pydantic import BaseModel, Field


line1 = "Я хочу услышать больше о вашей организации"
line2 = "Расскажите подробнее о вашей компании"


class SimilarityRequest(BaseModel):
    method: str = Field(..., example="levenshtein")
    line1: str = Field(..., example=line1)
    line2: str = Field(..., example=line2)


example_response = {
    200: {
        "description": "A successful response",
        "content": {
            "application/json": {
                "example": {
                    "method": "Levenshtein",
                    "line1": line1,
                    "line2": line2,
                    "similarity": 15
                }
            }
        }
    }
}
