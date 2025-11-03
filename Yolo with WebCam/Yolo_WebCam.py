# video_detect.py
from ultralytics import YOLO
import cv2
import cvzone
import math
import os

# --- Settings ---
# Choose ONE of these:
VIDEO_SOURCE = "../videos/businessman.mp4"   # set to a file path for video
# VIDEO_SOURCE = 0                     # or use 0 for your webcam

WEIGHTS_PATH = "weights/yolov8n.pt"    # adjust to your weights file
CONF_THRES = 0.25                      # optional confidence filter

# --- Load model ---
model = YOLO(WEIGHTS_PATH)
names = model.names  # class name list from the model

# --- Video capture ---
cap = cv2.VideoCapture(VIDEO_SOURCE)
if not cap.isOpened():
    raise RuntimeError(f"Could not open video source: {VIDEO_SOURCE}")

# If you're using a webcam, you can set size:
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    success, frame = cap.read()
    if not success:
        # If file video ends, break. If webcam fails, also break.
        break

    # Run inference (stream=True yields generator over results)
    results = model(frame, stream=True)

    for r in results:
        for box in r.boxes:
            # Confidence
            conf = float(box.conf[0])
            if conf < CONF_THRES:
                continue

            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            # Draw fancy rectangle
            cvzone.cornerRect(frame, (x1, y1, w, h), l=12, t=3)

            # Class label
            cls_id = int(box.cls[0])
            label = f"{names[cls_id]} {conf:.2f}"
            cvzone.putTextRect(
                frame,
                label,
                (max(0, x1), max(20, y1 - 10)),
                scale=1,
                thickness=1,
                offset=3
            )

    cv2.imshow("YOLOv8 - Video", frame)
    key = cv2.waitKey(1) & 0xFF
    if key in (27, ord('q')):  # ESC or q to quit
        break

cap.release()
cv2.destroyAllWindows()
