#https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/

import sys
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication, QMdiSubWindow, QDialog
from PySide6.QtCore import QRunnable, Slot, QThreadPool, QThread, Signal, Qt
from PySide6.QtGui import QPixmap, QImage

from mainWindow import Ui_MainWindow
from controls import Ui_controls
from picture_window import Ui_pictureFrame
from init_dialog import Ui_Dialog
from misc import *

class Controls(QWidget, Ui_controls):

    def __init__(self, parent = None):
        super(Controls, self).__init__()
        self.setupUi(self)
        

class Picture(QWidget, Ui_pictureFrame):

    def __init__(self, parent = None):
        super(Picture, self).__init__()
        self.setupUi(self)

class Setup(QDialog, Ui_Dialog):

    def __init__(self, parent= None):
        super(Setup, self).__init__()
        self.setupUi(self)

        

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        #self.showMaximized()

        self.setup = Setup(self)
        models = find_models()
        for x in models:
            self.setup.modelListBox.addItem(x)
        self.setup.exec()

        self.controls = Controls(self)
        self.dockControls.setWidget(self.controls) 

        self.picture = Picture(self)
        self.mdiArea.addSubWindow(self.picture)
        self.picture.showMaximized()


        

        


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()