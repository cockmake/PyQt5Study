import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDesktopWidget, QFileDialog, QApplication, QAction
from widgets.widget3.ui import three
import cv2 as cv
import methods
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from qfluentwidgets import FluentIcon as FIF, RoundMenu


# 窗口自己无法释放自己, 但是可以通过外部调用
class Win3(QtWidgets.QWidget, three.Ui_Form2):
    # 自定义信号 在这
    def __init__(self, parent=None):
        super(Win3, self).__init__(parent=parent)
        self.setupUi(self)
        self.SwitchButton.checkedChanged.connect(self.switchChange)
        lis = ['1', '2', '3', '4']
        for li in lis:
            self.ComboBox.addItems(li)
        self.ComboBox.setCurrentIndex(0)
        self.ComboBox.currentIndexChanged.connect(self.comboxIndexChange)
        self.ComboBox.currentTextChanged.connect(self.comboxTextChange)
        self.Slider.valueChanged.connect(self.sliderValueChange)
        self.setToolTip('123')
        ac = QAction(FIF.SEND_FILL.icon(), 'Send', self)
        ac2 = QAction(FIF.SAVE.icon(), 'Save', self)
        ac.triggered.connect(self.actionE)
        ac2.triggered.connect(self.actionE)
        actions = [ac, ac2]
        self.menu = RoundMenu(parent=self)
        self.menu.addActions(actions)
        self.menu.setToolTip('123')
        self.SplitToolButton.setIcon(FIF.GITHUB.icon())
        self.SplitToolButton.setFlyout(self.menu)
        self.SplitToolButton.clicked.connect(self.btnClick)

    def actionE(self):
        print('Action事件')

    def btnClick(self):
        print('按钮被点击了')
    def switchChange(self, value):
        print(value)
    def comboxTextChange(self, value):
        print(value)
    def comboxIndexChange(self, value):
        print(value)
    def sliderValueChange(self, value):
        print(value)
if __name__ == '__main__':
    # 创建QApplication类的实例
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    # 创建一个窗口 可传递参数 窗口由u111i初始化 更加独立化的设计
    # 显示窗口
    win = Win3()
    win.show()
    # win_two = win2.Win2()
    # win_two.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    sys.exit(app.exec_())