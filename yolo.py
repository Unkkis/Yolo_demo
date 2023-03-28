# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
# https://docs.ultralytics.com/usage/python/

from ultralytics import YOLO
import cv2
from misc import *

model = YOLO("yolov8s.pt")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is not read correctly
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # if frame is read correctly
    if ret :
        results = model.predict(frame)

        cv2.imshow('Capture from webcam', draw_boxes(frame, results[0]))

        #to exit with q-key
        if cv2.waitKey(25) & 0xFF == ord('q'): break
    else: break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
