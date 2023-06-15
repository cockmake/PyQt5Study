from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDesktopWidget, QPushButton, QFileDialog
from ui import one
import cv2 as cv
import utils
from widget.style import qss
from PyQt5.QtGui import QPixmap
class Win(QtWidgets.QWidget, one.Ui_Form):
    def __init__(self):
        super(Win, self).__init__()
        self.setupUi(self)
        self.init_style()
        self.setToolTip("123")
        # 手动绑定信号和槽
        self.pushButton.clicked.connect(self.button_clicked)
        self.open_img.clicked.connect(self.to_open_img)

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
