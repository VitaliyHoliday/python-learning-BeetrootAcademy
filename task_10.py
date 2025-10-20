# Task 10
# 1

"""
Напишіть функцію під назвою oops, яка явно викликає
виняток IndexError під час виклику. Потім напишіть
іншу функцію, яка викликає oops всередині оператора try/except,
щоб перехопити помилку. Що станеться, якщо змінити oops на виклик
KeyError замість IndexError?
"""

def oops(x):
    # викликаємо елемент, індекс якого виходить за межі об'єкта
    print(x[len(x)])

y = [1, 2, 3, 4, 5]


try:
    oops(y)
except KeyError:
# except IndexError:
    print('Помилка')
# Як що замінити IndexError на KeyError,
# програма зупинить роботу та видасть помилку: IndexError: list index out of range

# 2
"""
Напишіть функцію, яка приймає два числа від користувача через input(), 
викликає числа a та b , а потім повертає значення квадрата a , 
поділеного на b , та створює блок try-except, який перехоплює виняток, 
якщо два значення, надані функцією input, не були числами, 
і якщо значення b дорівнювало нулю (не можна ділити на нуль).    
"""

result = 0

def squardiv(one, two):
    #
    try:
        result = int(one) ** 2 / int(two)
    except TypeError:
        print('Введені не числа')
        print('TypeError')
    except ValueError:
        print('Введені не числа')
        print('ValueError')
    except ZeroDivisionError:
        print('Cannot divide by zero')
        print('ZeroDivisionError')
    else:
        print(result)



a = input('Введіть число a:')
b = input('Введіть число b:')
squardiv(a, b)
squardiv(31, 0)
squardiv(45, 3)
