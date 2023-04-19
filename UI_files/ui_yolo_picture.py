# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yolo_picture.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_pictureFrame(object):
    def setupUi(self, pictureFrame):
        if not pictureFrame.objectName():
            pictureFrame.setObjectName(u"pictureFrame")
        pictureFrame.resize(914, 607)
        self.horizontalLayout = QHBoxLayout(pictureFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.videoFrame = QLabel(pictureFrame)
        self.videoFrame.setObjectName(u"videoFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoFrame.sizePolicy().hasHeightForWidth())
        self.videoFrame.setSizePolicy(sizePolicy)
        self.videoFrame.setMinimumSize(QSize(690, 480))
        self.videoFrame.setBaseSize(QSize(690, 480))
        self.videoFrame.setFrameShape(QFrame.NoFrame)
        self.videoFrame.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.videoFrame)

        self.resultsFrame = QLabel(pictureFrame)
        self.resultsFrame.setObjectName(u"resultsFrame")
        self.resultsFrame.setEnabled(True)
        self.resultsFrame.setMinimumSize(QSize(200, 0))
        self.resultsFrame.setBaseSize(QSize(200, 0))
        font = QFont()
        font.setPointSize(16)
        self.resultsFrame.setFont(font)
        self.resultsFrame.setFrameShape(QFrame.Box)
        self.resultsFrame.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.resultsFrame)


        self.retranslateUi(pictureFrame)

        QMetaObject.connectSlotsByName(pictureFrame)
    # setupUi

    def retranslateUi(self, pictureFrame):
        pictureFrame.setWindowTitle(QCoreApplication.translate("pictureFrame", u"Yolo predict", None))
        self.videoFrame.setText(QCoreApplication.translate("pictureFrame", u"webcam", None))
        self.resultsFrame.setText(QCoreApplication.translate("pictureFrame", u"Results", None))
    # retranslateUi

