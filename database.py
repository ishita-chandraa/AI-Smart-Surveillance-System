import sqlite3

def get_connection():
    return sqlite3.connect("detections.db")

def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detections (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        track_id INTEGER,

        timestamp TEXT,

        confidence REAL,

        image_path TEXT

    )
    """)

    conn.commit()

    conn.close()


def insert_detection(track_id, timestamp, confidence, image_path):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO detections(track_id, timestamp, confidence, image_path)
    VALUES (?, ?, ?, ?)
    """,
    (
        track_id,
        timestamp,
        confidence,
        image_path
    ))

    conn.commit()

    conn.close()

def get_total_detections():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM detections
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total

def get_today_count():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM detections
    WHERE DATE(timestamp)=DATE('now', 'localtime')
    """)

    today = cursor.fetchone()[0]

    conn.close()

    return today

def get_weekly_count():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM detections
    WHERE timestamp >= DATETIME('now', 'localtime', '-7 days')
    """)

    week = cursor.fetchone()[0]

    conn.close()

    return week

def get_latest_detection():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM detections
    ORDER BY timestamp DESC
    LIMIT 1
    """)

    latest = cursor.fetchone()

    conn.close()

    return latest

def get_all_detections():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM detections
    ORDER BY timestamp DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_monthly_count():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM detections
    WHERE timestamp >= DATETIME('now', 'localtime', '-30 days')
    """)

    month = cursor.fetchone()[0]

    conn.close()

    return month

def get_detections_between(start_date, end_date):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM detections
    WHERE DATE(timestamp) BETWEEN DATE(?) AND DATE(?)
    ORDER BY timestamp DESC
    """, (start_date, end_date))

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_daily_statistics():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT DATE(timestamp), COUNT(*)
    FROM detections
    GROUP BY DATE(timestamp)
    ORDER BY DATE(timestamp) DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

def get_daily_detections():

    import sqlite3

    conn = sqlite3.connect("detections.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DATE(timestamp), COUNT(*)
        FROM detections
        GROUP BY DATE(timestamp)
        ORDER BY DATE(timestamp)
    """)

    data = cursor.fetchall()

    conn.close()

    return data

def get_weekly_detections():

    conn = sqlite3.connect("detections.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT strftime('%Y-%W', timestamp), COUNT(*)
        FROM detections
        GROUP BY strftime('%Y-%W', timestamp)
        ORDER BY strftime('%Y-%W', timestamp)
    """)

    data = cursor.fetchall()

    conn.close()

    return data

def get_confidence_distribution():

    conn = sqlite3.connect("detections.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            CASE
                WHEN confidence < 0.70 THEN 'Low'
                WHEN confidence < 0.90 THEN 'Medium'
                ELSE 'High'
            END,
            COUNT(*)
        FROM detections
        GROUP BY 1
    """)

    data = cursor.fetchall()

    conn.close()

    return data



