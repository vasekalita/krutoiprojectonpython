from db import Database
from PyQt6 import QtWidgets
from pyform.update_form import Ui_Update_Form

class Update(QtWidgets.QWidget):
    def __init__(self, request_id = None):
        super().__init__()
        self.ui = Ui_Update_Form()
        self.ui.setupUi(self)
        self.request_id = request_id

        self.db = Database()
        self.cursor = self.db.get_cursor()

        self.ui.status_combo.addItem("На рассмотрении")
        self.ui.status_combo.addItem("Одобрена")
        self.ui.status_combo.addItem( "Отклонено")

        self.ui.priotitet_combo.addItem("Низкий")
        self.ui.priotitet_combo.addItem("Наивысший")

        self.cursor.execute(f"select *from request where id = {self.request_id}")
        data = self.cursor.fetchone()

        self.ui.id_req_label.setText(str(data[0]))
        self.ui.id_user_label.setText(str(data[1]))
        self.ui.type_label.setText(str(data[2]))
        self.ui.status_combo.setCurrentText(data[3])
        self.ui.priotitet_combo.setCurrentText(data[4])

        self.ui.update_but.clicked.connect(self.update_req)

    def update_req(self):
        try:
            status = self.ui.status_combo.currentText()
            prioritet = self.ui.priotitet_combo.currentText()
            self.cursor.execute(f"update request set status = '{status}', priorite = '{prioritet}' where id = {self.request_id}")
            self.db.connect.commit()
            QtWidgets.QMessageBox.information(self, "Успех", "Данные успешно обновлены!")
            self.close()
        except Exception as e:
            print(e)

