import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sqlite3
class cofee_table(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Эспрессо')
        self.conor = sqlite3.connect('coffee.sqlite')
        self.cur = self.conor.cursor()
        self.result = self.cur.execute('''SELECT 
                c.sort, g.d_or_d, c.roast, c.teasty, c.price, c.vol
            FROM 
                coffee c,
                g_g g
            WHERE c.g_or_g = g.id''').fetchall()
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableWidget.setRowCount(len(self.result))
        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                a = QTableWidgetItem(str(val))
                self.tableWidget.setItem(i, j, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = cofee_table()
    w.show()
    sys.exit(app.exec_())