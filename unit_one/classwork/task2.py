#todo 2.1: Заданы множества
# все позьзователи
all_users = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
# пользователи не в сети
offline_users = {'id3', 'id9', 'id7', 'id2', 'id4', 'id6'}
print("Пользователи online: ", all_users - offline_users)

#Вычислить пользователей online


#todo 2.2: Заданы множества
#Даны читатели книг
readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1' }

#Даны читатели газет
readers_magazines = { 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}
print("Пользователи читающие и книги и газеты: ", readers_books & readers_magazines)

#Найти пользователей кто читает и книги и газеты


