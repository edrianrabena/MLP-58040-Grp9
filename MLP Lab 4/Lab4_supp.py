import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2

def sobelwindow(image_color):
    image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    sobelxy = cv2.Sobel(image_gray, -1, dx=0, dy=1, ksize=1)
    return sobelxy

def cannywindow(image_color):
    image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(image_gray, 30, 80)
    return canny

def laplacianwindow(image_color):
    image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(image_gray, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))
    return laplacian

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Live Edge Detection (Sobel)', sobelwindow(frame))
    cv2.imshow('Live Edge Detection (Canny)', cannywindow(frame))
    cv2.imshow('Live Edge Detection (Laplacian)', laplacianwindow(frame))
    cv2.imshow('Webcam Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' key
        break
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

cap.release()
cv2.destroyAllWindows()