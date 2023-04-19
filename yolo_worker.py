
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

    def __init__(self, model, confidence, source, url, width, height, YOLO_plotting, parent=None):
        QThread.__init__(self, parent=parent)
        self.yolo_is_running = True
        self.model = model
        self.confidenceScore = confidence/100
        self.source = source
        self.url = url
        self.videoWidth = width
        self.videoHeight = height
        self.YOLO_plotting = YOLO_plotting
                
        print("model: ", model, "Confidence: ", self.confidenceScore, "Source: ", source)

    @Slot() 
    def run(self):
    # https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
    # https://docs.ultralytics.com/modes/predict/#streaming-source-for-loop
    # https://pypi.org/project/pafy/
    # https://stackoverflow.com/questions/43032163/how-to-read-youtube-live-stream-using-opencv-python

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
            sum_output = ["ERROR", "Cannot open camera"]
            self.sendResults.emit(sum_output)
            cap.release()
            cv2.destroyAllWindows()

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # if frame is not read correctly
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                sum_output = ["ERROR", "Can't receive frame (stream end?). Exiting ..."]
                self.sendResults.emit(sum_output)
                cap.release()
                cv2.destroyAllWindows()
                break
            
            # if frame is read correctly
            if ret :
                results = model(frame, conf=self.confidenceScore)
                              
                # Visualize the results on the frame
                if self.YOLO_plotting == True:
                    # multicolor boxes
                    annotated_frame = results[0].plot()
                else: 
                    # red and green boxes
                    img = draw_boxes(frame, results[0])


                #https://stackoverflow.com/questions/57204782/show-an-opencv-image-with-pyqt5
                
                if self.YOLO_plotting == True:
                    rgbImage = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
                else: 
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

        #https://pythonbasics.org/pyqt-qpixmap/
        img = QPixmap("./logo.jpg")
        p = img.scaled(640, 480, Qt.KeepAspectRatio)
        self.changePixmap.emit(p)
        self.yolo_is_running = True
    
    @Slot()
    def stop(self):
        self.yolo_is_running = False
        self.wait()

    #https://stackoverflow.com/questions/71234281/opencv-video-feed-automatic-resizing-with-pyqt5
    #https://stackoverflow.com/questions/74095602/how-to-adjust-video-to-widget-size-in-qt-python
    #https://forum.qt.io/topic/110955/layout-signal-when-resized/3
    @Slot()
    def change_video_size(self, width, height):
        self.videoHeight = height
        self.videoWidth = width
