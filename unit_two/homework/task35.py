import bcrypt
import psycopg
from abc import ABC, abstractmethod

class DB:
    '''Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются переменные
      (атрибуты доступа к БД) . Метод возвращает соединение.'''

    # В констукторе инициализируем атрибуты доступа к БД
    def __init__(self, dbname, user, password):
        self.dbname = dbname
        self.user = user
        self.password = password

    def get_connect(self):
        # Метод возвращает соединение к БД
        connect = psycopg.connect(f" dbname = {self.dbname} user = {self.user} password = {self.password}")
        return connect


class Auth:
    """Класс содержит методы регистрации, захода в систему и выхода из нее"""
    def __init__(self, conn):
        self.conn = conn
        self.is_auth = False

    def registration(self, conn):
        """"Метод создания профиля пользователя в системе """
        print("Регистрация")
        id_group = 1
        name = input("Введите Имя: ")
        surname = input("Введите Фамилию: ")
        age = int(input("Укажите Возраст: "))
        login = input("Придумайте логин: ")
        password = input("Придумайте пароль: ")
        new_user = Profile(id_group, name, surname, age, login, password)
        new_user.set_profile(conn)
        print(f"Поздравляем {surname}{name}, Вы успешно зарегистрировались!")
        self.is_auth = True


    def login(self):
        """Метод аутентификации пользователя в системе"""
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        password1 = Profile().get_profile(conn, login)
        print(password1)
        print("Добро пожаловать")if (bcrypt.checkpw(password.encode(), bytes(password1))) is True else print("Неверный пароль")
        print(f"{login} Вы вошли в систему!")


    def logout(self):
        Auth.is_auth = False


class Profile:
    ''' Данный класс содержит конструктор и метод set_profile и get_profile для добавления и получения
      пользователя соответсвенно'''
    def __init__(self, id_group=None, name=None, surname=None,  age=None, login=None, password=None):
        """В констукторе инициализируем атрибуты сущности Profile"""
        self.id_group = id_group
        self.name = surname
        self.surname = name
        self.age = age
        self.login = login
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


    def set_profile(self, conn):
        """в аргументе conn передается дискриптор подключения к БД, метод Добавляет профиль в БД"""
        cur = conn.cursor()
        cur.execute(f"""
                                INSERT INTO student (id_group, name, surname, age, login, password)
                                VALUES  ({self.id_group}, '{self.name}', '{self.surname}', {self.age},
                                 '{self.login}', {self.password});
                                """)
        conn.commit()

    def get_profile(self, conn, login):
        """Метод Извлекает профиль из БД"""
        cur = conn.cursor()
        cur.execute(f"""SELECT "password" FROM student where login ='{login}';""")
        obj = cur.fetchall()
        return obj


class Test:
    """ В классе реализуем методы работы с БД """

    def __init__(self, conn):
        self.conn = conn

    def get_list_tests(self):
        """В методе  получаем список тестов по темам """
        cur = conn.cursor()
        cur.execute(f"""SELECT Theme FROM test;""")
        obj_theme = list(sum(cur.fetchall(), ()))
        return obj_theme


    def get_questions(self, id_test):
        """В методе  получаем список вопросов-ответов по id теста """
        cur = conn.cursor()
        cur.execute(f"""SELECT q.text_quest, a.text_answer FROM questions q, answer a 
                        WHERE q.id_questions = a.id_questions;""")
        quest = list(sum(cur.fetchall(), ()))
        print(f'Список вопросов-ответов {quest}')
        return quest




class TestSystem:
    "Класс взаимодействует с моделью и представлением. Включает всю бизнес логику системы."
    def __init__(self, conn):
        self.conn = conn


    def run(self):
        """Метод реализует запуск теста"""
        run = Auth.login(conn)
        # Получаем логин из класса auth
        return run

    def show_list(self):
        """Метод реализует вывод списка тестов на экран"""
        # Надо дернуть гет лист тест из теста
        show_test = Test.get_list_tests(self.conn)
        return show_test

    def show_question(self, id_theme):
        """Метод реализует вывод списка вопросов на экран"""
        show_ques = Test.get_questions(conn)
        return show_ques


class View:
    """ 'Абстрактный' класс для потомков """

    @abstractmethod
    def render(self):
        pass


class TestView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""

    def render(self, data):
        """Метод реализует отрисовку экранной формы выбора билета """
        data = Test.get_list_tests(self.conn)
        return data


class QuestionView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""

    def render(self, data):
        """Метод реализует отрисовку вопроса с вариантами ответа и строкой выбора варианта"""
        data = Test.get_questions(conn)
        return data


class RegistrationView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""

    def render(self, data):
        """Метод реализует отрисовку регистрации пользователя"""
        data = Auth.registration(conn)


class LoginView(View):
    """В классе перегружаем виртуальный метод  render от родителя"""

    def render(self, data):
        """Метод реализует отрисовку входа по логину и паролю для зарегистрированного пользователя"""
        data = Auth.login(conn)
        return data


connection = DB(dbname="testsystem", user="testsystem", password="tyubvc9;")
conn = connection.get_connect()
