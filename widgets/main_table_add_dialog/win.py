from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal

from widgets.main_table_add_dialog.main_table_add_dialog import Ui_main_table_add_dialog


class MainTableAddDialog(QtWidgets.QDialog, Ui_main_table_add_dialog):
    add_confirm = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(MainTableAddDialog, self).__init__(parent)
        self.setupUi(self)

        self.main_table_add_confirm.setFocus()
        self.main_table_add_confirm.clicked.connect(self.main_table_add_confirm_slot)
        self.main_table_add_cancel.clicked.connect(self.close)
        # 设置默认日期为今天
        self.main_table_add_date.setDate(QtCore.QDate.currentDate())
        # 只允许输入Double类型的数字
        self.main_table_add_money.setValidator(QtGui.QDoubleValidator())
        self.main_table_add_pay.setValidator(QtGui.QDoubleValidator())

    def main_table_add_confirm_slot(self):
        if self.qiandan_no.isChecked():
            qiandan = self.qiandan_no.text()
        elif self.qiandan_yes.isChecked():
            qiandan = self.qiandan_yes.text()
        else:
            qiandan = ""
        if self.shou_no.isChecked():
            shou = self.shou_no.text()
        elif self.shou_yes.isChecked():
            shou = self.shou_yes.text()
        else:
            shou = ""
        if self.fu_no.isChecked():
            fu = self.fu_no.text()
        elif self.fu_yes.isChecked():
            fu = self.fu_yes.text()
        else:
            fu = ""
        if self.main_table_add_money.text() == "":
            je = "0"
            # 不允许金额为空
            # QtWidgets.QMessageBox.warning(self, "警告", "金额不能为空")
            # return
        else:
            je = self.main_table_add_money.text()

        if self.main_table_add_pay.text() == "":
            yf = "0"
            # 不允许应付为空
            # QtWidgets.QMessageBox.warning(self, "警告", "应付不能为空")
            # return
        else:
            yf = self.main_table_add_pay.text()

        target_info = {
            "date": self.main_table_add_date.date().toString("yyyy-MM-dd").strip(),
            "driver": self.main_table_add_driver.text().strip(),
            "car_type": self.main_table_add_car_type.text().strip(),
            "car_number": self.main_table_add_car_number.text().strip(),
            "qiandan": qiandan,
            "cheshudanwei": self.main_table_add_cheshudanwei.text().strip(),
            "yongchedanwei": self.main_table_add_yongchedanwei.text().strip(),
            "time": self.main_table_add_time.text().strip(),
            "money": je,
            "pay": yf,
            "shou": shou,
            "fu": fu,
            "remark": self.main_table_add_remark.text().strip(),
            "itinerary": self.main_table_add_itinerary.text().strip(),
        }
        self.add_confirm.emit(target_info)
        # 添加完成后清空输入框
        # self.add_completed_slot()

    def add_completed_slot(self):
        # 日期不清空其余清空 复选框不清空
        self.main_table_add_driver.clear()
        self.main_table_add_car_type.clear()
        self.main_table_add_car_number.clear()
        self.main_table_add_yongchedanwei.clear()
        self.main_table_add_money.clear()
        self.main_table_add_pay.clear()
        self.main_table_add_remark.clear()
        self.main_table_add_itinerary.clear()
        self.main_table_add_time.clear()

