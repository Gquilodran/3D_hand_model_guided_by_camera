from ultralytics import YOLO
import cv2

def init_Yolo():
    model = YOLO("yolov8n.pt")
    return model

def deteccion(model, frame):
    results = model(frame)
    boxes = results[0].boxes
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        x1=int(x1)
        y1=int(y1)
        x2=int(x2)
        y2=int(y2)
        ncl = box.cls[0] ##numero de la clase
        names = results[0].names ##dicsionario de objetos detectados
        conf = box.conf[0]
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
        label = f"{model.names[int(ncl)]},{conf:.2f}"
        cv2.putText(
            frame,
            label,
            (x1,y1-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0,255,0),
            2
        )
    return frame