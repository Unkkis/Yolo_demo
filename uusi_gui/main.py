#https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/

import sys
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication, QMdiSubWindow, QDialog
from PySide6.QtCore import QRunnable, Slot, QThreadPool, QThread, Signal, Qt
from PySide6.QtGui import QPixmap, QImage

from mainWindow import Ui_MainWindow
from controls import Ui_controls
from picture_window import Ui_pictureFrame
from init_dialog import Ui_Dialog
from yolo_worker import Worker
from misc import *

class Controls(QWidget, Ui_controls):

    def __init__(self, parent = None):
        super(Controls, self).__init__()
        self.setupUi(self)

        self.stopButton.setEnabled(False)
        

class Picture(QWidget, Ui_pictureFrame):

    def __init__(self, parent = None):
        super(Picture, self).__init__()
        self.setupUi(self)

class Setup(QDialog, Ui_Dialog):

    def __init__(self, parent= None):
        super(Setup, self).__init__()
        self.setupUi(self)
        self.label_youtube.setVisible(False)
        self.youtubeURL.setEnabled(False)

        models = find_files("pt")
        for x in models:
            self.modelListBox.addItem(x)

        self.sourceListBox.addItem("Webcam")
        self.sourceListBox.addItem("Youtube")
        sources = find_files("mp4")
        for x in sources:
            self.sourceListBox.addItem(x)

        self.sourceListBox.currentTextChanged.connect(self.checkYoutube)
        
    def checkYoutube(self):

        if self.sourceListBox.currentText == "Youtube":
            self.youtubeURL.setEnabled(True)
            self.label_youtube.setVisible(True)
    

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #self.showMaximized()

        self.setup = Setup(self)
        self.setup.exec()

        self.controls = Controls(self)
        self.dockControls.setWidget(self.controls)
        self.controls.startButton.setEnabled(False)
        
        self.picture = Picture(self)
        self.mdiArea.addSubWindow(self.picture)
        self.picture.showMaximized()

        self.dockControls.toggleViewAction(self.actionShow_Controls)

        

        #self.menuView.addAction(self.dockControls.toggleViewAction())

        #self.model = self.setup.modelListBox.currentText()
        #self.controls.chosenModel.setText(self.model)
        #self.source = self.setup.sourceListBox.currentText()
        #self.controls.chosenSource.setText(self.source)

        self.setup.buttonBox.accepted.connect(self.setOptions)
        
        self.yolo_worker = None

        img = QPixmap("./kampus.jpg")
        img = img.scaled(640, 480, Qt.KeepAspectRatio)
        self.picture.pictureFrame_2.setPixmap(img)

    
        self.controls.startButton.clicked.connect(self.start_button_clicked)
        self.controls.stopButton.clicked.connect(self.stop_button_clicked)
        self.controls.newButton.clicked.connect(lambda: self.setup.exec())

        
    def setOptions(self):
        self.model = self.setup.modelListBox.currentText()
        self.controls.chosenModel.setText(self.model)
        self.source = self.setup.sourceListBox.currentText()
        self.controls.chosenSource.setText(self.source)
        self.controls.startButton.setEnabled(True)
        

    def start_button_clicked(self):
        self.controls.startButton.setEnabled(False)
        self.controls.stopButton.setEnabled(True)
        self.controls.newButton.setEnabled(False)
        self.yolo_worker = Worker(self.model, self.source)
        self.yolo_worker.changePixmap.connect(self.picture.pictureFrame_2.setPixmap)
        self.yolo_worker.start()

    def stop_button_clicked(self):
        self.controls.startButton.setEnabled(True)
        self.controls.stopButton.setEnabled(False)
        self.controls.newButton.setEnabled(True)
        self.yolo_worker.stop()
        self.yolo_worker.quit()
        self.yolo_worker.terminate()

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()