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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_controls(object):
    def setupUi(self, controls):
        if not controls.objectName():
            controls.setObjectName(u"controls")
        controls.resize(200, 379)
        controls.setMinimumSize(QSize(200, 250))
        self.widget = QWidget(controls)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 171, 111))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.formLayout = QFormLayout(self.widget1)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.chosenModel = QLabel(self.widget1)
        self.chosenModel.setObjectName(u"chosenModel")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.chosenModel)

        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.chosenSource = QLabel(self.widget1)
        self.chosenSource.setObjectName(u"chosenSource")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.chosenSource)

        self.youtubeLabel = QLabel(self.widget1)
        self.youtubeLabel.setObjectName(u"youtubeLabel")
        self.youtubeLabel.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.youtubeLabel)

        self.youtubeUrl = QLabel(self.widget1)
        self.youtubeUrl.setObjectName(u"youtubeUrl")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.youtubeUrl)


        self.verticalLayout_2.addWidget(self.widget1)

        self.widget2 = QWidget(controls)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(10, 130, 171, 231))
        self.verticalLayout = QVBoxLayout(self.widget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.startButton = QPushButton(self.widget2)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setFont(font)

        self.verticalLayout.addWidget(self.startButton)

        self.stopButton = QPushButton(self.widget2)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setFont(font)

        self.verticalLayout.addWidget(self.stopButton)

        self.newButton = QPushButton(self.widget2)
        self.newButton.setObjectName(u"newButton")
        self.newButton.setFont(font)

        self.verticalLayout.addWidget(self.newButton)


        self.retranslateUi(controls)

        QMetaObject.connectSlotsByName(controls)
    # setupUi

    def retranslateUi(self, controls):
        controls.setWindowTitle(QCoreApplication.translate("controls", u"Controls", None))
        self.label.setText(QCoreApplication.translate("controls", u"Controls", None))
        self.label_2.setText(QCoreApplication.translate("controls", u"Model:", None))
        self.chosenModel.setText(QCoreApplication.translate("controls", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("controls", u"Source", None))
        self.chosenSource.setText(QCoreApplication.translate("controls", u"TextLabel", None))
        self.youtubeLabel.setText(QCoreApplication.translate("controls", u"TextLabel", None))
        self.youtubeUrl.setText(QCoreApplication.translate("controls", u"TextLabel", None))
        self.startButton.setText(QCoreApplication.translate("controls", u"Start", None))
        self.stopButton.setText(QCoreApplication.translate("controls", u"Stop", None))
        self.newButton.setText(QCoreApplication.translate("controls", u"New", None))
    # retranslateUi

