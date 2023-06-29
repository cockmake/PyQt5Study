from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDesktopWidget, QFileDialog
from .ui import one
import cv2 as cv
import methods
from PyQt5 import QtGui
from widgets.widget2.win2 import Win2
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


# 窗口自己无法释放自己, 但是可以通过外部调用
class Win(QtWidgets.QWidget, one.Ui_Form):
    # 自定义信号 在这
    sss = pyqtSignal(str, int)

    def __init__(self):
        super(Win, self).__init__()
        self.setupUi(self)
        self.initStyle()
        # 手动绑定信号和槽
        self.pushButton.clicked.connect(self.button_clicked)
        self.open_img.clicked.connect(self.to_open_img)
        self.open_win2.clicked.connect(self.open_new_win)
        self.close_win2.clicked.connect(self.close_new_win)
        self.emitS.clicked.connect(self.sendSignal)
        self.son_win = None
        print('父窗口被创建了')
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
            q_img = methods.cvimg_to_qtimg(img).scaled(self.label_img.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            q_pix = QPixmap(q_img)
            self.label_img.setPixmap(q_pix)

        except Exception as E:
            print(E)

    def initStyle(self):
        self.setStyleSheet('')

    def open_new_win(self, flag):
        try:
            if self.son_win is None:
                self.son_win = Win2(self.parent())
                self.son_win.close_s.connect(self.closeSonWin)  # 子窗口与父窗口的关闭释放函数绑定
            self.son_win.show()
        except Exception as E:
            print(E)

    def close_new_win(self, flag):
        if self.son_win is not None:
            self.son_win.close()

    def __del__(self):
        print('父窗口被被释放了')

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        pass

    # 自定义槽函数
    def rrr(self, a, b):
        # print(self.sender()) # 是主窗口
        self.SearchLineEdit.setText(a)

    # 自定义槽函数
    def closeSonWin(self):
        # 这里操作子窗口被关闭并已经释放了其资源后的处理
        # 这里利用python的垃圾回收机制释放窗口占用的资源
        self.son_win = None
        print('父窗口操作子窗口关闭事件')