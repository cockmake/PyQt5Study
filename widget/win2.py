from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal
from ui import two
from widget.style import qss
# 窗口自己无法释放自己, 但是可以通过外部调用
class Win2(QtWidgets.QWidget, two.Ui_Form2):
    # 自定义信号 在这
    close_s = pyqtSignal()

    def __init__(self):
        super(Win2, self).__init__()
        self.setupUi(self)
        self.init_style()
        print('我被创建了')

    def __del__(self):
        print('我被释放了')

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        # 关闭自己所占的资源
        print('关闭所占资源...')
        self.close_s.emit()


    def init_style(self):
        self.setStyleSheet(qss)