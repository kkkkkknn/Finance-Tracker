# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_analiz_incom_wnd(object):
    def setupUi(self, analiz_incom_wnd):
        analiz_incom_wnd.setObjectName("analiz_incom_wnd")
        analiz_incom_wnd.resize(710, 510)
        analiz_incom_wnd.setStyleSheet("background-color: rgb(255, 255,240);")
        self.centralwidget = QtWidgets.QWidget(analiz_incom_wnd)
        self.centralwidget.setObjectName("centralwidget")
        self.label_analiz_icome = QtWidgets.QLabel(self.centralwidget)
        self.label_analiz_icome.setGeometry(QtCore.QRect(20, 60, 430, 260))
        self.label_analiz_icome.setText("")
        self.label_analiz_icome.setObjectName("label_analiz_icome")
        self.back_btn__icome = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn__icome.setGeometry(QtCore.QRect(645, 10, 50, 30))
        font = QtGui.QFont()
        font.setFamily("Britannic Bold")
        font.setPointSize(14)
        self.back_btn__icome.setFont(font)
        self.back_btn__icome.setObjectName("back_btn__icome")
        analiz_incom_wnd.setCentralWidget(self.centralwidget)

        self.retranslateUi(analiz_incom_wnd)
        QtCore.QMetaObject.connectSlotsByName(analiz_incom_wnd)

    def retranslateUi(self, analiz_incom_wnd):
        _translate = QtCore.QCoreApplication.translate
        analiz_incom_wnd.setWindowTitle(_translate("analiz_incom_wnd", "Анализ доходов"))
        self.back_btn__icome.setText(_translate("analiz_incom_wnd", "<-"))
