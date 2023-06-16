import sqlite3
import json
import interface
from interface import *
class Properties:
    database_filename = ''

    def __init__(self, in_put=dict()):
        self.database_filename = in_put.get("database_filename")

with open('properties.json', 'r') as opened:
    properties = json.load(opened, object_hook=Properties)
json_object = json.dumps(properties.__dict__)
with open('properties.json', 'w') as to_write:
    to_write.write(json_object)
class Database:
    def __new__(cls):
        if not hasattr(Database, '_instance'):
            Database._instance = super().__new__(cls)
        return Database._instance
    def __init__(self):
        with open('properties.json', 'r') as openfile:
            self.properties = json.load(openfile, object_hook=Properties)

        db_filename = self.properties.database_filename
        self.connection = sqlite3.connect(db_filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                          id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                          name TEXT NOT NULL,
                          surname TEXT NOT NULL,
                          login TEXT UNIQUE NOT NULL,
                          password TEXT NOT NULL,
                          email TEXT,
                          status INTEGER,
                          birthdate TEXT,
                          orders TEXT,
                          adress_id INTEGER,
                          bill INTEGER);
                      """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS adresses(
                                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                  country TEXT NOT NULL,
                                  city TEXT NOT NULL,
                                  neighbourhood TEXT NOT NULL,
                                  house INTEGER NOT NULL,
                                  flat INTEGER NOT NULL);
                              """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
                                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                  sender_id INTEGER NOT NULL,
                                  adress_id INTEGER NOT NULL,
                                  status_id INTEGER);
                              """)

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS orderstatuses(
                                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                  status TEXT NOT NULL UNIQUE);
                              """)

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS userstatuses(
                                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                  status TEXT NOT NULL UNIQUE);
                              """)
        self.connection.commit()
    # Пользователь
    def get_all_users(self):
        self.cursor.execute('SELECT * FROM users')
        rows = self.cursor.fetchall()
        users = []
        for row in rows:
            user = interface.User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
            users.append(user)
        return users
    def add_new_user(self, user: interface.User):
        try:
            self.cursor.execute(
                "INSERT INTO users (name, surname, login, password, email, status, birthdate, orders, adress_id, bill) VALUES (?,?,?,?,?,?,?,?, ?, ?)",
                (user.name, user.surname, user.login, user.password, user.email, user.status, user.birthdate, user.orders, user.adress_id ,user.bill))
            self.connection.commit()
        except Exception as e:
            print(e)
    def delete_user(self, user: interface.User):
        try:
            self.cursor.execute("""DELETE FROM users WHERE login = ? AND password = ?""", (user.login, user.password))
            self.connection.commit()
            return 'Пользователь успешно удален'
        except Exception as s:
            print(s)
            return 'Возникла ошибка'
    def get_user_by_login_and_password(self, login: str, password: str):
        try:
            self.cursor.execute("""SELECT * FROM users WHERE login = ? AND password = ?""", (login, password))
            rows = self.cursor.fetchall()
            for row in rows:
                return interface.User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
            return interface.User(0, '-', '-', 'гость', '-', '-', 4, None, '', 0, 0)
        except Exception:
            print('Ошибка')
            return interface.User(0, '-', '-', 'гость', '-', '-', 4, None, '', 0, 0)
    def get_user_by_id(self, user_id: int):
        try:
            self.cursor.execute("""SELECT * FROM users WHERE id = ?""", (user_id,))
            row = self.cursor.fetchone()
            return interface.User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        except Exception as e:
            print(e)
            return interface.User(0, '-', '-', 'гость', '-', '-', 4, None, '', 0, 0)

    def get_all_statuses(self):
        try:
            self.cursor.execute("""SELECT * FROM userstatuses""")
            statuses = self.cursor.fetchall()
            return dict((id, tit) for tit, id in statuses)
        except Exception:
            return {}
    def get_status_by_login(self, login: str):
        try:
            self.cursor.execute("""SELECT * FROM userstatuses WHERE status = ?""", (login,))
            status = self.cursor.fetchone()
            return status[0]
        except Exception:
            return ''
    def get_status_by_id(self, id: int):
        try:
            self.cursor.execute("""SELECT * FROM userstatuses WHERE id = ?""", (id,))
            status = self.cursor.fetchone()
            return status[1]
        except Exception:
            return ''
    def update_user(self, what_to_redact: str, redacted_value: str, key: int):
        try:
            if what_to_redact == 'имя':
                self.cursor.execute("""UPDATE users SET name = ? WHERE id = ?""", (redacted_value, key))
            if what_to_redact == 'фамилия':
                self.cursor.execute("""UPDATE users SET surname = ? WHERE id = ?""", (redacted_value, key))
            if what_to_redact == 'логин':
                self.cursor.execute("""UPDATE users SET login = ? WHERE id = ?""", (redacted_value, key))
            if what_to_redact == 'пароль':
                self.cursor.execute("""UPDATE users SET password = ? WHERE id = ?""", (redacted_value, key))
            if what_to_redact == 'почта':
                self.cursor.execute("""UPDATE users SET email = ? WHERE id = ?""", (redacted_value, key))
            if what_to_redact == 'дата рождения':
                self.cursor.execute("""UPDATE users SET birthdate = ? WHERE id = ?""", (redacted_value, key))

            self.connection.commit()
        except Exception as e:
            print(e)
    # Адрес
    def get_all_adresses(self):
        try:
            self.cursor.execute("""SELECT * FROM adresses""")
            adresses = self.cursor.fetchall()
            adress_list = []
            for adress in adresses:
                adress_list.append(interface.Adress(adress))
            return adress_list
        except Exception as e:
            print(e)
            return []
    def get_adress_by_id(self, adress_id: int):
        try:
            self.cursor.execute("""SELECT * FROM adresses WHERE id = ?""", (adress_id,))
            return interface.Adress(self.cursor.fetchone())
        except Exception as e:
            print(e)
            return None
    def add_new_adress(self, adress: interface.Adress):
        try:
            self.cursor.execute(
                "INSERT INTO adresses (country, city, neighbourhood, house, flat) VALUES (?,?,?,?,?)",
                (adress.country, adress.city, adress.neighbourhood, adress.house, adress.flat))
            self.connection.commit()
        except Exception as e:
            print(e)
    def get_adressID_by_adress(self, adress: interface.Adress):
        try:
            self.cursor.execute("""SELECT * FROM adresses WHERE country = ? AND city = ? AND neighbourhood = ? AND house = ? AND flat = ?""", (adress.country, adress.city, adress.neighbourhood, adress.house, adress.flat))
            adress = interface.Adress(self.cursor.fetchone())
            return adress.id
        except Exception as e:
            print(e)
            return None
    # Заказ
    def get_all_user_orders(self, user: interface.User):
        try:
            self.cursor.execute("""SELECT * FROM orders WHERE adress_id = ?""", (user.adress_id,))
            rows = self.cursor.fetchall()
            orders = []
            for row in rows:
                orders.append(interface.Order(row))
            return orders
        except Exception as e:
            print(e)
    def get_order_by_id(self, order_id: int):
        try:
            self.cursor.execute("""SELECT * FROM orders WHERE id = ?""", (order_id,))
            row = self.cursor.fetchone()
            return interface.Order(row)
        except Exception as e:
            print(e)
    def add_new_order(self, order:interface.Order):
        try:
            self.cursor.execute(
                "INSERT INTO orders (sender_id, adress_id, status_id) VALUES (?,?,?)",
                (order.sender_id, order.reciever_adress_id, order.status_id))
            self.connection.commit()
        except Exception as e:
            print(e)


    def set_interface(self):
        window = Window(self)



d = Database()
d.set_interface()