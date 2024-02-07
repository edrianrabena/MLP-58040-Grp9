import numpy as np
import cv2 as cv

def capture():
    cap = cv.VideoCapture(0)
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter('supp.mp4', fourcc, 20.0, (640,  480))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows()

def play():
    cap = cv.VideoCapture(r'supp.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv.imshow('frame', frame)
        if cv.waitKey(15) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

while True:
    print(
        "Type '1' if you wish to record.\n"
        "Type '2' if you wish to play the recorded video.\n"
        "Type '3' if you wish to close the window.\n"
    )

    userInput = input("Enter your choice: ")

    if userInput == "1":
        capture()
    elif userInput == "2":
        play()
    elif userInput == "3":
        break
    else:
        print("Please enter a valid input.\n")