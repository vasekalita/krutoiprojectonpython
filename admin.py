from db import Database
from PyQt6 import QtWidgets
from pyform.admin_form import Ui_Admin_Form
from update import Update

class Admin(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Admin_Form()
        self.ui.setupUi(self)

        self.db = Database()
        self.cursor = self.db.get_cursor()

        self.ui.request_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.request_table.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.load_data()

    def load_data(self):
        self.cursor.execute("select *from request")
        data = self.cursor.fetchall()

        self.ui.request_table.setRowCount(len(data))

        try:
            for i in range(len(data)):
                self.ui.request_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data[i][0])))
                self.ui.request_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data[i][1])))
                self.ui.request_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(data[i][2])))
                self.ui.request_table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(data[i][3])))
                self.ui.request_table.setItem(i, 4, QtWidgets.QTableWidgetItem(str(data[i][4])))

                btn = QtWidgets.QPushButton("Изменить")
                btn.setObjectName("upd_but")
                btn.setStyleSheet("background-color: rgb(85, 255, 127);")
                btn.clicked.connect(lambda checked, rid=data[i][0]: self.update_req(rid))

                self.ui.request_table.setCellWidget(i, 5, btn)


        except Exception as e:
            print(e)

    def update_req(self, rid: int):
        self.up = Update(rid)
        self.up.show()
