# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(677, 607)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.sysButton = QtWidgets.QPushButton(Form)
        self.sysButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.sysButton.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.sysButton.setObjectName("sysButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(310, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.BaiduButt = QtWidgets.QPushButton(Form)
        self.BaiduButt.setGeometry(QtCore.QRect(390, 50, 75, 31))
        self.BaiduButt.setStatusTip("")
        self.BaiduButt.setAutoFillBackground(False)
        self.BaiduButt.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.BaiduButt.setObjectName("BaiduButt")
        self.MiguButt = QtWidgets.QPushButton(Form)
        self.MiguButt.setGeometry(QtCore.QRect(480, 50, 75, 31))
        self.MiguButt.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.MiguButt.setObjectName("MiguButt")
        self.TencentButt = QtWidgets.QPushButton(Form)
        self.TencentButt.setGeometry(QtCore.QRect(570, 50, 75, 31))
        self.TencentButt.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.TencentButt.setObjectName("TencentButt")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(150, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(320, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textGet = QtWidgets.QLabel(Form)
        self.textGet.setGeometry(QtCore.QRect(40, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.textGet.setFont(font)
        self.textGet.setText("")
        self.textGet.setObjectName("textGet")
        self.searchButt = QtWidgets.QPushButton(Form)
        self.searchButt.setGeometry(QtCore.QRect(260, 50, 41, 71))
        self.searchButt.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.searchButt.setObjectName("searchButt")
        self.textTarget = QtWidgets.QLabel(Form)
        self.textTarget.setGeometry(QtCore.QRect(210, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.textTarget.setFont(font)
        self.textTarget.setText("")
        self.textTarget.setObjectName("textTarget")
        self.textSuccess_2 = QtWidgets.QLabel(Form)
        self.textSuccess_2.setGeometry(QtCore.QRect(390, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.textSuccess_2.setFont(font)
        self.textSuccess_2.setText("")
        self.textSuccess_2.setObjectName("textSuccess_2")
        self.textError = QtWidgets.QLabel(Form)
        self.textError.setGeometry(QtCore.QRect(60, 160, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.textError.setFont(font)
        self.textError.setText("")
        self.textError.setObjectName("textError")
        self.keywordEdit = QtWidgets.QLineEdit(Form)
        self.keywordEdit.setGeometry(QtCore.QRect(90, 50, 161, 31))
        self.keywordEdit.setObjectName("keywordEdit")
        self.getBar = QtWidgets.QProgressBar(Form)
        self.getBar.setGeometry(QtCore.QRect(10, 190, 661, 23))
        self.getBar.setProperty("value", 0)
        self.getBar.setTextVisible(True)
        self.getBar.setOrientation(QtCore.Qt.Horizontal)
        self.getBar.setInvertedAppearance(False)
        self.getBar.setObjectName("getBar")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 40, 669, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.picNumEdit = QtWidgets.QLineEdit(Form)
        self.picNumEdit.setGeometry(QtCore.QRect(90, 90, 161, 31))
        self.picNumEdit.setObjectName("picNumEdit")
        self.label_picNum = QtWidgets.QLabel(Form)
        self.label_picNum.setGeometry(QtCore.QRect(10, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.label_picNum.setFont(font)
        self.label_picNum.setObjectName("label_picNum")

        self.retranslateUi(Form)
        self.sysButton.clicked.connect(Form.test1)
        self.BaiduButt.clicked.connect(self.targetBaidu)
        self.MiguButt.clicked.connect(self.targetMigu)
        self.TencentButt.clicked.connect(self.targetTencent)
        self.searchButt.clicked.connect(self.search)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "test"))
        self.label.setText(_translate("Form", "Key word"))
        self.sysButton.setText(_translate("Form", "system"))
        self.label_2.setText(_translate("Form", "Platform"))
        self.BaiduButt.setText(_translate("Form", "Baidu"))
        self.MiguButt.setText(_translate("Form", "Migu"))
        self.TencentButt.setText(_translate("Form", "Tencent"))
        self.label_3.setText(_translate("Form", "Get:"))
        self.label_4.setText(_translate("Form", "Target:"))
        self.label_5.setText(_translate("Form", "Error:"))
        self.label_6.setText(_translate("Form", "Success:"))
        self.searchButt.setText(_translate("Form", "下载"))
        self.label_picNum.setText(_translate("Form", "Pic Num"))

