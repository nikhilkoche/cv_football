from ultralytics import YOLO

model = YOLO('yolov8s')
results = model.predict('input/08fd33_4.mp4',save=True)
print(results[0])
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
for box in results[0].boxes:
    print(box)