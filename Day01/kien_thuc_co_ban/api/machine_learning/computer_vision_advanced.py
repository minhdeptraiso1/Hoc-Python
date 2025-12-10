"""
===============================================================================
                       COMPUTER VISION NÂNG CAO
Gồm:
✔ YOLO Object Detection (Ultralytics)
✔ Faster R-CNN (TorchVision)
Giúp em học về nhận diện vật thể (Object Detection) — kỹ năng cực quan trọng trong thị giác máy tính.
===============================================================================
"""

# ============================ YOLO ===============================

print("\n===== YOLO OBJECT DETECTION =====")

from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Predict on image
results = model.predict("image.jpg")  # cần sẵn ảnh
print("YOLO prediction complete!")


# ============================ FASTER R-CNN =========================

print("\n===== FASTER R-CNN =====")

import torchvision
import torch

# Load pre-trained Faster R-CNN
faster = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights="DEFAULT")

# Dummy input
image = torch.randn(1, 3, 480, 640)
output = faster(image)

print("Faster R-CNN prediction:", output[0]["boxes"][:2])
