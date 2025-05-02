from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.predict("media/Cat.jpg", save=True)

model.predict(
    source="media/Cat.jpg",   
    save=True,
    project="output",       
    name="cat_run",           
    exist_ok=True             
)

