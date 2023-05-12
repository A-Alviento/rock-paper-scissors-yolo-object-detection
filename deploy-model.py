from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

model = YOLO(r"C:\Users\Adrian\yolo-test-env-1\runs\detect\train\weights\best.pt")
model.predict(source="0", show=True, conf=0.5)