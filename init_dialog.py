# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'init_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(435, 356)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 310, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 40, 331, 91))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.whatIsYoloButton = QPushButton(self.layoutWidget)
        self.whatIsYoloButton.setObjectName(u"whatIsYoloButton")

        self.gridLayout.addWidget(self.whatIsYoloButton, 0, 1, 1, 1)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(40, 180, 331, 121))
        self.formLayout = QFormLayout(self.layoutWidget1)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_4)

        self.modelListBox = QComboBox(self.layoutWidget1)
        self.modelListBox.setObjectName(u"modelListBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.modelListBox)

        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.sourceListBox = QComboBox(self.layoutWidget1)
        self.sourceListBox.setObjectName(u"sourceListBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.sourceListBox)

        self.label_youtube = QLabel(self.layoutWidget1)
        self.label_youtube.setObjectName(u"label_youtube")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_youtube)

        self.youtubeURL = QLineEdit(self.layoutWidget1)
        self.youtubeURL.setObjectName(u"youtubeURL")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.youtubeURL)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"What is YOLO??", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Check Documentation", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"YOLO Documentation", None))
        self.whatIsYoloButton.setText(QCoreApplication.translate("Dialog", u"Check Wikipedia", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"YOLO object detection demo", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Choose YOLO Model", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Choose Video source", None))
        self.label_youtube.setText(QCoreApplication.translate("Dialog", u"IInput Youtube URL", None))
    # retranslateUi

