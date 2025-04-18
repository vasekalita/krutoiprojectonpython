from db import Database
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from pyform.user_form import Ui_User_Form
from history import History

class User(QtWidgets.QWidget):
    def __init__(self, user_id = None):
        super().__init__()
        self.ui = Ui_User_Form()
        self.ui.setupUi(self)
        self.user_id = user_id

        self.db = Database()
        self.cursor = self.db.get_cursor()

        self.ui.add_req.clicked.connect(self.add_request)
        self.ui.view_histor.clicked.connect(self.view_history)

    def add_request(self):
        type = self.ui.type_line.text()
        try:
            self.cursor.execute(f"insert into request(id_us, type, status, priorite) values ({int(self.user_id)}, '{str(type)}', 'На рассмотрении', 'Низкий')")
            self.db.connect.commit()
            QMessageBox.information(self, 'Успех', 'Заявка отправлена на рассмотрение')
        except Exception as e:
            print(e)

    def view_history(self):
        self.hi = History()
        self.hi.show()