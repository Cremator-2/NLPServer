from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
import nltk
from joblib import load

from api import healthcheck_router, similarity_router, processing_router
from routers import plot_router, page_router
from core.config import settings
from utils.logger import get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(_):
    nltk.download('stopwords')
    app.state.classificator = load('static/ml_models/lr_tfidf_model.joblib')
    app.state.vectorizer = load('static/ml_models/tfidf_vectorizer.joblib')
    logger.info(f"Start {settings.PROJECT_NAME}")
    yield

app = FastAPI(lifespan=lifespan)


app.include_router(healthcheck_router)
app.include_router(similarity_router)
app.include_router(processing_router)
app.include_router(plot_router)
app.include_router(page_router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8001,
        log_level=settings.LOGGING_LEVEL.lower(),
        forwarded_allow_ips="*",
        proxy_headers=True,
    )
