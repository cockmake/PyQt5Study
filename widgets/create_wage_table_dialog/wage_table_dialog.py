# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wage_table_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wage_table_dialog(object):
    def setupUi(self, wage_table_dialog):
        wage_table_dialog.setObjectName("wage_table_dialog")
        wage_table_dialog.resize(900, 675)
        font = QtGui.QFont()
        font.setPointSize(11)
        wage_table_dialog.setFont(font)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(wage_table_dialog)
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(wage_table_dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.wage_table_start_date = QtWidgets.QDateEdit(wage_table_dialog)
        self.wage_table_start_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 1, 1), QtCore.QTime(0, 0, 0)))
        self.wage_table_start_date.setObjectName("wage_table_start_date")
        self.horizontalLayout.addWidget(self.wage_table_start_date)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(wage_table_dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.wage_table_end_date = QtWidgets.QDateEdit(wage_table_dialog)
        self.wage_table_end_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2024, 1, 1), QtCore.QTime(0, 0, 0)))
        self.wage_table_end_date.setObjectName("wage_table_end_date")
        self.horizontalLayout_2.addWidget(self.wage_table_end_date)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(wage_table_dialog)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.drivers_key = QtWidgets.QLineEdit(wage_table_dialog)
        self.drivers_key.setObjectName("drivers_key")
        self.verticalLayout_3.addWidget(self.drivers_key)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.drivers = QtWidgets.QScrollArea(wage_table_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drivers.sizePolicy().hasHeightForWidth())
        self.drivers.setSizePolicy(sizePolicy)
        self.drivers.setMinimumSize(QtCore.QSize(0, 230))
        self.drivers.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.drivers.setFrameShadow(QtWidgets.QFrame.Plain)
        self.drivers.setWidgetResizable(True)
        self.drivers.setObjectName("drivers")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 302, 247))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.drivers.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_5.addWidget(self.drivers)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(wage_table_dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.cheshudanweis_key = QtWidgets.QLineEdit(wage_table_dialog)
        self.cheshudanweis_key.setObjectName("cheshudanweis_key")
        self.verticalLayout.addWidget(self.cheshudanweis_key)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.cheshudanweis = QtWidgets.QScrollArea(wage_table_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cheshudanweis.sizePolicy().hasHeightForWidth())
        self.cheshudanweis.setSizePolicy(sizePolicy)
        self.cheshudanweis.setMinimumSize(QtCore.QSize(0, 230))
        self.cheshudanweis.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.cheshudanweis.setFrameShadow(QtWidgets.QFrame.Plain)
        self.cheshudanweis.setWidgetResizable(True)
        self.cheshudanweis.setObjectName("cheshudanweis")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 302, 247))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.cheshudanweis.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_4.addWidget(self.cheshudanweis)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(wage_table_dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.shou_groupbox = QtWidgets.QGroupBox(wage_table_dialog)
        self.shou_groupbox.setFlat(True)
        self.shou_groupbox.setObjectName("shou_groupbox")
        self.verticalLayout_5.addWidget(self.shou_groupbox)
        self.fu_groupbox = QtWidgets.QGroupBox(wage_table_dialog)
        self.fu_groupbox.setFlat(True)
        self.fu_groupbox.setObjectName("fu_groupbox")
        self.verticalLayout_5.addWidget(self.fu_groupbox)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.wage_table_dialog_cancel_btn = QtWidgets.QPushButton(wage_table_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wage_table_dialog_cancel_btn.sizePolicy().hasHeightForWidth())
        self.wage_table_dialog_cancel_btn.setSizePolicy(sizePolicy)
        self.wage_table_dialog_cancel_btn.setObjectName("wage_table_dialog_cancel_btn")
        self.horizontalLayout_3.addWidget(self.wage_table_dialog_cancel_btn)
        self.wage_table_dialog_search_btn = QtWidgets.QPushButton(wage_table_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wage_table_dialog_search_btn.sizePolicy().hasHeightForWidth())
        self.wage_table_dialog_search_btn.setSizePolicy(sizePolicy)
        self.wage_table_dialog_search_btn.setObjectName("wage_table_dialog_search_btn")
        self.horizontalLayout_3.addWidget(self.wage_table_dialog_search_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_6.setStretch(0, 7)
        self.verticalLayout_6.setStretch(1, 1)

        self.retranslateUi(wage_table_dialog)
        QtCore.QMetaObject.connectSlotsByName(wage_table_dialog)

    def retranslateUi(self, wage_table_dialog):
        _translate = QtCore.QCoreApplication.translate
        wage_table_dialog.setWindowTitle(_translate("wage_table_dialog", "工资查询"))
        self.label.setText(_translate("wage_table_dialog", "开始日期"))
        self.wage_table_start_date.setDisplayFormat(_translate("wage_table_dialog", "yyyy-MM-dd"))
        self.label_2.setText(_translate("wage_table_dialog", "结束日期"))
        self.wage_table_end_date.setDisplayFormat(_translate("wage_table_dialog", "yyyy-MM-dd"))
        self.label_6.setText(_translate("wage_table_dialog", "司机"))
        self.drivers_key.setPlaceholderText(_translate("wage_table_dialog", "搜索"))
        self.label_4.setText(_translate("wage_table_dialog", "车属单位"))
        self.cheshudanweis_key.setPlaceholderText(_translate("wage_table_dialog", "搜索"))
        self.label_3.setText(_translate("wage_table_dialog", "收付状态"))
        self.shou_groupbox.setTitle(_translate("wage_table_dialog", "收"))
        self.fu_groupbox.setTitle(_translate("wage_table_dialog", "付"))
        self.wage_table_dialog_cancel_btn.setText(_translate("wage_table_dialog", "取消"))
        self.wage_table_dialog_search_btn.setText(_translate("wage_table_dialog", "查询"))
