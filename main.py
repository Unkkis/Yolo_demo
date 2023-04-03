#https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/

import sys
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QRunnable, Slot, QThreadPool, QThread, Signal
from PySide6.QtGui import QPixmap, QImage

from misc import *

class MainWindow(QMainWindow):
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
 


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()