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
print(users[10])
def number_of_friends(u):
    user_id = u['id']
    friend_ids = friendships[user_id]
    return len(friend_ids)


print(users[10]['name'], number_of_friends(users[10]))

# 5)Создадим функцию, выводящую на экран пользователей, отсортированных по количеству друзей