from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import csv
import os
print("=== LOADING DASHBOARD.PY ===")
from database import (
    get_daily_detections,
    get_total_detections,
    get_today_count,
    get_weekly_count,
    get_monthly_count,
    get_latest_detection,
    get_all_detections,
    get_weekly_detections,
    get_confidence_distribution
)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/evidence", StaticFiles(directory="evidence"), name="evidence")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):

    context = {
    "daily_data": get_daily_detections(),
    "total": get_total_detections(),
    "today": get_today_count(),
    "week": get_weekly_count(),
    "month": get_monthly_count(),
    "latest": get_latest_detection(),
    "detections": get_all_detections(),
    "weekly_data": get_weekly_detections(),
    "confidence_data": get_confidence_distribution()
}

    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context=context
    )


@app.get("/download-csv")
def download_csv():

    filename = "detection_history.csv"

    detections = get_all_detections()

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Track ID",
            "Timestamp",
            "Confidence",
            "Evidence"
        ])

        writer.writerows(detections)

    return FileResponse(
        filename,
        media_type="text/csv",
        filename=filename
    )