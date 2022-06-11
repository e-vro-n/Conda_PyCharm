# Практика №1 (Практическое_задание_1_ВрЕН) в Юпитер
# 1) Сначала делаем словарь пользователей соц сети(11 участников) ----------------------------------------------------
users = [
    {"id": 1, "name": "Алекс"},
    {"id": 2, "name": "Маша"},
    {"id": 3, "name": "Яна"},
    {"id": 4, "name": "Даша"},
    {"id": 5, "name": "Макс"},
    {"id": 6, "name": "Клим"},
    {"id": 7, "name": "Женя"},
    {"id": 8, "name": "Света"},
    {"id": 9, "name": "Миша"},
    {"id": 10, "name": "Дима"},
    {"id": 11, "name": "Клава"}
]
# сделал еще вариант входного словаря с данными для проверки универсальности работы
# функции dic_name(d1) - ниже по коду ( для вычленения ключей входного списка соц сети)
users1 = [
    {"id": 1, "name": "Алекс", 'age': 18},
    {"id": 2, "name": "Маша", 'age': 15},
    {"id": 3, "name": "Яна", 'age': 21},
    {"id": 4, "name": "Даша", 'age': 25},
    {"id": 5, "name": "Макс", 'age': 19},
    {"id": 6, "name": "Клим", 'age': 31},
    {"id": 7, "name": "Женя", 'age': 28},
    {"id": 8, "name": "Света", 'age': 33},
    {"id": 9, "name": "Миша", 'age': 27},
    {"id": 10, "name": "Дима", 'age': 19},
    {"id": 11, "name": "Клава", 'age': 23}
]
print(type(users))
# print(users)
# for el in users:
#     print(el)

# 2) Составим список кортежей (пользователь, кол-во друзей) ----------------------------------------------------------
fp = [(1, 4), (1, 8), (2, 5), (2, 6), (2, 11), (3, 5), (3, 6), (3, 11), (4, 1), (4, 5), (4, 11), (5, 2), (5, 3),
      (5, 4), (5, 7), (6, 2), (6, 3), (6, 9), (7, 5), (7, 8), (8, 1), (8, 7), (8, 10), (9, 6), (9, 10), (10, 8),
      (10, 9), (11, 2), (11, 3), (11, 4)]
# print(type(fp))
# print(fp)

# !!ради интереса хотел вывести длинный список построчно с заданным кол-вом кортежей в строке
# count = 0
# a = 4
# count2 = a
# for i in range(len(fp)):
#     if i <= len(fp) and count2 <= len(fp):
#         while count < count2:
#             print(fp[count], end=f'/[{count+1}] ')
#             count += 1
#             if count == count2:
#                 print()
#         if (count2 + a) <= len(fp):
#             count2 += a
#         else:
#             count2 = len(fp)

# 3)Инициализировать словарь пустым списком для идентификатора каждого пользователя
friendships = {user["id"]: [] for user in users}
# print(type(friendships), friendships)

for i, j in fp:
    friendships[i].append(j)  # Добавить j как друга для i
    friendships[j].append(i)  # Добавить i как друга ДЛЯ j
# print(friendships)
for key, value in friendships.items():
    friendships[key] = sorted(set(value))  # исключим обратные ссылки(задвоенность и для удобства отсортируем)
print('dict', friendships)

for k, v in friendships.items():
    print(k, v)

# 4)Создадим функцию определяющяя количество друзей у выбранного пользователя
print('1x1x1', users[10])


def number_of_friends(u):
    user_id = u['id']
    friend_ids = friendships[user_id]
    return len(friend_ids)


print(users[10]['name'], number_of_friends(users[10]))

# 5)Создадим функцию, выводящую на экран пользователей, отсортированных по количеству друзей

# а)создадим вспомогательную функцию для вычленения значений ключей первоначального входного списка словарей отражающий
# пользователей соцсети

num_friends_by_name = []


def dic_name(d1):
    d1_keys = list(d1[0].keys())
    dict_id_name = []
    for el in d1:
        prom_lst = []
        for i in range(len(d1_keys)):
            prom_lst.append(el[d1_keys[i]])
        dict_id_name.append(prom_lst)
    return dict_id_name


print('function', dic_name(users))
# print(dic_name(users1))

# б) теперь с помощью функции dic_name(d1) создадим список кортежей (пользовательб кол-во друзей)
for k, v in friendships.items():
    num_friends_by_name.append((*[el[1] for el in dic_name(users) if k == el[0]], len(v)))

print(num_friends_by_name)

# 7)Сделаем сортировку списка по числу друзей:
num_friends_by_name.sort(key=lambda x: (-x[1], x[0]))
print(num_friends_by_name)


# for el in num_friends_by_name:
#     print(el)


### Изменить данную функцию, чтобы она выводила Имена пользователей из списка друзья друзей
# а) выводит id друзей друзей:
def friends_of_friends(user):
    user_id = user["id"]
    return sorted(set([ff_id
            for friend_id in friendships[user_id]
            for ff_id in friendships[friend_id]
            if ff_id != user_id and ff_id not in friendships[user_id]]))


print('клава', friends_of_friends(users[10]))


# б) выводит имена друзей друзей:
def friends_of_friends_n(user):
    user_id = user["id"]
    ff = sorted(set([ff_id
            for friend_id in friendships[user_id]
            for ff_id in friendships[friend_id]
            if ff_id != user_id and ff_id not in friendships[user_id]]))
    id_name = dic_name(users)
    return [name[1] for id in ff for name in id_name if name[0] == id]


print(friends_of_friends_n(users[0]))

#  Создать список с кортежами (Имя пользователя , Список имен рекомендованных друзей) - то бишь пользователь и
#  друзья его друзей)

num_friends_by_friend = [(usr['name'], friends_of_friends_n(usr)) for usr in users]
print('ff', num_friends_by_friend)

for el in num_friends_by_friend:
    print(el)