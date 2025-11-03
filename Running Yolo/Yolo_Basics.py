# image_detect.py
from ultralytics import YOLO
import cv2

WEIGHTS_PATH = "weights/yolov8m.pt"  # your requested weight
IMAGE_PATH = "Images/img1.png"       # path to your image

model = YOLO(WEIGHTS_PATH)
results = model("./Images/img3.png")  # you can also pass a loaded image (cv2.imread)

# Render predictions onto the image and show
rendered = results[0].plot()
cv2.imshow("YOLO Result", rendered)
cv2.waitKey(0)
cv2.destroyAllWindows()
