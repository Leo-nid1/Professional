import datetime
import sqlite3
import json
import time



class User:
    def __init__(self, userid: str, name: str, surname:str, login:str, password:str, email:str, status:int, birthdate:str):
        self.id = userid
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.email = email
        self.status = status
        self.birthdate = birthdate

    @property
    def id(self):
        return self.id
    @id.setter
    def id(self, intervalue):
        if type(intervalue) != int:
            raise TypeError()
        if intervalue < 1:
            raise ValueError()
        self.id = intervalue

    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, value):
        ok = True
        if type(value) != str:
            raise TypeError()
        symbols = 'абвгдежзийклмнопрстуфхцчшщьыъэюя_ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ1234567890'
        for i in value:
            if not i in symbols:
                ok = False
        if len(value) < 8:
            raise NotImplementedError()
        if ok:
            self._login = value
            return
        raise TypeError()

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        ok = True
        if type(value) != str:
            raise TypeError()
        SYMBOLS = 'абвгдежзийклмнопрстуфхцчшщьыъэюя_ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ1234567890'
        for i in value:
            if not i in SYMBOLS:
                ok = False
        if len(value) < 8:
            raise NotImplementedError()
        if ok:
            self._password = value
            return
        raise TypeError()

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if type(value) != str:
            raise TypeError('*_*')
        FORBIDDEN_SYMBOLS = ' !@#$%^&*()"№;:?<>,./|{}[]'
        for i in value:
            if i in FORBIDDEN_SYMBOLS:
                raise TypeError(f'Что это такое? -- {i}')
        if value[0].islower():
            raise TypeError('2 в журнал!')
        self._name = value

    @property
    def surname(self):
        return self._surname
    @surname.setter
    def surname(self, value):
        if type(value) != str:
            raise TypeError('*_*')
        FORBIDDEN_SYMBOLS = ' !@#$%^&*()"№;:?<>,./|{}[]'
        for i in value:
            if i in FORBIDDEN_SYMBOLS:
                raise TypeError(f'Что это такое? -- {i}')
        if value[0].islower():
            raise TypeError('2 в журнал!')
        self._surname = value

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        if value is None:
            self._birthdate = None
            return
        amount_of_dots = 0
        FORBIDDEN_SYMBOLS = ' !#$%^&*()"№;:?<>,/|{}[]'
        if len(value) < 9:
            raise ValueError()
        if type(value) != str:
            raise ValueError('o_o')
        if '@' not in value:
            raise ValueError("Это не почта!")
        for i in value:
            if '.' in value:
                amount_of_dots += 1
            if i in FORBIDDEN_SYMBOLS:
                raise ValueError('Точка, точка, запятая -- вышла рожица смешная')
        if amount_of_dots > 1:
            raise ValueError('Точка, точка, запятая -- вышла рожица смешная')
        if 3 <= len(value) - value.find('.') <= 4:
            self._email = value
        raise ValueError()

    @property
    def birthdate(self):
        return self._birthdate
    @birthdate.setter
    def birthdate(self, value):
        if value is None:
            self._birthdate = None
            return
        if type(value) != str:
            raise TypeError()
        nums = list(map(int, value.split('-')))
        if len(nums) < 3:
            raise ValueError()
        date = datetime.datetime.date(nums[0], nums[1], nums[2])
        if date < datetime.datetime.now():
            raise ValueError()
        self._birthdate = value

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        if type(value) != int:
            raise TypeError()
        if value < 1:
            raise ValueError()
        self._status = value


    def __str__(self):
        return f'Пользователь {self._surname} {self._name}'
    def __repr__(self):
        return f'Пользователь {self._surname} {self._name}'











class Database():
    def __new__(cls):
        if not hasattr(Database, '_instance'):
            Database._instance = super().__new__(cls)
        return Database._instance

    def __init__(self):
        db_filename = 'wait_a_year.db'
        self.connection = sqlite3.connect(db_filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                  name TEXT NOT NULL,
                  surname TEXT NOT NULL,
                  login TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL,
                  email TEXT);
              """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS adresses(
                          id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                          country TEXT NOT NULL,
                          city TEXT NOT NULL,
                          neighbourhood TEXT NOT NULL,
                          house TEXT NOT NULL,
                          flat int NOT NULL);
                      """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
                          id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                          sender_id TEXT NOT NULL,
                          adress TEXT NOT NULL,
                          info TEXT NOT NULL);
                      """)
        # self.cursor.execute("""ALTER TABLE users ADD COLUMN status INTEGER""")
        # self.cursor.execute("""ALTER TABLE orders ADD COLUMN status INTEGER""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS orderstatuses(
                          id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                          status TEXT NOT NULL UNIQUE);
                      """)

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS userstatuses(
                          id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                          status TEXT NOT NULL UNIQUE);
                      """)
  #       self.cursor.execute(f"""INSERT INTO users (name, surname, login, password, email, status)
  # VALUES ( 'Семен', 'Дежнев', 'Путешественник', '123454679', 'netpochty@mail.ru', {2});""")

        #self.cursor.execute("""ALTER TABLE users ADD COLUMN birthdate text""")
        self.connection.commit()

    def get_all_users(self):
        self.cursor.execute('SELECT * FROM users')
        rows = self.cursor.fetchall()
        users = []
        for row in rows:
            user = User(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
            users.append(user)
        return users




class Adress:
    def __init__(self, info:tuple):
        self.id = info[0]
        self.country = info[1]
        self.city =info[2]
        self.neighbourhood = info[3]
        self.house = info[4]
        self.flat = info[5]
class Order:
    def __init__(self):
        pass

class Properties:
    database_filename = ''

    def __init__(self, in_put=dict()):
        self.database_filename = in_put.get("database_filename")

with open('properties.json', 'r') as opened:
    properties = json.load(opened, object_hook=Properties)
json_object = json.dumps(properties.__dict__)
with open('properties.json', 'w') as to_write:
    to_write.write(json_object)

# class Cat:
#     def __init__(self):
#         self.name = 'cat'
#         self.sound = 'Miaw'
#         self.legs_amount = 4
# with open('cat.json', 'w') as writttte:
#     writttte.write(json.dumps(Cat().__dict__))


d = Database()
print(d.get_all_users())