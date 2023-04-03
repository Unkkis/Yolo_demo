# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controls.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_controls(object):
    def setupUi(self, controls):
        if not controls.objectName():
            controls.setObjectName(u"controls")
        controls.resize(200, 250)
        controls.setMinimumSize(QSize(200, 250))
        self.label = QLabel(controls)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 121, 20))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.modelListBox = QComboBox(controls)
        self.modelListBox.setObjectName(u"modelListBox")
        self.modelListBox.setGeometry(QRect(20, 50, 141, 20))
        self.stopButton = QPushButton(controls)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(20, 160, 141, 51))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.stopButton.setFont(font1)
        self.startButton = QPushButton(controls)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(20, 100, 141, 51))
        self.startButton.setFont(font1)
        self.frame = QFrame(controls)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 200, 251))
        self.frame.setMinimumSize(QSize(200, 250))
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.raise_()
        self.label.raise_()
        self.modelListBox.raise_()
        self.stopButton.raise_()
        self.startButton.raise_()

        self.retranslateUi(controls)

        QMetaObject.connectSlotsByName(controls)
    # setupUi

    def retranslateUi(self, controls):
        controls.setWindowTitle(QCoreApplication.translate("controls", u"Controls", None))
        self.label.setText(QCoreApplication.translate("controls", u"Choose Model", None))
        self.stopButton.setText(QCoreApplication.translate("controls", u"Stop", None))
        self.startButton.setText(QCoreApplication.translate("controls", u"Start", None))
    # retranslateUi

