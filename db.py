import pymysql
from pymysql import Error

class Database:
    def __init__(self):
        try:
            self.connect = pymysql.connect(host="localhost", user="root", password="root", database="kalash")
            print("Успешное подключение!")
        except Error as e:
            print(f"Ошибка подключения: {e}")

    def get_cursor(self):
        return self.connect.cursor()

    def close(self):
        if self.connect:
            self.connect.close()
            print("Соединие закрыто")