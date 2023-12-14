import sqlite3
import sys
import matplotlib.pyplot as plt
import os

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from main_wnd_disign import Ui_MainWnd
from analiz_expense_wnd_disign import Ui_expense_analiz_wnd
from analiz_income_wnd_disign import Ui_analiz_incom_wnd


class MainWnd(QMainWindow, Ui_MainWnd):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('images/иконка.ico'))
        self.add_btn_expense.clicked.connect(self.add_expense)
        self.add_btn_income.clicked.connect(self.add_income)
        self.st_btn_expense.clicked.connect(self.show_analiz_expense_wnd)
        self.st_btn_income.clicked.connect(self.show_analiz_income_wnd)
        # self.get_chart_expense()
        # self.get_chart_income()

    def add_expense(self):
        category_expense = self.ct_exp_le.text()
        sum_expense = self.add_exp_le.text()
        date_expense = self.date_exp_le.text()
        self.con = sqlite3.connect('data/my_users.db')
        self.cur = self.con.cursor()
        self.cur.execute('''INSERT INTO expense VALUES (?, ?, ?)''', (category_expense, sum_expense, date_expense))
        self.con.commit()
        self.con.close()

    def add_income(self):
        category_income = self.ct_inc_le.text()
        sum_income = self.add_inc_le.text()
        date_income = self.date_inc_le.text()
        self.con = sqlite3.connect('data/my_users.db')
        self.cur = self.con.cursor()
        self.cur.execute('''INSERT INTO income VALUES (?, ?, ?)''', (category_income, sum_income, date_income))
        self.con.commit()
        self.con.close()

    def show_analiz_expense_wnd(self):
        self.analiz_exp_win = AnalizExpenseWnd()
        self.analiz_exp_win.show()
        self.hide()

    def show_analiz_income_wnd(self):
        self.analiz_inc_win = AnalizIncomeWnd()
        self.analiz_inc_win.show()
        self.hide()


class AnalizExpenseWnd(QMainWindow, Ui_expense_analiz_wnd):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('images/иконка.ico'))
        self.back_btn_exp.clicked.connect(self.back_to_main_wnd_exp)
        self.label_expense = QLabel(self)
        self.get_chart_expense() ####
        self.label_expense.setGeometry(50, 50, 600, 450)
        pixmap = QPixmap("images/expense_chart.png")
        self.label_expense.setPixmap(pixmap)

    def get_chart_expense(self):
        self.con = sqlite3.connect('data/my_users.db')
        self.cur = self.con.cursor()
        self.cur.execute('''SELECT * FROM expense''')
        data_exp = self.cur.fetchall()
        cat_exp = []
        sums_exp = []
        for elem in data_exp:
            if elem[0] not in cat_exp:
                cat_exp.append(elem[0])
                sums_exp.append(int(elem[1]))

        fig, ax = plt.subplots()
        ax.pie(sums_exp, labels=cat_exp, autopct='%1.1f%%')
        fig.savefig('images/expense_chart.png')

    def back_to_main_wnd_exp(self):
        self.back_exp = MainWnd()
        self.back_exp.show()
        self.hide()

        if os.path.isfile('images/expense_chart.png'):####
            os.remove('images/expense_chart.png')####


class AnalizIncomeWnd(QMainWindow, Ui_analiz_incom_wnd):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('images/иконка.ico'))
        self.back_btn__icome.clicked.connect(self.back_to_main_wnd_inc)
        self.label_expense = QLabel(self)
        self.get_chart_income()

        self.label_expense.setGeometry(50, 50, 600, 450)
        pixmap = QPixmap("images/income_chart.png")
        self.label_expense.setPixmap(pixmap)

    def get_chart_income(self):
        self.con = sqlite3.connect('data/my_users.db')
        self.cur = self.con.cursor()
        self.cur.execute('''SELECT * FROM income''')
        data_inc = self.cur.fetchall()
        cat_inc = []
        sums_inc = []
        for elem in data_inc:
            if elem[0] not in cat_inc:
                cat_inc.append(elem[0])
                sums_inc.append(int(elem[1]))

        fig, ax = plt.subplots()
        ax.pie(sums_inc, labels=cat_inc, autopct='%1.1f%%')
        fig.savefig('images/income_chart.png')

    def back_to_main_wnd_inc(self):
        self.back_inc = MainWnd()
        self.back_inc.show()
        self.hide()

        if os.path.isfile('images/income_chart.png'):####
            os.remove('images/income_chart.png')####


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_wnd = MainWnd()
    main_wnd.show()
    sys.exit(app.exec_())
