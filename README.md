# AI Smart Surveillance System

An AI-powered smart surveillance system that detects and tracks people in real time, captures evidence only when a new person enters the scene, stores detection records in a SQLite database, and provides a FastAPI-based dashboard for monitoring surveillance statistics.

## Features

* 🎯 Real-time person detection using YOLOv8
* 👤 Multi-object tracking with persistent person IDs
* 🚨 Alert generation only for newly detected individuals
* 📸 Automatic evidence image capture for each new person
* 🗄️ SQLite database for persistent detection logging
* 📊 Detection analytics (total, daily, weekly, monthly)
* 🌐 FastAPI web dashboard
* 🧩 Modular project architecture with separate database layer

---

## Current Workflow

```
Camera
    │
    ▼
YOLOv8 Person Detection
    │
    ▼
Multi-Object Tracking
    │
    ▼
New Person?
    │
    ├── No → Continue Monitoring
    │
    └── Yes
          │
          ▼
Generate Alert
          │
          ▼
Capture Evidence Image
          │
          ▼
Store Detection in SQLite
          │
          ▼
Display Statistics on FastAPI Dashboard
```

---

## Tech Stack

* Python
* YOLOv8 (Ultralytics)
* OpenCV
* SQLite
* FastAPI
* Jinja2
* Uvicorn

---

## Project Structure

```
AI-Smart-Surveillance-System/

│── evidence/
│── static/
│── templates/
│     └── index.html
│
│── database.py
│── dashboard.py
│── database_view.py
│── test_database.py
│── main.py
│── requirements.txt
│── README.md
```

---

## Database Schema

The application stores every new detection in SQLite.

| Column     | Description                  |
| ---------- | ---------------------------- |
| id         | Primary Key                  |
| track_id   | Tracking ID assigned by YOLO |
| timestamp  | Date & time of detection     |
| confidence | Detection confidence         |
| image_path | Path to saved evidence image |

---

## Analytics Supported

The system currently supports:

* Total detections
* Today's detections
* Weekly detections
* Monthly detections
* Latest detection
* Complete detection history

---

## Setup

Clone the repository:

```bash
git clone https://github.com/ishita-chandraa/AI-Smart-Surveillance-System.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the surveillance system:

```bash
python main.py
```

Run the dashboard:

```bash
python -m uvicorn dashboard:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

## Project Status

### ✅ Completed

* Real-time person detection
* Persistent object tracking
* One alert per unique person
* Evidence image capture
* SQLite integration
* Analytics queries
* FastAPI backend
* Initial web dashboard

### 🚧 In Progress

* Dashboard UI improvements
* Evidence gallery
* Detection history table

### 📅 Planned

* Interactive charts
* Real-time dashboard updates
* Email/Telegram alerts
* Multi-camera support
* User authentication
* Docker deployment
* Cloud deployment

---


## Author

**Ishita Chandra**

