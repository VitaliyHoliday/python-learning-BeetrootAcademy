# Task 06

import random

# 1
# робимо список випадкових 10
numbers = [random.randint(1, 1000) for i in range(10)]
print(numbers)

index = 0 # індекс у списку
num_max = numbers[0] # беремо перше число та порівнюємо з іншими

while index < len(numbers)-1: # перевіряємо увесь список
    check = numbers[index + 1]
    if num_max < check: # якщо наступний більше він є макс
        num_max = check
    index += 1

print(num_max)

# 2
numbers1 = [random.randint(1, 10) for i in range(10)]
numbers2 = [random.randint(1, 10) for i in range(10)]
numbers3 = []
idx = 0
while idx < len(numbers1):
    number = numbers1[idx]
    if number in numbers2 and number not in numbers3:
        numbers3.append(number)
    idx += 1

print('1 > ', numbers1)
print('2 > ', numbers2)
print('Unic 1+2 > ', numbers3)

# 3
hundred = list(range(1, 101))
numbers4 = []
idx = 0
while idx < len(hundred):
    number_h = hundred[idx]

    if number_h % 7 == 0 and number_h % 5 != 0:
        # if elem1 % 5 != 0:
        numbers4.append(number_h)

    idx += 1

print('Список %7 !=/5 > ', numbers4)