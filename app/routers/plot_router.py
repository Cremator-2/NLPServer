from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

from utils.logger import get_logger

logger = get_logger(__name__)

router = APIRouter(
    prefix="/plot",
    tags=["Plots"],
)


@router.get("/example", response_class=HTMLResponse)
async def example_plot():
    try:
        return HTMLResponse(content=open("static/plots/example_plot.html", encoding="utf-8").read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Contact page not found")
