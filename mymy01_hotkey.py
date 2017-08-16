# -*- coding: utf8-*-

import sys
from ctypes import *
from ctypes.wintypes import *

import win32con
import win32gui
from PyQt5.QtWidgets import QApplication

import test01

WM_HOTKEY = 0x0312
MOD_ALT = 0x0001
MOD_CONTROL = 0x0002
MOD_SHIFT = 0x0004
WM_KEYUP = 0x0101


class MSG(Structure):
    _fields_ = [('hwnd', c_int),
                ('message', c_uint),
                ('wParam', c_int),
                ('lParam', c_int),
                ('time', c_int),
                ('pt', POINT)]

# 激活窗口焦点,65 is Key 'a'
hotkeyId = 1
if not windll.user32.RegisterHotKey(None, hotkeyId, win32con.MOD_SHIFT, 65):
    sys.exit("Cant Register Hotkey")

msg = MSG()
# app = QApplication(sys.argv)
# w = test01.Test()
# w.show()

app = QApplication(sys.argv)
test = test01.Test()
desktop = QApplication.desktop()
x = (desktop.width() - test.width()) // 2
y = (desktop.height() - test.height()) // 2 + desktop.height() // 4
test.move(x, y)
test.show()


hd = windll.user32.GetActiveWindow()

while True:
    if (windll.user32.GetMessageA(byref(msg), None, 0, 0) != 0):
        if msg.message == WM_HOTKEY and msg.wParam == hotkeyId:

            win32gui.SetForegroundWindow(hd)  #使指定窗口获取焦点且前置

        windll.user32.TranslateMessage(byref(msg))
        windll.user32.DispatchMessageA(byref(msg))




