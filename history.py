from pyform.history_form import Ui_History_Form
from db import Database
from PyQt6 import  QtWidgets

class History(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_History_Form()
        self.ui.setupUi(self)

        self.db = Database()
        self.cursor = self.db.get_cursor()

        self.ui.exit_but.clicked.connect(self.back)

        self.ui.history_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.cursor.execute("select id_req, request.type, old_value, new_value from history_request inner join request on request.id = history_request.id_req")
        data = self.cursor.fetchall()

        self.ui.history_table.setRowCount(len(data))

        try:
            for i in range(len(data)):
                self.ui.history_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data[i][0])))
                self.ui.history_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data[i][1])))
                self.ui.history_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(data[i][2])))
                self.ui.history_table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(data[i][3])))
        except Exception as e:
            print(e)


    def back(self):
        self.close()
