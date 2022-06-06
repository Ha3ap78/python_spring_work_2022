# todo: Реализовать полный функционал системы. Любой класс можно расширить до той функциональности которая
# потребуется в результате написания кода.

import psycopg
import bcrypt
import datetime

class DB:
    '''Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются
        атрибуты доступа к БД. Метод возвращает соединение.'''

    __instance__ = None

    def __new__(cls, *args, **kwargs):  # '''Singltone класс. Метод возвращает объект класса DB
                                        # и запрещает создание других экзмепляров класса''
        if not cls.__instance__:
            cls.__instance__ = object.__new__(cls)
            return cls.__instance__
        else:
            raise Exception(f"Нельзя создать более одного объекта класса {DB.__name__}")

    def __init__(self, database, user, passw):

        self.database = database
        self.user = user
        self.passw = passw

    def get_connect(self):
        conn = psycopg.connect(f"dbname={self.database} user={self.user} password={self.passw}")
        return conn



class Auth:
    """Класс содержит методы регистрации, захода в систему и выхода из нее"""
    is_auth = False

    def __init__(self, conn):
        self.conn = conn

    def user_in_base(self, login):
        # Проверяет есть ли пользователь в базе
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT login FROM public.user WHERE login LIKE '{login}'")
            return False if cur.fetchone() == None else True

    def registration(self):

        """Метод создания профиля пользователя в системе """

        login = input('Введите логин: ')

        if self.user_in_base(login) == False and login != '':
            pswd = input('Введите пароль: ')
            pswd = bcrypt.hashpw(pswd.encode(), bcrypt.gensalt())
            surname = input('Введите фамилию: ')
            name = input('Введите имя: ')
            otchestvo = input('Введите отчество: ')
            dt_birth = input('Введите дату рождения (дд.мм.гггг): ')
            dt_birth = [int(i) for i in dt_birth.split('.')]
            dt_birth = datetime.date(dt_birth[2], dt_birth[1], dt_birth[0])
            email = input('Введите адрес эл.почты: ')
            tel = input('Введите номер телефона: ')
            group = input('Введите номер группы: ')
            return login, pswd, surname, name, otchestvo, dt_birth, email, tel, group

        else:
            print('Логин пустой или такой пользователь уже существует. Введите другой логин')
            return self.registration()

    def login(self):
        """Метод аутентификации пользователя в системе"""

        login = input('Введите логин: ')
        pswd = input('Введите пароль: ')
        if self.user_in_base(login):
            with self.conn.cursor() as cur:
                cur.execute(f"SELECT login, password FROM public.user WHERE login LIKE '{login}'")
                hashed_pass = cur.fetchone()
                if bcrypt.checkpw(pswd.encode(), hashed_pass[1].encode()):
                    cur.execute(f"""SELECT name, surname FROM public.profile a
                                    JOIN public.user b ON a.id_user = b.id_user
                                    WHERE b.login LIKE '{login}'""")
                    data = cur.fetchone()
                    if data != None:
                        print(f'Добро пожаловать {data[0]} {data[1]}!')
                    else:
                        print(f'Профиль пользователя {login} не найден')
                        Auth.is_auth = False
                        return
                else:
                    print('Введен неверный пароль')
                    return
                Auth.is_auth = True
                return
        else:
            print("Пользователь не найден")
            Auth.is_auth = False
            return

    def logout(self):
        Auth.is_auth = False


