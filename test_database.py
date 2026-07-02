from database import (
    get_total_detections,
    get_today_count,
    get_weekly_count,
    get_monthly_count,
    get_latest_detection,
    get_all_detections,
    get_detections_between,
    get_daily_statistics
)

print("Total:", get_total_detections())

print("Today:", get_today_count())

print("Week:", get_weekly_count())

print("Month:", get_monthly_count())

print("Latest:", get_latest_detection())

print("\nAll Detections:")
for row in get_all_detections():
    print(row)

print("\nDetections Between 2026-06-30 and 2026-07-03:")
rows = get_detections_between(
    "2026-06-30",
    "2026-07-03"
)

for row in rows:
    print(row)

print("\nDaily Statistics:")
stats = get_daily_statistics()

for date, count in stats:
    print(f"{date} : {count}")