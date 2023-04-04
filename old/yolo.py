from ultralytics import YOLO
import cv2
from misc import *

#Choose the used YOLO model first.
model_name = "yolov8s.pt"

#Choose above what conficende score the boxes are drawn
confidence_score = 0.5 

# This script is for capturing video and running YOLO
def run_yolo(model):


    model = YOLO(model)

    #Choose capture device. 0 is the default for webcam.
    cap = cv2.VideoCapture("test50.mp4")
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


if __name__ == "__main__":
    run_yolo(model_name)