class Profile:
    ''' Данный класс содержит конструктор и метод set_profile и get_profile для добавления и получения
     пользователя соответсвенно'''
    def __init__(self, login, password, name, surname, otchestvo, dt_birth, email, tel, group):
        """В констукторе инициализируем атрибуты сущности Profile"""
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.otchestvo = otchestvo
        self.dt_birth = dt_birth
        self.tel = tel
        self.email = email
        self.group = group

    def set_profile(self, conn):
        """в аргументе conn передается дискриптор подключения к БД"""
        try:
            with conn.cursor() as cur:
                dt_create = datetime.datetime.today()
                cur.execute(f"""
                       INSERT INTO public.user (login, password, dt_create) 
                       VALUES ('{self.login}', '{self.password.decode()}', '{dt_create.strftime("%Y-%m-%d")}')""")

                cur.execute(f"SELECT id_group FROM public.group WHERE name LIKE '{self.group}'")
                if cur.fetchone() == None:
                    cur.execute(f"INSERT INTO public.group (name) VALUES ('{self.group}')")

                cur.execute(f"""
                                            SELECT a.id_student FROM student a
                                            JOIN public.user b ON a.id_user = b.id_user
                                            WHERE b.login LIKE '{self.login}'""")

                if cur.fetchone() == None:
                    cur.execute(f"""INSERT INTO public.student (id_group, name, surname, tel, id_user)
                                           VALUES
                                           ((SELECT id_group FROM public.group 
                                           WHERE name LIKE '{self.group}'), '{self.name}', '{self.surname}', '{self.tel}',
                                           (SELECT id_user FROM public.user WHERE login LIKE '{self.login}'))""")

                cur.execute(f"""
                                       INSERT INTO profile (id_user, id_student, name, surname, patronymic, dt_birth, 
                                       tel, email, id_group)
                                       VALUES 
                                       ((SELECT id_user FROM public.user WHERE login LIKE '{self.login}'), 
                                       (SELECT id_student FROM student WHERE id_user = (SELECT id_user FROM public.user 
                                       WHERE login LIKE '{self.login}')), 
                                       '{self.name}', '{self.surname}', '{self.otchestvo}', 
                                       '{self.dt_birth.strftime("%Y-%m-%d")}', '{self.tel}', '{self.email}',
                                       (SELECT id_group FROM public.group WHERE name LIKE '{self.group}'))""")

        except psycopg.errors.UniqueViolation as err:
            print('Такой номер телефона уже есть в базе')
            print(err)

        except psycopg.Error as err:
            print('Ошибка регистрации нового пользователя. Тип ошибки:', type(err))
            print(err)
            # main()

        else:
            print(f"Пользователь {self.login} успешно зарегистрирован")
            conn.commit()
            return True


def get_profile(self, conn):
    # Извлекает профиль из БД
    pass


conn = DB('testsystem', 'testsystem', 'tyubvc9').get_connect()

auth = Auth(conn)
new = list(auth.registration())
profile = Profile(new[0], new[1], new[2], new[3], new[4], new[5], new[6], new[7], new[8]).set_profile(conn)
conn.close()

#
#
# class Test:
#     """ В классе реализуем методы работы с БД """
#
#     def get_list_tests(self):
#         """В методе  получаем список тестов по темам """
#         pass
#
#     def get_questions(self, id_test):
#         """В методе  получаем список вопросов-ответов по id теста """
#         pass
#
#
# class TestSystem:
#     "Класс взаимодействует с моделью и представлением. Включает всю бизнес логику системы."
#     def run(self):
#         """Метод реализует запуск теста"""
#         pass
#
#     def show_list(self):
#         """Метод реализует вывод списка тестов на экран"""
#         pass
#
#     def show_question(self, id_question):
#         """Метод реализует вывод списка тестов на экран"""
#
#
#     def YouMethods(self):
#         """Методы которые вам дополнительно понадобятся"""
#
#
# class View:
#     """ 'Абстрактный' класс для потомков """
#     def render(self):
#         pass
#
#
# class TestView(View):
#     """В классе перегружаем виртуальный метод  render от родителя"""
#
#     def render(self, data):
#         """Метод реализует отрисовку экранной формы выбора билета """
#
#
# class QuestionView(View):
#     """В классе перегружаем виртуальный метод  render от родителя"""
#
#     def render(self, data):
#         """Метод реализует отрисовку вопроса с вариантами ответа и строкой выбора варианта"""
#
#
# class RegistrationView(View):
#     """В классе перегружаем виртуальный метод  render от родителя"""
#
#     def render(self, data):
#         """Метод реализует отрисовку регистрации пользователя"""
#
#
# class LoginView(View):
#     """В классе перегружаем виртуальный метод  render от родителя"""
#
#     def render(self, data):
#         """Метод реализует отрисовку входа по логину и паролю для зарегистрированного пользователя"""
