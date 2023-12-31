# 开发第一个基于PyQt5的桌面应用
import sys
from PyQt5.QtWidgets import (
    QApplication
)
# 解决设计窗口与显示窗口不同的问题
from widgets.widget import win
from widgets.widget2 import win2
from PyQt5.QtCore import Qt
# 画质和窗口问题
QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口 可传递参数 窗口由u111i初始化 更加独立化的设计
    # 显示窗口
    win_one = win.Win()
    win_one.show()
    # win_two = win2.Win2()
    # win_two.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    sys.exit(app.exec_())
