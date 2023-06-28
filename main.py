# 开发第一个基于PyQt5的桌面应用
import sys
from PyQt5.QtWidgets import (
    QApplication
)
from PyQt5 import QtCore
# 解决设计窗口与显示窗口不同的问题
from widgets import win
from qt_material import apply_stylesheet
from PyQt5.QtCore import Qt
# 画质和窗口问题
QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    apply_stylesheet(app, 'default')
    # 创建一个窗口 可传递参数 窗口由u111i初始化 更加独立化的设计
    win_one = win.Win()
    # 显示窗口
    win_one.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    sys.exit(app.exec_())
