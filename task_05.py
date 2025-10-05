# Task 5

# 1
# Вгадай число

import random


num_user = input('Введіть число від 1 до 10, включно >')
num_comp = random.randint(1, 10)

if not num_user.isdigit():
    print('Ви ввели неправильно!')
else:
    if num_comp == int(num_user):
        print('Ви вгадали')
    else:
        print(f'Ви не вгадали, число = {num_comp}' )


# 2
# The birthday greeting program.
#
# Write a program that takes your name as input, and then your age as input and greets you with the following:
#
# “Hello <name>, on your next birthday you’ll be <age+1> years”

name_user = input('Введить ваше ім`я - ')
age_user = input("Age = ")
age_int = int(age_user)
print(f"Hello {name_user}, on your next birthday you’ll be {age_int + 1} years")


# 3
import random

string_user = input('Введіть слово: ')

for i in range(0, 5):

    for j in range(0, len(string_user)):
        print(string[random.randint(0, len(string_user)-1)], end='')
    print()
