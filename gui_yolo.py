# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(980, 758)
        font = QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.Finland))
        self.actionMain_menu = QAction(MainWindow)
        self.actionMain_menu.setObjectName(u"actionMain_menu")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.modelList = QComboBox(self.centralwidget)
        self.modelList.setObjectName(u"modelList")
        self.modelList.setGeometry(QRect(20, 20, 171, 31))
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(230, 20, 151, 51))
        font1 = QFont()
        font1.setPointSize(16)
        self.startButton.setFont(font1)
        self.stopButton = QPushButton(self.centralwidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(440, 20, 151, 51))
        self.stopButton.setFont(font1)
        self.pictureArea = QLabel(self.centralwidget)
        self.pictureArea.setObjectName(u"pictureArea")
        self.pictureArea.setGeometry(QRect(10, 80, 721, 621))
        self.pictureArea.setCursor(QCursor(Qt.ForbiddenCursor))
        self.pictureArea.setFrameShape(QFrame.Panel)
        self.pictureArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.objectsFound = QLabel(self.centralwidget)
        self.objectsFound.setObjectName(u"objectsFound")
        self.objectsFound.setGeometry(QRect(740, 80, 221, 351))
        self.objectsFound.setCursor(QCursor(Qt.ForbiddenCursor))
        self.objectsFound.setFrameShape(QFrame.Panel)
        self.objectsFound.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 980, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionMain_menu)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"YOLO webcam view", None))
        self.actionMain_menu.setText(QCoreApplication.translate("MainWindow", u"Main menu", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit Program", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pictureArea.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.objectsFound.setText(QCoreApplication.translate("MainWindow", u"Objects", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

