# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        Dialog.setMinimumSize(QtCore.QSize(1000, 600))
        Dialog.setMaximumSize(QtCore.QSize(1000, 600))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 20, 831, 41))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 220, 261, 91))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 320, 261, 271))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_1.setGeometry(QtCore.QRect(10, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(210, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 70, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(60, 70, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(110, 70, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(160, 70, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(210, 70, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_11.setGeometry(QtCore.QRect(10, 120, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_12.setGeometry(QtCore.QRect(60, 120, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_13.setGeometry(QtCore.QRect(110, 120, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_14.setGeometry(QtCore.QRect(160, 120, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_15.setGeometry(QtCore.QRect(210, 120, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_16.setGeometry(QtCore.QRect(10, 170, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(60, 170, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(110, 170, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(160, 170, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(210, 170, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_21.setGeometry(QtCore.QRect(10, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_22.setGeometry(QtCore.QRect(60, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(110, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_24.setGeometry(QtCore.QRect(160, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_24.setFont(font)
        self.lineEdit_24.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_25.setGeometry(QtCore.QRect(210, 220, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_25.setFont(font)
        self.lineEdit_25.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(290, 90, 700, 500))
        self.groupBox_4.setMinimumSize(QtCore.QSize(700, 500))
        self.groupBox_4.setMaximumSize(QtCore.QSize(700, 500))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(0, 430, 700, 50))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.groupBox_4)
        self.widget.setGeometry(QtCore.QRect(0, 10, 700, 400))
        self.widget.setObjectName("widget")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 89, 261, 131))
        self.groupBox_5.setObjectName("groupBox_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Micro/Nano Electronic Devices Research group"))
        self.groupBox.setTitle(_translate("Dialog", "state"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_2.setTitle(_translate("Dialog", "data"))
        self.lineEdit_1.setText(_translate("Dialog", "1"))
        self.lineEdit_2.setText(_translate("Dialog", "1"))
        self.lineEdit_3.setText(_translate("Dialog", "1"))
        self.lineEdit_4.setText(_translate("Dialog", "1"))
        self.lineEdit_5.setText(_translate("Dialog", "1"))
        self.lineEdit_6.setText(_translate("Dialog", "1"))
        self.lineEdit_7.setText(_translate("Dialog", "1"))
        self.lineEdit_8.setText(_translate("Dialog", "1"))
        self.lineEdit_9.setText(_translate("Dialog", "1"))
        self.lineEdit_10.setText(_translate("Dialog", "1"))
        self.lineEdit_11.setText(_translate("Dialog", "1"))
        self.lineEdit_12.setText(_translate("Dialog", "1"))
        self.lineEdit_13.setText(_translate("Dialog", "1"))
        self.lineEdit_14.setText(_translate("Dialog", "1"))
        self.lineEdit_15.setText(_translate("Dialog", "1"))
        self.lineEdit_16.setText(_translate("Dialog", "1"))
        self.lineEdit_17.setText(_translate("Dialog", "1"))
        self.lineEdit_18.setText(_translate("Dialog", "1"))
        self.lineEdit_19.setText(_translate("Dialog", "1"))
        self.lineEdit_20.setText(_translate("Dialog", "1"))
        self.lineEdit_21.setText(_translate("Dialog", "1"))
        self.lineEdit_22.setText(_translate("Dialog", "1"))
        self.lineEdit_23.setText(_translate("Dialog", "1"))
        self.lineEdit_24.setText(_translate("Dialog", "1"))
        self.lineEdit_25.setText(_translate("Dialog", "1"))
        self.groupBox_4.setTitle(_translate("Dialog", "painting"))
        self.pushButton.setText(_translate("Dialog", "Reset"))
        self.groupBox_5.setTitle(_translate("Dialog", "view rotation"))
