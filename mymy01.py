# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mymy01.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(772, 74)
        # 窗口圆角用qss设置无效，改用qpainter画出来
        # Form.setStyleSheet("QWidget{border-radius:20px}")
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 一定要有,否则圆角后任有矩形背景

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(368, 52, 391, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 751, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{border-radius:15px}")
        self.lineEdit.setTextMargins(8, 0, 0, 0)
        self.lineEdit.setObjectName("lineEdit")

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.SubWindow | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(0.8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Powered by NeroSong"))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.label.setFont(font)
