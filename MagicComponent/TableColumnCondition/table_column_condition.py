# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_column_condition.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_table_column_condition(object):
    def setupUi(self, table_column_condition):
        table_column_condition.setObjectName("table_column_condition")
        table_column_condition.resize(400, 550)
        font = QtGui.QFont()
        font.setPointSize(11)
        table_column_condition.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(table_column_condition)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(table_column_condition)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.search_key = QtWidgets.QLineEdit(self.groupBox)
        self.search_key.setObjectName("search_key")
        self.verticalLayout_2.addWidget(self.search_key)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.select_all = QtWidgets.QCheckBox(self.groupBox)
        self.select_all.setObjectName("select_all")
        self.horizontalLayout_2.addWidget(self.select_all)
        self.not_select_all = QtWidgets.QCheckBox(self.groupBox)
        self.not_select_all.setObjectName("not_select_all")
        self.horizontalLayout_2.addWidget(self.not_select_all)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.scroll_area = QtWidgets.QScrollArea(self.groupBox)
        self.scroll_area.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.scroll_area.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 376, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_area.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scroll_area)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel.sizePolicy().hasHeightForWidth())
        self.cancel.setSizePolicy(sizePolicy)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.confirm = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm.sizePolicy().hasHeightForWidth())
        self.confirm.setSizePolicy(sizePolicy)
        self.confirm.setObjectName("confirm")
        self.horizontalLayout.addWidget(self.confirm)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_3.setStretch(0, 7)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(table_column_condition)
        QtCore.QMetaObject.connectSlotsByName(table_column_condition)

    def retranslateUi(self, table_column_condition):
        _translate = QtCore.QCoreApplication.translate
        table_column_condition.setWindowTitle(_translate("table_column_condition", "筛选"))
        self.groupBox.setTitle(_translate("table_column_condition", "xxx"))
        self.search_key.setPlaceholderText(_translate("table_column_condition", "搜索"))
        self.select_all.setText(_translate("table_column_condition", "全选"))
        self.not_select_all.setText(_translate("table_column_condition", "全不选"))
        self.cancel.setText(_translate("table_column_condition", "取消"))
        self.confirm.setText(_translate("table_column_condition", "确认"))
