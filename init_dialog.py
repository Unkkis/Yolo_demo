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
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(431, 402)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(40, 340, 341, 32))
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
        self.layoutWidget1.setGeometry(QRect(40, 150, 331, 184))
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

        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.modelListBox = QComboBox(self.layoutWidget1)
        self.modelListBox.setObjectName(u"modelListBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.modelListBox)

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

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.confidenceSlider = QSlider(self.layoutWidget1)
        self.confidenceSlider.setObjectName(u"confidenceSlider")
        self.confidenceSlider.setValue(50)
        self.confidenceSlider.setSliderPosition(50)
        self.confidenceSlider.setTracking(True)
        self.confidenceSlider.setOrientation(Qt.Horizontal)
        self.confidenceSlider.setInvertedAppearance(False)
        self.confidenceSlider.setInvertedControls(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.confidenceSlider)

        self.radioButtonCustomPlotting = QRadioButton(self.layoutWidget1)
        self.radioButtonCustomPlotting.setObjectName(u"radioButtonCustomPlotting")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.radioButtonCustomPlotting)

        self.radioButtonYOLOPlotting = QRadioButton(self.layoutWidget1)
        self.radioButtonYOLOPlotting.setObjectName(u"radioButtonYOLOPlotting")
        self.radioButtonYOLOPlotting.setChecked(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.radioButtonYOLOPlotting)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_7)

        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.confidenceLabel = QLabel(Dialog)
        self.confidenceLabel.setObjectName(u"confidenceLabel")
        self.confidenceLabel.setGeometry(QRect(380, 260, 49, 16))

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
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("Dialog", u"Choose from available YOLO models", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Dialog", u"Choose YOLO Model", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Dialog", u"Choose source for video", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Choose Video source", None))
#if QT_CONFIG(tooltip)
        self.label_youtube.setToolTip(QCoreApplication.translate("Dialog", u"Input URL to Youtube video", None))
#endif // QT_CONFIG(tooltip)
        self.label_youtube.setText(QCoreApplication.translate("Dialog", u"IInput Youtube URL", None))
#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("Dialog", u"Draw rectangles only when confidence score is above this treshold. 50% is the norm.", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Confidence treshold", None))
#if QT_CONFIG(tooltip)
        self.confidenceSlider.setToolTip(QCoreApplication.translate("Dialog", u"Draw rectangles only when confidence score is above this treshold. 50% is the norm.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.radioButtonCustomPlotting.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Use plotting where objects with confidence score over 80% are green and under 80% are red.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButtonCustomPlotting.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
#if QT_CONFIG(tooltip)
        self.radioButtonYOLOPlotting.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Use YOLOs built in plotting, where different objects have different colors)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButtonYOLOPlotting.setText(QCoreApplication.translate("Dialog", u"RadioButton", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Use YOLOs built in plotting, where different objects have different colors)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Use YOLO Plotting", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Use plotting where objects with confidence score over 80% are green and under 80% are red.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Use Red/Green Plotting", None))
        self.confidenceLabel.setText(QCoreApplication.translate("Dialog", u"0%", None))
    # retranslateUi

