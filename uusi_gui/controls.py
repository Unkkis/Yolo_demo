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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_controls(object):
    def setupUi(self, controls):
        if not controls.objectName():
            controls.setObjectName(u"controls")
        controls.resize(200, 304)
        controls.setMinimumSize(QSize(200, 250))
        self.stopButton = QPushButton(controls)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setGeometry(QRect(20, 160, 141, 51))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.stopButton.setFont(font)
        self.startButton = QPushButton(controls)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(20, 100, 141, 51))
        self.startButton.setFont(font)
        self.frame = QFrame(controls)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 200, 301))
        self.frame.setMinimumSize(QSize(200, 250))
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(3)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 50, 141, 40))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.chosenModel = QLabel(self.layoutWidget)
        self.chosenModel.setObjectName(u"chosenModel")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.chosenModel)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.chosenSource = QLabel(self.layoutWidget)
        self.chosenSource.setObjectName(u"chosenSource")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.chosenSource)

        self.newButton = QPushButton(self.frame)
        self.newButton.setObjectName(u"newButton")
        self.newButton.setGeometry(QRect(20, 230, 141, 51))
        self.newButton.setFont(font)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 121, 20))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.frame.raise_()
        self.stopButton.raise_()
        self.startButton.raise_()

        self.retranslateUi(controls)

        QMetaObject.connectSlotsByName(controls)
    # setupUi

    def retranslateUi(self, controls):
        controls.setWindowTitle(QCoreApplication.translate("controls", u"Controls", None))
        self.stopButton.setText(QCoreApplication.translate("controls", u"Stop", None))
        self.startButton.setText(QCoreApplication.translate("controls", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("controls", u"Model:", None))
        self.chosenModel.setText(QCoreApplication.translate("controls", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("controls", u"Source", None))
        self.chosenSource.setText(QCoreApplication.translate("controls", u"TextLabel", None))
        self.newButton.setText(QCoreApplication.translate("controls", u"New", None))
        self.label.setText(QCoreApplication.translate("controls", u"Controls", None))
    # retranslateUi

