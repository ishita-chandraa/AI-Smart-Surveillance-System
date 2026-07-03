from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from database import (
    get_total_detections,
    get_today_count,
    get_weekly_count,
    get_monthly_count,
    get_latest_detection,
    get_all_detections
)

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):

    context = {
    "total": get_total_detections(),
    "today": get_today_count(),
    "week": get_weekly_count(),
    "month": get_monthly_count(),
    "latest": get_latest_detection(),
    "detections": get_all_detections()
}

    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context=context
    )
