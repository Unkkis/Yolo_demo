#https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/

import sys
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QRunnable, Slot, QThreadPool, QThread, Signal
from PySide6.QtGui import QPixmap, QImage

from gui_yolo import Ui_MainWindow
from misc import *
from yolo_worker import Worker

'''
#https://www.pythonguis.com/tutorials/multithreading-pyside6-applications-qthreadpool/
class Worker(QThread):
    changePixmap = Signal(QPixmap)

    def __init__(self, model, parent=None):
        QThread.__init__(self, parent=parent)
        self.yolo_is_running = True
        self.model = model
        print(self.model)

    @Slot() 
    def run(self):
    # https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
    # https://docs.ultralytics.com/usage/python/

        model = YOLO(self.model)

        #Choose capture device. 0 is the default for webcam.
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

                img = draw_boxes(frame, results[0])

                rgbImage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format.Format_RGB888)
                convertToQtFormat = QPixmap.fromImage(convertToQtFormat)

                p = convertToQtFormat.scaled(640, 480)
                self.changePixmap.emit(p)
                
                #to exit with q-key or Stop button
                if cv2.waitKey(25) & 0xFF == ord('q'): break
                if self.yolo_is_running == False: break
            else: break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

        img = QPixmap("./image.jpeg")
        p = img.scaled(640, 480)
        self.changePixmap.emit(p)
        self.yolo_is_running = True
    
    @Slot()
    def stop(self):
        print("täällä threadissa stoppia painettu")
        self.yolo_is_running = False
        self.wait()
'''

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.stopButton.setEnabled(False)
        self.startButton.clicked.connect(self.start_button_clicked)
        self.stopButton.clicked.connect(self.stop_button_clicked)

        models = find_models()
        for x in models:
            self.modelList.addItem(x)
        #self.yolo_model = "yolov8s.pt"

        self.yolo_worker = Worker(self.modelList.currentText())
        self.yolo_worker.changePixmap.connect(self.pictureArea.setPixmap)

    def start_button_clicked(self):
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        self.yolo_worker.start()

    def stop_button_clicked(self):
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.yolo_worker.stop()
        self.yolo_worker.quit()
 


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()