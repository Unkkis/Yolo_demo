#https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/
#https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QMainWindow.html
#https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/
#https://doc.qt.io/qtforpython/PySide6/QtGui/QDesktopServices.html
#https://doc.qt.io/qt-6/widget-classes.html#basic-widget-classes

import sys
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QDialog
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap, QResizeEvent, QDesktopServices, QIcon

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
        self.label_youtube.setEnabled(False)
        self.youtubeURL.setEnabled(False)

        #Fetch available models
        models = find_files("pt")
        for x in models:
            self.modelListBox.addItem(x)

        #Add sources and fetch available videos
        self.sourceListBox.addItem("Webcam")
        self.sourceListBox.addItem("Youtube")
        videoFormats = [
            "asf",
            "avi",
            "gif",
            "m4v",
            "mkv",
            "mov",
            "mp4",
            "mpeg",
            "mpg",
            "ts",
            "wmv",
            "webm"
        ]
        for format in videoFormats:
            sources = find_files(format)
            for video in sources:
                self.sourceListBox.addItem(video)

        self.confidenceLabel.setText(str(self.confidenceSlider.value()) + "%")
        self.confidenceSlider.valueChanged.connect(self.slider_moved)

        self.sourceListBox.currentTextChanged.connect(self.checkYoutube)

        self.whatIsYoloButton.clicked.connect(self.yolo_button_clicked)
        self.pushButton.clicked.connect(self.documentation_button_clicked)
    
    def slider_moved(self):
        print(self.confidenceSlider.value())
        self.confidenceLabel.setText(str(self.confidenceSlider.value()) + "%")
    
    def yolo_button_clicked(self):
        QDesktopServices.openUrl("https://en.wikipedia.org/wiki/Object_detection")
    def documentation_button_clicked(self):
        QDesktopServices.openUrl("https://docs.ultralytics.com/")
        
    def checkYoutube(self):
        if self.sourceListBox.currentText() == "Youtube":
            self.youtubeURL.setEnabled(True)
            self.label_youtube.setEnabled(True)
        else:
            self.youtubeURL.setEnabled(False)
            self.label_youtube.setEnabled(False)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.showMaximized()

        #Adding controls widget
        self.controls = Controls(self)
        self.dockControls.setWidget(self.controls)
        self.controls.startButton.setEnabled(False)
        
        #Adding picture area
        self.picture = Picture(self)
        self.mdiArea.addSubWindow(self.picture)
        self.picture.showMaximized()

        #Adding button to toggle control widget
        self.controls_button = self.dockControls.toggleViewAction()
        self.controls_button.setText("Show controls")
        self.menuView.addAction(self.controls_button)

        #To Close program from File -menu
        self.actionExit.triggered.connect(lambda: self.close()) 

        #Preparing for extra thread for video    
        self.yolo_worker = None

        #Setting picture to picturearea
        self.videoHeight = 640
        self.videoWidth = 480
        self.img = QPixmap("./logo.jpg")
        self.img = self.img.scaled(self.videoHeight,self.videoWidth, Qt.KeepAspectRatio)
        self.picture.videoFrame.setPixmap(self.img)

        #Showing initial setup dialog
        self.setup = Setup(self)
        self.setup.buttonBox.accepted.connect(self.setOptions)
        self.setup.exec()
    
        self.controls.startButton.clicked.connect(self.start_button_clicked)
        self.controls.stopButton.clicked.connect(self.stop_button_clicked)
        self.controls.newButton.clicked.connect(lambda: self.setup.exec())
        
    def setOptions(self):
        self.model = self.setup.modelListBox.currentText()
        self.controls.chosenModel.setText(self.model)
        self.source = self.setup.sourceListBox.currentText()
        self.controls.chosenSource.setText(self.source)
        if self.setup.youtubeURL.isEnabled():
            self.youtubeUrl = self.setup.youtubeURL.text()
            self.controls.youtubeUrl.setText(self.youtubeUrl)
            self.controls.youtubeLabel.setVisible(True)
        else:
            self.youtubeUrl = ""
            self.controls.youtubeUrl.setText(self.youtubeUrl)
            self.controls.youtubeLabel.setVisible(False)
       
        self.controls.startButton.setEnabled(True)        
        
        self.picture.videoFrame.resizeEvent = self.video_resize

        self.confidenceTreshold = self.setup.confidenceSlider.value()

        self.videoHeight = self.picture.videoFrame.height()
        self.videoWidth = self.picture.videoFrame.width()

    def video_resize(self, resizeEvent:QResizeEvent):
        self.videoWidth = self.picture.videoFrame.width()
        self.videoHeight = self.picture.videoFrame.height()
        if self.yolo_worker != None:
            self.yolo_worker.change_video_size(self.videoWidth, self.videoHeight)
              
        
    @Slot(list)
    def updateResults(self, result_list):
        
        text = ""
        if result_list[0] == "ERROR":
            text = f"{result_list[0]}: {result_list[1]}"
        else:
            for x in result_list:
                class_name, confidence = x               
                confidence = "{0:.0%}".format(confidence)
                text = text + f"{confidence} {class_name}" + "\n"

        self.picture.resultsFrame.setText(text)
            
            

    def start_button_clicked(self):
        self.controls.startButton.setEnabled(False)
        self.controls.stopButton.setEnabled(True)
        self.controls.newButton.setEnabled(False)
        self.yolo_worker = Worker(self.model, self.confidenceTreshold, self.source, self.youtubeUrl, self.videoWidth, self.videoHeight)
        self.yolo_worker.changePixmap.connect(self.picture.videoFrame.setPixmap)
        self.yolo_worker.sendResults.connect(self.updateResults)
        self.yolo_worker.start()

    def stop_button_clicked(self):
        self.controls.startButton.setEnabled(True)
        self.controls.stopButton.setEnabled(False)
        self.controls.newButton.setEnabled(True)
        self.picture.resultsFrame.setText("Results")
        self.yolo_worker.stop()
        self.yolo_worker.quit()
        self.yolo_worker.terminate()

    

app = QApplication(sys.argv)
app.setWindowIcon(QIcon('logo.ico'))

window = MainWindow()
window.show()
app.exec()