import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class cofee_table(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Капучино')
        self.pushButton.clicked.connect(self.new)
        self.conor = sqlite3.connect('coffee.sqlite')
        self.cur = self.conor.cursor()
        self.result = self.cur.execute('''SELECT 
                c.sort, g.d_or_d, c.roast, c.teasty, c.price, c.vol
            FROM 
                coffee c,
                g_g g WHERE c.g_or_g = g.id''').fetchall()
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableWidget.setRowCount(len(self.result))
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                a = QTableWidgetItem(str(val))
                self.tableWidget.setItem(i, j, a)

    def new(self):
        self.w2 = New()
        self.w2.show()



class New(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.setWindowTitle('Новый')
        self.conor = sqlite3.connect('coffee.sqlite')
        self.cur = self.conor.cursor()
        self.pushButton.clicked.connect(self.make)

    def make(self):
        a1 = self.lineEdit
        s = self.lineEdit_2
        a2 = self.cur.execute(f'''SELECT * FROM g_g 
                    WHERE d_or_d = '{s}' ''').fetchall()[0][0]
        a3 = self.lineEdit_3
        a4 = self.lineEdit_4
        a5 = self.lineEdit_5
        a6 = self.lineEdit_6
        self.neww = f'''INSERT INTO coffee
                    (sort, g_or_g, roast, teasty, price, vol)
                    VALUES
                    (?, ?, ?, ?, ?, ?)'''
        data_tuple = (a1, a2, a3, a4, a5, a6)
        self.cur.execute(self.neww, data_tuple)
        self.conor.commit()
        self.conor.close()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = cofee_table()
    w.show()
    sys.exit(app.exec_())