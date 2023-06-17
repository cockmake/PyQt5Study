from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt
from PyQt5.QtWidgets import QDesktopWidget, QFileDialog
from ui import one
import cv2 as cv
import os
import utils
from widget.style import qss
from PyQt5.QtGui import QPixmap, QWindow
# 窗口自己无法释放自己, 但是可以通过外部调用
class Win(QtWidgets.QWidget, one.Ui_Form):
    # 自定义信号 在这
    sss = pyqtSignal(str, int)
    close_s = pyqtSignal()

    def __init__(self):
        super(Win, self).__init__()
        self.setupUi(self)
        self.init_style()
        self.setToolTip("123")
        # 手动绑定信号和槽
        self.pushButton.clicked.connect(self.button_clicked)
        self.open_img.clicked.connect(self.to_open_img)
        self.open_win2.clicked.connect(self.open_new_win)
        self.close_win2.clicked.connect(self.close_new_win)
        self.emitS.clicked.connect(self.sendSignal)
        self.son_win = None
        print('我被创建了')
        # 连接信号和槽在这
        self.sss.connect(self.rrr)

    # 触发信号在这
    def sendSignal(self):
        self.sss.emit('1', 1)

    def center(self):
        screenRect = QDesktopWidget().screenGeometry()
        lt = ((screenRect.width() - self.width()) / 2,
              (screenRect.height() - self.height()) / 2)
        self.move(lt[0], lt[1])

    def button_clicked(self):
        sender = self.sender()
        # sender.setVisible(False)
        self.close()

    def to_open_img(self):
        img_path, file_type = QFileDialog.getOpenFileName(None, '选择图片', "./", "Image files (*.jpg *.gif *.png *.jpeg)")
        if img_path == '': return
        try:
            img = cv.imread(img_path)
            q_img = utils.cvimg_to_qtimg(img).scaled(self.label_img.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            q_pix = QPixmap(q_img)
            self.label_img.setPixmap(q_pix)

        except Exception as E:
            print(E)

    def init_style(self):
        self.setStyleSheet(qss)

    def open_new_win(self, flag):
        if self.son_win is None:
            self.son_win = Win()
            self.son_win.close_s.connect(self.closeSonWin)  # 子窗口与父窗口的关闭释放函数绑定
        self.son_win.show()

    def close_new_win(self, flag):
        if self.son_win is not None:
            del self.son_win
            self.son_win = None

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.close_s.emit()
        event.accept()

    def __del__(self):
        print('我被释放了')

    # 自定义槽函数
    def rrr(self, a, b):
        if self.son_win is not None:
            print(self.son_win.windowTitle())
        # print(self.sender()) # 是主窗口
        self.SearchLineEdit.setText(a)

    # 自定义槽函数
    def closeSonWin(self):
        # 这里利用python的垃圾回收机制释放窗口占用的资源
        self.son_win = None