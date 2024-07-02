# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QTabWidget,
    QWidget)

class Ui_TCVirtualCamera(object):
    def setupUi(self, TCVirtualCamera):
        if not TCVirtualCamera.objectName():
            TCVirtualCamera.setObjectName(u"TCVirtualCamera")
        TCVirtualCamera.resize(480, 270)
        self.tabWidget = QTabWidget(TCVirtualCamera)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 241, 131))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.comboBox = QComboBox(self.tab_1)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(70, 10, 151, 31))
        self.label = QLabel(self.tab_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 71, 31))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.pushButton = QPushButton(self.tab_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 60, 81, 31))
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 71, 31))
        self.label_7.setFont(font)
        self.pushButton_2 = QPushButton(self.tab_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(140, 60, 81, 31))
        self.plainTextEdit_5 = QPlainTextEdit(self.tab_2)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setGeometry(QRect(50, 10, 171, 31))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.label_8 = QLabel(self.tab_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 71, 31))
        self.label_8.setFont(font)
        self.plainTextEdit_4 = QPlainTextEdit(self.tab_3)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(50, 10, 171, 31))
        self.tabWidget.addTab(self.tab_3, "")
        self.groupBox = QGroupBox(TCVirtualCamera)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 130, 241, 131))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 17, 71, 31))
        self.label_2.setFont(font)
        self.plainTextEdit = QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(50, 17, 161, 31))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 54, 71, 31))
        self.label_3.setFont(font)
        self.plainTextEdit_2 = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(50, 54, 161, 31))
        self.plainTextEdit_3 = QPlainTextEdit(self.groupBox)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(50, 90, 161, 31))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 90, 71, 31))
        self.label_4.setFont(font)
        self.groupBox_2 = QGroupBox(TCVirtualCamera)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(260, 0, 211, 261))
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(52, 20, 151, 31))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(12, 20, 71, 31))
        self.label_5.setFont(font)
        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(120, 220, 81, 31))
        self.pushButton_5 = QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(30, 220, 81, 31))

        self.retranslateUi(TCVirtualCamera)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TCVirtualCamera)
    # setupUi

    def retranslateUi(self, TCVirtualCamera):
        TCVirtualCamera.setWindowTitle(QCoreApplication.translate("TCVirtualCamera", u"TCVirtualCamera", None))
        self.label.setText(QCoreApplication.translate("TCVirtualCamera", u"\u6444\u50cf\u5934\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("TCVirtualCamera", u"\u5237\u65b0\u5217\u8868", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("TCVirtualCamera", u"\u6444\u50cf\u5934\u6a21\u5f0f", None))
        self.label_7.setText(QCoreApplication.translate("TCVirtualCamera", u"\u6587\u4ef6\uff1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("TCVirtualCamera", u"\u9009\u62e9\u6587\u4ef6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("TCVirtualCamera", u"\u89c6\u9891\u6587\u4ef6\u6a21\u5f0f", None))
        self.label_8.setText(QCoreApplication.translate("TCVirtualCamera", u"\u5730\u5740\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("TCVirtualCamera", u"\u6d41\u5a92\u4f53\u6a21\u5f0f", None))
        self.groupBox.setTitle(QCoreApplication.translate("TCVirtualCamera", u"\u81ea\u5b9a\u4e49\u6570\u636e", None))
        self.label_2.setText(QCoreApplication.translate("TCVirtualCamera", u"\u5bbd\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("TCVirtualCamera", u"\u9ad8\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("TCVirtualCamera", u"\u5e27\uff1a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TCVirtualCamera", u"\u97f3\u9891\u8f93\u51fa", None))
        self.label_5.setText(QCoreApplication.translate("TCVirtualCamera", u"\u8bbe\u5907\uff1a", None))
        self.pushButton_4.setText(QCoreApplication.translate("TCVirtualCamera", u"\u786e\u5b9a", None))
        self.pushButton_5.setText(QCoreApplication.translate("TCVirtualCamera", u"\u53d6\u6d88", None))
    # retranslateUi
