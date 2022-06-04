#todo: Реализовать классы DB и Profile

import psycopg
import datetime


class DB:

    '''Данный класс содержит конструктор и метод get_connect. В конструкторе инициализируются переменные
     (атрибуты доступа к БД) . Метод возвращает соединение.'''

    def __init__(self, dbname, user, password):
        self.dbname = dbname
        self.user = user
        self.passw = password

    def get_connect(self):
        try:
            return psycopg.connect(f'dbname = {self.dbname} user = {self.user} password = {self.passw}')

        except psycopg.errors.OperationalError as err:
            print('Ошибка подключения к БД\n', err)
            return None


class Profile:

    ''' Данный класс содержит конструктор и метод set_profile и get_profile для добавления и получения
     пользователя соответсвенно'''

    def __init__(self, login, password, name, surname, dt_birth, tel, email):
        '''В констукторе инициализируем атрибуты сущности Profile'''
        self.login = login
        self.passw = password
        self.name = name
        self.surname = surname
        self.dt_birth = dt_birth
        self.tel = tel
        self.email = email
        self.today = datetime.date.today()

    def set_profile(self, conn):
        '''Добавляет профиль в БД. В аргументе conn передается дискриптор подключения к БД '''
        try:
            with conn.cursor() as cur:
                cur.execute(f"SELECT login FROM public.user WHERE login LIKE '{self.login}'")
                if cur.fetchone() == None:
                    cur.execute(f"""
                    INSERT INTO public.user (login, password, dt_create) 
                    VALUES ('{self.login}', '{self.passw}', '{self.today.strftime("%Y-%m-%d")}'""")
                    cur.execute(f"""
                    INSERT INTO profile (name, id_user, surname, dt_birth, tel, email)
                    VALUES ('{self.name}', (SELECT id_user FROM public.user WHERE login LIKE '{self.login}'), 
                    '{self.surname}', '{self.dt_birth}', '{self.tel}', '{self.email}')
                    """)

        except psycopg.Error as err:
            print(err)
            return None

    def get_profile(self, conn):
        '''Извлекает профиль из БД'''
        try:
            with conn.cursor() as cur:
                cur.execute(f"""
                SELECT a.name, a.surname, a.dt_birth, a.tel, a.email 
                FROM profile a JOIN public.user b ON a.id_user = b.id_user
                WHERE b.login LIKE '{self.login}'""")
                return cur.fetchone()

        except psycopg.Error as err:
            print(err)
            return None

db = DB('testsystem', 'testsystem', 'tyubvc9').get_connect()

if db != None:
    login = input('Введите логин: ')
    profile = Profile(login, 'sharik11', 'Полиграф', 'Шариков', '1925-01-06', '79113157078', 'sharikov@gmail.com')
    data = profile.get_profile(db)

    if data != None:
        print(f"""
Данные профиля: {profile.login}\n
Имя: {data[0]}
Фамилия: {data[1]}
Возраст: {profile.today.year - data[2].year}
Телефон: {data[3]}
E-mail: {data[4]}
    """)

    else:
        print('Не удалось получить профиль')
        if profile.set_profile(db) != None:
            print(f'Добавлен профиль {profile.login}')
    db.close()


