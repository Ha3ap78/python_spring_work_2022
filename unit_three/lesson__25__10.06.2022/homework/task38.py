# todo: Реализовать две сопрограммы. Первая с заданной периодичность(раз в 2,3 сек) пишет в файл и выводит результат.
# другая делает запрос к БД на выборку  билета и отображает поочередно  название билета (раз в 2,3 сек)


import asyncio
from aiofile import async_open
import asyncpg
import random


async def write():
    async with async_open('class.TXT', 'rt+', encoding="utf-8") as f:
        await f.write('Test')
        await asyncio.sleep(2)
        await f.write(' Test again')
        f.seek(0)
        a = await f.read()
        print(a)


async def get_profile():
    conn = await asyncpg.connect(database="testsystem", user='testsystem', password='tyubvc9', host="localhost", port="5432")
    async with conn.transaction():
        cur = await conn.fetch(f"SELECT * FROM student")
        profiles = [dict(cur[i]) for i in range(len(cur))]
        list = [[j for j in profiles[i].values()] for i in range(len(profiles))]
        print(random.choice(list)[0])


async def main():
    await asyncio.gather(write(), get_profile())

asyncio.run(main())


# async def get_list_tests(cls):
#     print(f"Вход в БД {datetime.datetime.now()}")
#     con = await asyncpg.connect(dbname="testsystem2", user="test", password="123", host="localhost", port="5432")
#     print(f"Запрос данных из БД {datetime.datetime.now()}")
#     async with con.transaction():
#         cur = await con.fetch(f"""SELECT id_answer, answer_text FROM test_answer""")
#         theme_lists = [dict(cur[i]) for i in range(len(cur))]
#         val_list = [[v for v in theme_lists[i].values()] for i in range(len(theme_lists))]
#         print(random.choice(val_list)[0])