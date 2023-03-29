from PyQt6 import QtCore, QtGui, QtWidgets
from ultralytics import YOLO
from misc import *
from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QWidget

class Video(QThread):
    
    def run(self):
    # https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
    # https://docs.ultralytics.com/usage/python/

        #model_name = self.modelList.currentText()
        model_name =  "yolov8s.pt"
        
        model = YOLO(model_name)
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

                cv2.imshow('Capture from webcam', draw_boxes(frame, results[0]))

                #to exit with q-key
                if cv2.waitKey(25) & 0xFF == ord('q'): break
            else: break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 758)
        MainWindow.move(200, 50)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.Finland))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Model list
        self.modelList = QtWidgets.QComboBox(parent=self.centralwidget)
        self.modelList.setGeometry(QtCore.QRect(20, 20, 171, 31))
        self.modelList.setObjectName("modelList")
        models = find_models()
        for x in models:
            self.modelList.addItem(x)

        #Start Button
        self.startButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(230, 20, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")

        #Stop Button
        self.stopButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(440, 20, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.stopButton.setEnabled(False)

        #Area for webcam picture
        self.pictureArea = QtWidgets.QLabel(parent=self.centralwidget)
        self.pictureArea.setGeometry(QtCore.QRect(10, 80, 721, 621))
        self.pictureArea.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.pictureArea.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.pictureArea.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.pictureArea.setObjectName("pictureArea")
        self.pictureArea.setScaledContents(True)

        #Area for object list
        self.objectsFound = QtWidgets.QLabel(parent=self.centralwidget)
        self.objectsFound.setGeometry(QtCore.QRect(740, 80, 221, 351))
        self.objectsFound.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.objectsFound.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.objectsFound.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.objectsFound.setObjectName("objectsFound")

        #Manubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        #Statusbar
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMain_menu = QtGui.QAction(parent=MainWindow)
        self.actionMain_menu.setObjectName("actionMain_menu")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.menuFile.addAction(self.actionMain_menu)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

        self.startButton.clicked.connect(self.startPressed)
        self.stopButton.clicked.connect(self.stopPressed)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YOLO webcam view"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.pictureArea.setText(_translate("MainWindow", "Camera"))
        self.objectsFound.setText(_translate("MainWindow", "Objects"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionMain_menu.setText(_translate("MainWindow", "Main menu"))
        self.actionExit.setText(_translate("MainWindow", "Exit Program"))


    def startPressed(self):
        self.stopButton.setEnabled(True)
        video = Video(self)
        video.start()
        self.startButton.setEnabled(False)
            
    def stopPressed(self):
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
