from ultralytics import YOLO
import cv2
from datetime import datetime
from database import initialize_database, insert_detection

# Create the database/table if it doesn't exist
initialize_database()

# -----------------------------
# Load the pretrained YOLOv8 model
# -----------------------------
model = YOLO("yolov8n.pt")

# -----------------------------
# Open the default webcam
# 0 = Laptop webcam
# -----------------------------
cap = cv2.VideoCapture(0)


alerted_ids = set()
while True:

    # Capture one frame from the webcam
    success, frame = cap.read()

    # Stop if the webcam fails
    if not success:
        print("Failed to capture frame.")
        break

    results = model.track(frame, persist=True)

    for box in results[0].boxes:
        if box.id is None:
         continue
        # Get the class ID
        cls = int(box.cls[0])
        name = model.names[cls]
        confidence = float(box.conf[0])
        track_id = int(box.id[0])
           
        if name == "person" and confidence > 0.80:
          print(f"Person ID: {track_id} | Confidence: {confidence:.2f}")
          if track_id not in alerted_ids:

            print(f"🚨 New Person Detected! ID = {track_id}")
            now = datetime.now()
            db_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            file_timestamp = now.strftime("%Y%m%d_%H%M%S")
            filename = f"evidence/person_{track_id}_{file_timestamp}.jpg"
            saved = cv2.imwrite(filename, frame)

            if saved:
             insert_detection(
             track_id,
             db_timestamp,
             confidence,
             filename
            )
             print(f"📸 Evidence saved: {filename}")

            else:
             print("❌ Failed to save evidence image.")

            alerted_ids.add(track_id)

    annotated_frame = results[0].plot()

    # Show the annotated frame
    cv2.imshow("Object Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
