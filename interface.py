from tkinter import *
from tkinter import ttk
import datetime
import re

class User:
    def __init__(self, userid: int, name: str, surname: str, login: str, password: str, email: str, status: int, birthdate, orders: str, adress_id: int, bill: int):
        self.id = userid
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.email = email
        self.status = status
        self.birthdate = birthdate
        self._orders = orders
        self._adress_id = adress_id
        self._bill = bill


    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, intervalue):
        if type(intervalue) != int:
            raise TypeError()
        if intervalue < 0:
            raise ValueError()
        self._id = intervalue

    @property
    def login(self):
        return self._login
    @login.setter
    def login(self, value):
        ok = True
        if type(value) != str:
            raise TypeError()
        symbols = 'абвгдежзийклмнопрстуфхцчшщьыъэюя_ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ1234567890-'
        for i in value:
            if i not in symbols:
                ok = False
        if len(value) < 8 and value != 'гость':
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
        SYMBOLS = 'абвгдежзийклмнопрстуфхцчшщьыъэюя_ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ1234567890-'
        for i in value:
            if not i in SYMBOLS:
                ok = False
        if len(value) < 8 and value != '-':
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
        FORBIDDEN_SYMBOLS = ' !@#$%^&*()"№;:?<>,./|{}[]+='
        for i in value:
            if i in FORBIDDEN_SYMBOLS:
                raise TypeError(f'Что это такое? -- {i}')
        if value[0].islower() and value != '-':
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
        if value[0].islower() and value != '-':
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
        if len(value) < 9 and value != '-':
            raise ValueError()
        if type(value) != str:
            raise ValueError('o_o')
        if '@' not in value and value != '-':
            raise ValueError("Это не почта!")
        for i in value:
            if i == '.' :
                amount_of_dots += 1
            if i in FORBIDDEN_SYMBOLS:
                raise ValueError('Точка, точка, запятая -- вышла рожица смешная')
        if amount_of_dots > 1:
            raise ValueError('Точка, точка, запятая -- вышла рожица смешная')

        self._email = value

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
        self._birthdate = value

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value: int):
        if type(value) != int:
            raise TypeError()
        if value < 1:
            raise ValueError()
        self._status = value

    @property
    def bill(self):
        return self._bill
    @bill.setter
    def bill(self, value):
        if type(value) != int:
            raise TypeError('Не число')
        if value < 0:
            raise ValueError('Мы пока не принимаем пожертвования')
        self._bill = value

    @property
    def adress_id(self):
        return self._adress_id
    @adress_id.setter
    def adress_id(self, value):
        if type(value) != int:
            raise TypeError()
        if value < 0:
            raise ValueError()
        self._adress_id = value

    @property
    def orders(self):
        return self._orders
    @orders.setter
    def orders(self, value):
        FORBIDDEN_SYMBOLS = "_=+)(*&^%$#@!;:'/|.,<>{}[]~`"
        if type(value) != str:
            raise TypeError()
        for i in value:
            if value in FORBIDDEN_SYMBOLS:
                raise ValueError()
        self._orders = value







    def __str__(self):
        return f'Пользователь {self._surname} {self._name}'

    def __repr__(self):
        return f'Пользователь {self._surname} {self._name}'

