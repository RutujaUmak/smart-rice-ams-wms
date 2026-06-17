]from ultralytics import YOLO

model = YOLO("yolo11s.pt")

results = model.train(
    data="gunny bags.v1i.coco/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8
)

print("Training completed!")