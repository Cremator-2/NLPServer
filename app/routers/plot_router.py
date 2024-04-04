from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

router = APIRouter(
    prefix="/plot",
    tags=["Plots"],
)


@router.get("/example", response_class=HTMLResponse)
async def example_plot():
    """
    Example plot page
    """
    try:
        return HTMLResponse(content=open("static/plots/example_plot.html", encoding="utf-8").read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Contact page not found")
