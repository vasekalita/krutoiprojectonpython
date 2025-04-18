from db import Database
from PyQt6 import QtWidgets
from pyform.log_form import Ui_Login_Form
from user import User
from admin import Admin

class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login_Form()
        self.ui.setupUi(self)

        self.db = Database()
        self.cursor = self.db.get_cursor()

        self.ui.pushButton.clicked.connect(self.open_form)

    def open_form(self):
        login = self.ui.login_line.text()
        password = self.ui.pas_line.text()

        self.cursor.execute(f"select id, login, password, role from users")
        data = self.cursor.fetchall()

        for i in data:
            if i[1] == login and i[2] == password and i[3] == "admin":
                self.open_admin()
                print("Вы админ")
                break
            if i[1] == login and i[2] == password and i[3] == "user":
                self.open_user(i[0])
                print("Вы пользователь")
                break
        else:
            print("Неверные данные")

    def open_user(self, user_id: int):
        self.us = User(user_id)
        self.us.show()
        self.close()

    def open_admin(self):
        self.ad = Admin()
        self.ad.show()
        self.close()


if __name__ == "__main__":
    import sys

app = QtWidgets.QApplication(sys.argv)
window = Login()
window.show()
sys.exit(app.exec())