# Task 07

import random

# 1

# приклад речення для вводу
# hello cell hello far cell hello hello cell hello
sentence = input("Enter your sentence: ") # отримуємо речення від юзера
words_list = sentence.split() # розбиваємо рядок на список
print('words >', words_list) # друкуємо список для перевірки
#пустий словник
words_dict = {}
# додаємо в словник кожне слово у вигляді ключа, а кількість входжень в списку як значення
for key in words_list:
    words_dict[key] = (words_list.count(key))
# друкуємо словник
print(words_dict) # {'hello': 5, 'cell': 3, 'far': 1}


# 2
"""
Обчисліть загальну ціну запасу, де загальна ціна дорівнює сумі ціни товару,
помноженої на кількість цього конкретного товару.

Код має повертати словник із сумами цін за типами товарів.
"""

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# пустий словник
total = {}

for fruit in stock.keys():
    total[fruit] = stock[fruit] * prices[fruit] * 1.0

print('Total cost:', total)
# Total cost: {'banana': 24.0, 'apple': 0.0, 'orange': 48.0, 'pear': 45.0}


# 3
# створити список, що містить кортежі (i, j),
# де 'i' змінюється від 1 до 10, а 'j' відповідає 'i' у квадраті.

# зробити список з кортежами
# list_tuple = [(1, 1), (2, 4), (3, 9), (4, 16)....]

# list_tuple = []
list_tuple = [(i, i**2) for i in range(1, 11)]
print('list_tuple -', list_tuple)
# list_tuple - [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]

# 4

"""
Створити лист із днями тижня.
В один рядок (ну або як завжди) створіть словник виду: {1: "Понеділок", 2:...
Також в один рядок або як вдасться створити зворотний словник {"Понеділок": 1,
"""


week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_forw = {}
days_over = {}
for i, day in enumerate(week):
    days_forw[day] = (i + 1)
    days_over[i + 1] = (day)

print(days_forw)
print(days_over)


# {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
# {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}


