from ultralytics import YOLO
import cv2

# loads the trained model, selecting the best model trained 
model = YOLO("./runs/detect/train/weights/best.pt")

# predict on source 0 (webcam) with a confidence threshold of 50%
# device="mps" is for apple silicon to utilize the gpu; ignore if not needed
model.predict(source="0", show=True, conf=0.5, device="mps")