class Adress:
    def __init__(self, info: tuple):
        self.id = info[0]
        self.country = info[1]
        self.city = info[2]
        self.neighbourhood = info[3]
        self.house = info[4]
        self.flat = info[5]

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        if type(value) != int:
            raise TypeError('НеЧисло')
        if value < 0:
            raise ValueError('Отрицательный ID')
        self._id = value

    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, value):
        FORBIDDEN_SYMBOLS = "1234567890_=+)(*&^%$#@!;:'/|.,<>{}[]~`"
        if type(value) != str:
            raise TypeError('Название страны -- не число')
        if value[0].islower():
            raise ValueError(' 2 в журнал!')
        if len(value) <= 1:
            raise ValueError(' Слишком коротко ')
        for i in value:
            if i in FORBIDDEN_SYMBOLS:
                raise ValueError('Непонятности...')
        self._country = value

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, value):
        FORBIDDEN_SYMBOLS = "1234567890_=+)(*&^%$#@!;:'/|.,<>{}[]~`"
        if type(value) != str:
            raise TypeError('Название города -- не число')
        if value[0].islower():
            raise ValueError(' 2 в журнал!')
        for i in value:
            if i in FORBIDDEN_SYMBOLS:
                raise ValueError('Непонятности...')
        self._city = value

    @property
    def neighbourhood(self):
        return self._neighbourhood
    @neighbourhood.setter
    def neighbourhood(self, value):
        FORBIDDEN_SYMBOLS = "1234567890_=+)(*&^%$#@!;:'/|.,<>{}[]~`"
        if type(value) != str:
            raise TypeError('Название района -- не число')
        if value[0].islower():
            raise ValueError(' 2 в журнал!')
        for i in value:
            if i in FORBIDDEN_SYMBOLS:
                raise ValueError('Непонятности...')
        self._neighbourhood = value

    @property
    def house(self):
        return self._house
    @house.setter
    def house(self, value):
        if type(value) != int:
            raise TypeError('Номер дома должен быть числом')
        if value < 0:
            raise ValueError('Отрицательный номер дома')
        self._house = value

    @property
    def flat(self):
        return self._flat
    @flat.setter
    def flat(self, value):
        if type(value) != int:
            raise TypeError('Номер квартиры должен быть числом')
        if value < 0:
            raise ValueError('Отрицательный номер квартиры')
        self._flat = value








class Order:
    def __init__(self, info: tuple):
        self._id = info[0]
        self._sender_id = info[1]
        self._reciever_adress_id = info[2]
        self._status_id = info[3]

    @property
    def sender_id(self):
        return self._sender_id
    @sender_id.setter
    def sender_id(self, value):
        if type(value) != int:
            raise TypeError()
        if value < 1:
            raise  ValueError()
        self._sender_id = value

    @property
    def reciever_adress_id(self):
        return self._reciever_adress_id
    @reciever_adress_id.setter
    def reciever_adress_id(self, value):
        if type(value) != int:
            raise TypeError()
        if value < 1:
            raise ValueError()
        self._reciever_adress_id = value

    @property
    def status_id(self):
        return self._status_id
    @status_id.setter
    def status_id(self, value):
        if type(value) != int:
            raise TypeError()
        if value < 1:
            raise ValueError()
        self._status_id = value

    def __repr__(self):
        return f'от (ID) {self.sender_id}'
    def __str__(self):
        return f'от {self.sender_id}'


