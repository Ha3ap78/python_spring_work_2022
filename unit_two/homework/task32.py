# todo: Написать скрипт создания базы данных(ER-модели) TestSystem
# Скрипт  create_db.py  должен создавать таблицы, индексы , констрейнты в СУБД PostgresSQL
# В задании использовать библиотеку psycopg


# Ссылка на документацию
# https://www.psycopg.org/psycopg3/docs/basic/usage.html
# Для подключения использовать пользователя и базу отличную от postgres

import psycopg

# Подключение к базе данных
with psycopg.connect("dbname=homework user=homeuser password=123456") as conn:
    # Открытие курсора для выполнения операций с базой данных
    with conn.cursor() as cur:
        # Создание новой таблицы
        cur.execute("""CREATE TABLE "user" (
          "id_user" SERIAL PRIMARY KEY,
          "first_name" VARCHAR(255) NOT NULL,
          "otchestvo" VARCHAR(255) NOT NULL,
          "last_name" VARCHAR(255) NOT NULL,
          "age" SMALLINT,
          "dt_create" TIMESTAMP,
          "status" BOOLEAN
            );""")

        # Создание новой таблицы
        cur.execute("""CREATE TABLE "profile" (
          "profile" SERIAL PRIMARY KEY,
          "id_users" INTEGER NOT NULL,
          "login" TEXT NOT NULL,
          "password" TEXT NOT NULL,
          "avatar" TEXT NOT NULL,
          "dt_reg" DATE,
          "dt_last_login" DATE,
          "status" BOOLEAN);
                """)
        #
        # # создание индекса
        cur.execute(
            """CREATE INDEX "idx_profile__id_users" ON "profile" ("id_users");"""
        )

        # констрейн
        cur.execute("""
        ALTER TABLE "profile" ADD CONSTRAINT "profile_id_users" FOREIGN KEY ("id_users")
        REFERENCES "user" ("id_user")
        """)

        # добавление нового пользователя в таблицу User
        cur.execute("""
        INSERT INTO "user" (id_user,first_name,otchestvo,last_name,age,dt_create,status)
        VALUES (1,'Семён','Семёнович','Шпак',45,'2022-05-02 07:34:00',true);
        """)

        # добавление в таблицу profile
        cur.execute("""
        INSERT INTO profile (id_users, login,"password", avatar, dt_reg, dt_last_login, status)
        VALUES (1,'shpak_1','56789','avatar link', '2022-05-20 15:22:15','2022-05-23 13:15:10',true);
        """)

        cur.execute("SELECT * FROM profile")   # Запрос базы данных и получение данных в виде объектов Python.
        res = cur.fetchall()
        for i in res:
            print(i)

        conn.commit()
