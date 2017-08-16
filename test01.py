# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QCursor, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from win32con import WM_HOTKEY

from mymy01 import Ui_Form



class Test(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit.textChanged.connect(self.lineEdit_changed)

    # 注册全局热键,仅用于win



    #输入内容改变时执行
    def lineEdit_changed(self, text):
        print(text)
        # todo 在全局快捷键配合任意时刻唤起时，对内容做处理

    # 防止在焦点状态下误按esc退出
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            print('you r esc')

    # 重写三个方法使窗口支持拖动
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    # 重写paintEvent方法来获得窗口圆角
    def paintEvent(self, QPaintEvent):
        qp = QPainter(self)
        qp.setPen(Qt.transparent)
        qp.setBrush(QColor("#1E90FF"))
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setRenderHint(QPainter.SmoothPixmapTransform)
        # 反锯齿，平滑变化算法。不能用|写在一起用？？？
        qp.drawRoundedRect(0, 0, self.width() - 1, self.height() - 1, 10, 10)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Test()
    desktop = QApplication.desktop()
    x = (desktop.width() - test.width()) // 2
    y = (desktop.height() - test.height()) // 2 + desktop.height() // 4
    test.move(x, y)
    test.show()
    sys.exit(app.exec_())
