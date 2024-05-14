import torch
import cv2
import numpy as np
import pathlib
import serial
import time

pathlib.PosixPath = pathlib.WindowsPath

yolov5_dir = r'C:\Users\raben\yolov5'
weights_path = r'C:\Users\raben\yolov5\best.pt'

model = torch.hub.load(str(yolov5_dir), 'custom', path=str(weights_path), source='local')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

arduino_port = 'COM3'
arduino_baudrate = 9600
arduino = serial.Serial(arduino_port, arduino_baudrate)
time.sleep(2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    class_names = results.names
    boxes = results.xyxy[0].cpu().numpy()

    Inhaler = False
    Jug = False
    Earpods = False

    for box in boxes:
        xmin, ymin, xmax, ymax, confidence, label = box
        label = int(label)

        if label == 1:
            Inhaler = True
            color = (0, 255, 0)
        elif label == 0:
            Jug = True
            color = (255, 0, 0)
        elif label == 2:
            Earpods = True
            color = (0, 0, 255)
        else:
            continue

        cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), color, 2)
        cv2.putText(frame, class_names[label], (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    if Earpods:
        arduino.write(b'A')
    else:
        arduino.write(b'D')

    if Inhaler:
        arduino.write(b'B')
    else:
        arduino.write(b'D')

    if Jug:
        arduino.write(b'C')
    else:
        arduino.write(b'D')

    cv2.imshow('YOLOv5 Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
