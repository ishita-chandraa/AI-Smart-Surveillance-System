from ultralytics import YOLO
import cv2
from datetime import datetime

model = YOLO("yolov8n.pt")


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
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"evidence/person_{track_id}_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"📸 Evidence saved: {filename}")
            alerted_ids.add(track_id)

    annotated_frame = results[0].plot()

    # Show the annotated frame
    cv2.imshow("Object Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

