
from PySide6.QtCore import Slot, QThread, Signal, Qt
from PySide6.QtGui import QPixmap, QImage

from ultralytics import YOLO
import cv2
import pafy
from misc import *

#https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/
class Worker(QThread):
    changePixmap = Signal(QPixmap)
    sendResults = Signal(list)

    def __init__(self, model, source, url, parent=None):
        QThread.__init__(self, parent=parent)
        self.yolo_is_running = True
        self.model = model
        self.source = source
        self.url = url
        self.videoWidth = 640
        self.videoHeight = 480
        
        print("model: ", model, "Sourde: ", source)

    @Slot() 
    def run(self):
    # https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
    # https://docs.ultralytics.com/modes/predict/#streaming-source-for-loop
    # https://pypi.org/project/pafy/

        model = YOLO(self.model)
        source = self.source
        
        if source == "Webcam":
            source = 0 
        if source == "Youtube":
            video = pafy.new(self.url)
            best = video.getbest(preftype="mp4")
            source = best.url

        
        cap = cv2.VideoCapture(source)
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
                

                img = draw_boxes(frame, results[0])

                #https://stackoverflow.com/questions/57204782/show-an-opencv-image-with-pyqt5
                rgbImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)

                p = convertToQtFormat.scaled(self.videoWidth, self.videoHeight, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

                res = results[0]
                class_id = res.boxes.cls.numpy().astype(int)
                confidence = res.boxes.conf.numpy().astype(float)
                class_name = [res.names[x] for x in class_id]
                confidence, class_name
                sum_output = list(zip(class_name, confidence))
                self.sendResults.emit(sum_output)
                
                #to exit with q-key or Stop button
                if cv2.waitKey(25) & 0xFF == ord('q'): break
                if self.yolo_is_running == False: break
            else: break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

        img = QPixmap("./kampus.jpg")
        p = img.scaled(self.videoWidth, self.videoHeight, Qt.KeepAspectRatio)
        self.changePixmap.emit(p)
        self.yolo_is_running = True
    
    @Slot()
    def stop(self):
        self.yolo_is_running = False
        self.wait()

    @Slot()
    def change_video_size(self, width, height):
        self.videoHeight = width
        self.videoWidth = height
        print(width, height)