class Window(Tk):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.title("Самая 'быстрая' почта")
        self.geometry('+300+100')
        self.add_user_func = self.data.add_new_user
        self.load_users_func = self.data.get_all_users
        self.get_all_statuses_function = self.data.get_all_statuses
        self.get_status_id_function = self.data.get_status_by_login
        self.get_status_function = self.data.get_status_by_id
        self.authentication_function = self.data.get_user_by_login_and_password
        self.delete_user_function = self.data.delete_user
        self.edit_user_function = self.data.update_user

        self.statuslist = list(self.get_all_statuses_function().keys())
        self.default_user = User(0, '-', '-', 'гость', '-', '-', 4, None, '', 0, 0)
        self.user = self.default_user
        self.redacted_user = self.default_user

        notebook = ttk.Notebook()
        notebook.pack(expand=True, fill=BOTH)
        frame_1 = ttk.Frame(notebook)
        frame_1.pack()
        notebook.add(frame_1, text='Просмотр пользователей')
        frame_2 = ttk.Frame()
        frame_2.pack()
        notebook.add(frame_2, text='Зарегестрироваться')
        frame_3 = ttk.Frame()
        frame_3.pack()
        notebook.add(frame_3, text='Войти')
        frame_4 = ttk.Frame()
        frame_4.pack()
        notebook.add(frame_4, text='Личный кабинет')
        self.frame_5 = ttk.Frame()
        self.frame_5.pack()
        notebook.add(self.frame_5, text='Редактировать профиль')
        self.frame_6 = ttk.Frame()
        self.frame_6.pack()
        notebook.add(self.frame_6, text='Посылки')


        self.authentication_label = Label(text='Войти', master=frame_3)
        self.authentication_label.grid(row=0, column=2, padx=3, pady=6)

        self.authentication_login_label = Label(text='Логин:', master=frame_3)
        self.authentication_login_label.grid(row=1, column=1, padx=3, pady=3)
        self.authentication_login_entry = ttk.Entry(master=frame_3)
        self.authentication_login_entry.grid(row=1, column=2, padx=3, pady=3)
        self.authentication_login_error = Label(master=frame_3)
        self.authentication_login_error.grid(row=1, column=3, padx=3, pady=3)
        self.authentication_login_entry.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[А-ЯЁа-яё]{8,}', self.authentication_login_error)), '%P'))

        self.authentication_password_label = Label(text='Пароль:', master=frame_3)
        self.authentication_password_label.grid(row=2, column=1, padx=3, pady=3)
        self.authentication_password_input = ttk.Entry(master=frame_3)
        self.authentication_password_input.grid(row=2, column=2, padx=3, pady=3)
        self.authentication_password_error = Label(master=frame_3)
        self.authentication_password_error.grid(row=2, column=3, padx=3, pady=3)
        self.authentication_password_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[А-ЯЁа-яё0-9]{8,}$', self.authentication_password_error)), '%P'))

        self.authentication_button = ttk.Button(text='Войти', master=frame_3, command=self.authenticate)
        self.authentication_button.grid(row=3, column=2, padx=3, pady=3) # Авторизация
        self.heading_label = Label(text='Таблица пользователей', master=frame_1, padx=3, pady=3)
        self.heading_label.pack(side=TOP)
        columns = ['идентификатор', 'имя', 'фамилия', 'имя пользователя', 'пароль', 'почта', 'статус', 'дата рождения']
        self.user_table = ttk.Treeview(columns=columns, show='headings', master=frame_1)
        self.user_table.pack(fill=BOTH, expand=True)
        columns_names = ['идентификатор', 'имя', 'фамилия', 'имя пользователя', 'пароль', 'почта', 'статус', 'дата рождения']
        columns_width = [130, 100, 80, 120, 120, 100, 100, 100]
        for i in range(len(columns)):
            self.user_table.heading(columns[i], text=columns_names[i])
            self.user_table.column(f'#{i}', stretch=NO, width=columns_width[i])


        horizontal_scrollbar = ttk.Scrollbar(orient=HORIZONTAL, command=self.user_table.xview(), master=frame_1)
        self.user_table.configure(xscrollcommand=horizontal_scrollbar.set)
        horizontal_scrollbar.pack(side=BOTTOM, fill=X)

        vertical_scrollbar = ttk.Scrollbar(orient=VERTICAL, command=self.user_table.yview(), master=frame_1)
        self.user_table.configure(yscrollcommand=vertical_scrollbar.set)
        vertical_scrollbar.pack(side=RIGHT, fill=Y)

        self.load_user_button = ttk.Button(text='Обновить', command=self.load_user_list, master=frame_1)
        self.load_user_button.pack(side=BOTTOM, anchor=S)

         # Отображение пользователей
        self.add_user_label = Label(text='Добавление пользователя', master=frame_2)
        self.add_user_label.grid(row=0, column=0, columnspan=3, padx=3, pady=3)

        self.login_label = Label(text='Логин*:', master=frame_2)
        self.login_label.grid(row=1, column=0, padx=3, pady=3)
        self.login_input = ttk.Entry(master=frame_2)
        self.login_input.grid(row=1, column=1, padx=3, pady=3)
        self.login_error = Label(master=frame_2)
        self.login_error.grid(row=1, column=2, padx=3, pady=3)
        self.login_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'[А-ЯЁа-яё]{8,}', self.login_error)), '%P'))

        self.password_label = Label(text='Пароль*:', master=frame_2)
        self.password_label.grid(row=2, column=0, padx=3, pady=3)
        self.password_input = ttk.Entry(master=frame_2)
        self.password_input.grid(row=2, column=1, padx=3, pady=3)
        self.password_error = Label(master=frame_2)
        self.password_error.grid(row=2, column=2, padx=3, pady=3)
        self.password_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[А-ЯЁа-яё0-9]{8,}$', self.password_error)), '%P'))


        self.name_label = Label(text='Имя*:', master=frame_2)
        self.name_label.grid(row=3, column=0, padx=3, pady=3)
        self.name_input = ttk.Entry(master=frame_2)
        self.name_input.grid(row=3, column=1, padx=3, pady=3)
        self.name_error = Label(master=frame_2)
        self.name_error.grid(row=3, column=2, padx=3, pady=3)
        self.name_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[А-ЯЁа-яё]*|[A-Za-z]*)$', self.name_error)), '%P'))

        self.surname_label = Label(text='Фамилия*:', master=frame_2)
        self.surname_label.grid(row=4, column=0, padx=3, pady=3)
        self.surname_input = ttk.Entry(master=frame_2)
        self.surname_input.grid(row=4, column=1, padx=3, pady=3)
        self.surname_error = Label(master=frame_2)
        self.surname_error.grid(row=4, column=2, padx=3, pady=3)
        self.surname_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[А-ЯЁа-яё]*|[A-Za-z]*)$', self.surname_error)), '%P'))


        self.email_label = Label(text='Электронная почта:', master=frame_2)
        self.email_label.grid(row=5, column=0, padx=3, pady=3)
        self.email_input = ttk.Entry(master=frame_2)
        self.email_input.grid(row=5, column=1, padx=3, pady=3)
        self.email_error = Label(master=frame_2)
        self.email_error.grid(row=5, column=2, padx=3, pady=3)
        self.email_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[0-9a-zа-яА-Я]{5,}[@][a-z]{0,7}[.][a-z]{2,3}$', self.email_error)), '%P'))


        self.birthdate_label = Label(text='Дата рождения:', master=frame_2)
        self.birthdate_label.grid(row=6, column=0, padx=3, pady=3)
        self.birthdate_input = ttk.Entry(master=frame_2)
        self.birthdate_input.grid(row=6, column=1, padx=3, pady=3)
        self.birthdate_error = Label(master=frame_2)
        self.birthdate_error.grid(row=6, column=2, padx=3, pady=3)
        self.email_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^(?:[1][9]|[2][0-1])[0-9]{2}[-](?:[1][1-9]|[2][0-2])[-][0-3][0-1]$', self.email_error)), '%P'))


        self.status_label = Label(text='Статус:', master=frame_2)
        self.status_label.grid(row=7, column=0, padx=3, pady=3)
        self.status_input = ttk.Combobox(values=self.statuslist, master=frame_2)
        self.status_input.grid(row=7, column=1, padx=3, pady=3)
        self.status_error = Label(master=frame_2)
        self.status_error.grid(row=7, column=2, padx=3, pady=3)
        self.email_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[0-9]{0,1}$', self.email_error)), '%P'))




        self.adress_heading = Label(text='Адрес (адрес нельзя будет изменить)', master=frame_2)
        self.adress_heading.grid(row=0, column=5, padx=3, pady=3)

        self.country_label = Label(text='Страна:', master=frame_2)
        self.country_label.grid(row=1, column=5, padx=3, pady=3)
        self.country_input = ttk.Entry(master=frame_2)
        self.country_input.grid(row=1, column=6, padx=3, pady=3)
        self.country_error = Label(master=frame_2)
        self.country_error.grid(row=1, column=7, padx=3, pady=3)
        self.country_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[А-Я]{0,1}[а-я]{0,}$', self.country_error)), '%P'))

        self.city_label = Label(text='Город:', master=frame_2)
        self.city_label.grid(row=2, column=5, padx=3, pady=3)
        self.city_input = ttk.Entry(master=frame_2)
        self.city_input.grid(row=2, column=6, padx=3, pady=3)
        self.city_error = Label(master=frame_2)
        self.city_error.grid(row=2, column=7, padx=3, pady=3)
        self.city_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[А-Я]{1}[а-я]{0,}$', self.city_error)), '%P'))

        self.neighbourhood_label = Label(text='Район:', master=frame_2)
        self.neighbourhood_label.grid(row=3, column=5, padx=3, pady=3)
        self.neighbourhood_input = ttk.Entry(master=frame_2)
        self.neighbourhood_input.grid(row=3, column=6, padx=3, pady=3)
        self.neighbourhood_error = Label(master=frame_2)
        self.neighbourhood_error.grid(row=3, column=7, padx=3, pady=3)
        self.neighbourhood_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[А-Я]{0,1}[а-я]{0,}$', self.neighbourhood_error)), '%P'))

        self.house_label = Label(text='Дом:', master=frame_2)
        self.house_label.grid(row=4, column=5, padx=3, pady=3)
        self.house_input = ttk.Entry(master=frame_2)
        self.house_input.grid(row=4, column=6, padx=3, pady=3)
        self.house_error = Label(master=frame_2)
        self.house_error.grid(row=4, column=7, padx=3, pady=3)
        self.house_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[0-9]{1,}$', self.house_error)), '%P'))

        self.flat_label = Label(text='Квартира:', master=frame_2)
        self.flat_label.grid(row=5, column=5, padx=3, pady=3)
        self.flat_input = ttk.Entry(master=frame_2)
        self.flat_input.grid(row=5, column=6, padx=3, pady=3)
        self.flat_error = Label(master=frame_2)
        self.flat_error.grid(row=5, column=7, padx=3, pady=3)
        self.flat_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value,  r'^[0-9]{1,}$', self.house_error)), '%P'))





        self.add_user_button = ttk.Button(text='Добавить пользователя', command=self.add_user, master=frame_2)
        self.add_user_button.grid(row=8, column=1, padx=3, pady=3) # Регистрация

        self.lk_heading_label = Label(text=f'', master=frame_4)
        self.lk_id_label = Label(text=f'', master=frame_4)
        self.lk_name_label = Label(text=f'', master=frame_4)
        self.lk_surname_label = Label(text=f'', master=frame_4)
        self.lk_login_label = Label(text=f'', master=frame_4)
        self.lk_password_label = Label(text=f'', master=frame_4)
        self.lk_email_label = Label(text=f'', master=frame_4)
        self.lk_status_label = Label(text=f'', master=frame_4)
        self.lk_birthdate_label = Label(text=f'', master=frame_4)

        self.lk_adress_label = Label(text=f'', master=frame_4)
        self.lk_country_label = Label(text=f'', master=frame_4)
        self.lk_city_label = Label(text=f'', master=frame_4)
        self.lk_neighbourhood_label = Label(text=f'', master=frame_4)
        self.lk_house_label = Label(text=f'', master=frame_4)
        self.lk_flat_label = Label(text=f'', master=frame_4)





        self.lk_exit_button = ttk.Button(master=frame_4, text='')
        self.user_delete_button = ttk.Button(master=frame_4, text='') # Личный кабинет
 # Личный кабинет



        self.update_()
        self.mainloop()
    def sort_self_orders(self):
        list1 = []
        list2 = []
        all_user_orders = self.data.get_all_user_orders(self.user)
        for order in all_user_orders:
            if order.status_id == 1:
                list1.append(f'{order}, ')
            if order.status_id == 2:
                list2.append(f'{order}, ')
        return [list1, list2]

    def frame_6_update(self):
        for label in self.frame_6.winfo_children():
            label.destroy()
        if self.user.status == 4:
            self.pachage_error_heading = Label(master=self.frame_6, text='Вы не авторизованы!')
            self.pachage_error_heading.grid(row=0, column=1, padx=3, pady=3)
        else:
            self.package_heading = Label(master=self.frame_6, text='Это ваш "почтовый ящик. Здесь вы можете принимать и отправлять посылки"')
            self.package_list_title = Label(master=self.frame_6,text=f'Посылки, которые скоро придут: {self.sort_self_orders()[0]}')
            self.package_list_title_v2 = Label(master=self.frame_6,text=f'Посылки, которые уже пришли: {self.sort_self_orders()[1]}')
            self.package_heading.grid(row=0, column=0, padx=3, pady=3)
            self.package_list_title.grid(row=1, column=0, padx=3, pady=3)
            self.package_list_title_v2.grid(row=2, column=0, padx=3, pady=3)
            self.send_package_option = ttk.Button(master=self.frame_6, text='Отправить посылку', command=self.frame_6_send_package)
            self.send_package_option.grid(row=3, column=0, padx=3, pady=3)

    def frame_6_send_package(self):
        self.sending_heading_label = Label(master=self.frame_6, text='Введите адрес получателя:')
        self.sending_heading_label.grid(row=3, column=1, padx=3, pady=3)

        self.order_country_label = Label(text='Страна:', master=self.frame_6)
        self.order_country_label.grid(row=4, column=0, padx=3, pady=3)
        self.order_country_input = ttk.Entry(master=self.frame_6)
        self.order_country_input.grid(row=4, column=1, padx=3, pady=3)
        self.order_country_error = Label(master=self.frame_6)
        self.order_country_error.grid(row=4, column=2, padx=3, pady=3)
        self.order_country_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[А-Я]{0,1}[а-я]{0,}$', self.order_country_error)), '%P'))

        self.order_city_label = Label(text='Город:', master=self.frame_6)
        self.order_city_label.grid(row=5, column=0, padx=3, pady=3)
        self.order_city_input = ttk.Entry(master=self.frame_6)
        self.order_city_input.grid(row=5, column=1, padx=3, pady=3)
        self.order_city_error = Label(master=self.frame_6)
        self.order_city_error.grid(row=5, column=2, padx=3, pady=3)
        self.order_city_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[А-Я]{1}[а-я]{0,}$', self.order_city_error)), '%P'))

        self.order_neighbourhood_label = Label(text='Район:', master=self.frame_6)
        self.order_neighbourhood_label.grid(row=6, column=0, padx=3, pady=3)
        self.order_neighbourhood_input = ttk.Entry(master=self.frame_6)
        self.order_neighbourhood_input.grid(row=6, column=1, padx=3, pady=3)
        self.order_neighbourhood_error = Label(master=self.frame_6)
        self.order_neighbourhood_error.grid(row=6, column=2, padx=3, pady=3)
        self.order_neighbourhood_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[А-Я]{0,1}[а-я]{0,}$', self.order_neighbourhood_error)), '%P'))

        self.order_house_label = Label(text='Дом:', master=self.frame_6)
        self.order_house_label.grid(row=7, column=0, padx=3, pady=3)
        self.order_house_input = ttk.Entry(master=self.frame_6)
        self.order_house_input.grid(row=7, column=1, padx=3, pady=3)
        self.order_house_error = Label(master=self.frame_6)
        self.order_house_error.grid(row=7, column=2, padx=3, pady=3)
        self.order_house_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[0-9]{1,}$', self.order_house_error)), '%P'))

        self.order_flat_label = Label(text='Квартира:', master=self.frame_6)
        self.order_flat_label.grid(row=8, column=0, padx=3, pady=3)
        self.order_flat_input = ttk.Entry(master=self.frame_6)
        self.order_flat_input.grid(row=8, column=1, padx=3, pady=3)
        self.order_flat_error = Label(master=self.frame_6)
        self.order_flat_error.grid(row=8, column=2, padx=3, pady=3)
        self.order_flat_input.configure(validate='focusout', validatecommand=(self.register(
            lambda value: self.validator(value, r'^[0-9]{1,}$', self.order_flat_error)), '%P'))



        self.order_create_button = ttk.Button(master=self.frame_6, text='Отправить', command=self.create_order)
        self.order_create_button.grid(row=9, column=0, padx=3, pady=3)





    def frame_5_update(self):
        for label in self.frame_5.winfo_children():
            label.destroy()
        self.input_values = [f'имя', f'фамилия', f'логин', f'пароль', f'почта', f'дата рождения']
        self.edit_user_heading = Label(master=self.frame_5,text=f'Редактировать профиль пользователя {self.user.login}')
        self.edit_user_heading2 = Label(master=self.frame_5, text=f'Выберите параметр, который хотите отредактировать:')
        self.edit_user_variety = ttk.Combobox(master=self.frame_5, values=self.input_values)
        self.edit_user_label = Label(master=self.frame_5, text='Введите новое значение:')
        self.edit_user_entry = ttk.Entry(master=self.frame_5)
        self.edit_error_label = Label(master=self.frame_5, text='')
        self.edit_user_button = ttk.Button(master=self.frame_5, text='Изменить', command=self.edit_user)
        self.user_edit_error_heading = Label(master=self.frame_5, text=f'Вы не авторизованы!')
        self.order_error_label = Label(master=self.frame_6, text='')
        if self.user.status == 4:
            self.user_edit_error_heading.grid(row=0, column=0, padx=3, pady=3)
        else:
            self.edit_user_heading.grid(row=0, column=0, padx=3, pady=3)
            self.edit_user_heading2.grid(row=1, column=0, padx=3, pady=3)
            self.edit_user_variety.grid(row=2, column=0, padx=3, pady=3)
            self.edit_user_label.grid(row=3, column=0, padx=3, pady=3)
            self.edit_user_entry.grid(row=4, column=0, padx=3, pady=3)
            self.edit_error_label.grid(row=4, column=1, padx=3, pady=3)
            self.edit_user_button.grid(row=5, column=0, padx=3, pady=3)

    def update_frame_4(self):
        self.lk_heading_label.configure(text='')
        self.lk_id_label.configure(text='')
        self.lk_name_label.configure(text='')
        self.lk_surname_label.configure(text='')
        self.lk_login_label.configure(text='')
        self.lk_password_label.configure(text='')
        self.lk_email_label.configure(text='')
        self.lk_status_label.configure(text='')
        self.lk_birthdate_label.configure(text='')

        self.lk_adress_label.configure(text='')
        self.lk_country_label.configure(text='')
        self.lk_city_label.configure(text='')
        self.lk_neighbourhood_label.configure(text='')
        self.lk_house_label.configure(text='')
        self.lk_flat_label.configure(text='')

        if self.user.status == 4:
            self.lk_heading_label.configure(text='Вы не авторизованы!')
            self.lk_exit_button.configure(text='Не доступно', command=None)
            self.user_delete_button.configure(text='Не доступно', command=None)
        else:
            self.lk_exit_button.configure(text='Выйти', command=self.exit_lk)
            self.user_delete_button.configure(text='Удалить', command=self.delete_user)

            self.lk_heading_label.configure(text=f'Личный кабинет пользователя {self.user.login}')
            self.lk_id_label.configure(text=f' Идентификатор:    {self.user.id}')
            self.lk_name_label.configure(text=f' Имя:    {self.user.name}')
            self.lk_surname_label.configure(text=f' Фамилия:    {self.user.surname}')
            self.lk_login_label.configure(text=f' Имя пользователя:    {self.user.login}')
            self.lk_password_label.configure(text=f' Пароль:    {self.user.password}')
            self.lk_email_label.configure(text=f' Почта:    {self.user.email}')
            self.lk_status_label.configure(text=f' Статус:    {self.user.status}')
            self.lk_birthdate_label.configure(text=f' Дата рождения:    {self.user.birthdate}')


            adress = self.data.get_adress_by_id(self.user.adress_id)

            self.lk_adress_label.configure(text='Адрес:')
            self.lk_country_label.configure(text=f'Страна: {adress.country}')
            self.lk_city_label.configure(text=f'Город: {adress.city}')
            self.lk_neighbourhood_label.configure(text=f'Район: {adress.neighbourhood}')
            self.lk_house_label.configure(text=f'Дом: {adress.house}')
            self.lk_flat_label.configure(text=f'Квартира: {adress.flat}')


        self.lk_heading_label.grid(row=0, column=3, padx=3, pady=3)

        self.lk_exit_button.grid(row=1, column=1, padx=3, pady=3)
        self.user_delete_button.grid(row=1, column=2, padx=3, pady=3)

        self.lk_id_label.grid(row=2, column=3, padx=3, pady=3)
        self.lk_name_label.grid(row=3, column=3, padx=3, pady=3)
        self.lk_surname_label.grid(row=4, column=3, padx=3, pady=3)
        self.lk_login_label.grid(row=5, column=3, padx=3, pady=3)
        self.lk_password_label.grid(row=6, column=3, padx=3, pady=3)
        self.lk_email_label.grid(row=7, column=3, padx=3, pady=3)
        self.lk_status_label.grid(row=8, column=3, padx=3, pady=3)
        self.lk_birthdate_label.grid(row=9, column=3, padx=3, pady=3)
        self.lk_adress_label.grid(row=0, column=4, padx=3, pady=3)
        self.lk_country_label.grid(row=1, column=4, padx=3, pady=3)
        self.lk_city_label.grid(row=2, column=4, padx=3, pady=3)
        self.lk_neighbourhood_label.grid(row=3, column=4, padx=3, pady=3)
        self.lk_house_label.grid(row=4, column=4, padx=3, pady=3)
        self.lk_flat_label.grid(row=5, column=4, padx=3, pady=3)

    def update_(self):
        self.load_user_list()
        self.frame_5_update()
        self.update_frame_4()
        self.frame_6_update()



    def create_order(self):
        country = self.order_country_input.get()
        city = self.order_city_input.get()
        neighbourhood = self.order_neighbourhood_input.get()
        house = self.order_house_input.get()
        flat = self.order_flat_input.get()
        if house.isnumeric():
            if flat.isnumeric():
                adress = Adress((0, country, city, neighbourhood, int(house), int(flat)))
                self.adress_id = self.data.get_adressID_by_adress(adress)
                if self.adress_id is not None:
                    order = Order((0, self.user.id, self.adress_id, 1))
                    self.data.add_new_order(order)
                    self.user.bill += 100
                    self.update_()
                else:
                    self.order_error_label.destroy()
                    self.order_error_label = Label(master=self.frame_6, text='Вы неправильно ввели адрес')
                    self.order_error_label.grid(row=10, column=0, padx=3, pady=3)
            else:
                self.order_error_label.destroy()
                self.order_error_label = Label(master=self.frame_6, text='Номер квартиры -- число!')
                self.order_error_label.grid(row=10, column=0, padx=3, pady=3)
        else:
            self.order_error_label.destroy()
            self.order_error_label = Label(master=self.frame_6, text='Номер дома -- число!')
            self.order_error_label.grid(row=10, column=0, padx=3, pady=3)


    def exit_lk(self):
        self.user = self.default_user
        self.update_()

    def add_user(self):
        name = self.name_input.get()
        surname = self.surname_input.get()
        login = self.login_input.get()
        password = self.password_input.get()
        email = self.email_input.get() if self.email_input.get() != '' else None
        birthdate = self.birthdate_input.get() if self.birthdate_input.get() != '' else None
        status = self.get_status_id_function(self.status_input.get())


        country = self.country_input.get()
        city = self.city_input.get()
        neighbourhood = self.neighbourhood_input.get()
        house = self.house_input.get()
        flat = self.flat_input.get()
        if house.isnumeric():
            house = int(house)
        if flat.isnumeric():
            flat = int(flat)

        adress = Adress((0, country, city, neighbourhood, house, flat))
        self.data.add_new_adress(adress)
        adress_id = self.data.get_adressID_by_adress(adress)


        user = User(1, name, surname, login, password, email, status, birthdate, '', adress_id, 0)
        self.user = user
        self.add_user_func(user)

        self.update_()

    def delete_user(self):
        user = self.user
        self.user = self.default_user
        if user != self.default_user:
            self.delete_user_function(user)
        self.update_()

    def edit_user(self):
        input_variety = self.edit_user_variety.get()
        entry = self.edit_user_entry.get()
        self.edit_user_function(input_variety, entry, self.user.id)
        self.user = self.data.get_user_by_id(self.user.id)
        self.update_()

    def load_user_list(self):
        users = self.load_users_func()
        for i in self.user_table.get_children():
            self.user_table.delete(i)
        for user in users:
            if self.user.status == 1:
                self.user_table.insert('', END, values=(user.id, user.name, user.surname, user.login, '-', user.email, self.get_status_function(user.status), user.birthdate))
            elif self.user.status == 2 or self.user.status == 3:
                self.user_table.insert('', END, values=(user.id, '-', '-', user.login, '-', user.email, self.get_status_function(user.status), '-'))
            else:
                self.user_table.insert('', END, values=(user.id, '-', '-', user.login, '-', '-', self.get_status_function(user.status), '-'))

    def authenticate(self):
        login = self.authentication_login_entry.get()
        password = self.authentication_password_input.get()
        self.user = self.authentication_function(login, password)

        self.update_()



    def validator(self, value:str, pattern:str, error_label:Label):
        if re.fullmatch(pattern, value) is None:
            error_label.configure(text='Ошибка валидации')
            return False
        error_label.configure(text='')
        return True






