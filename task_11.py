# task_11
# 1

"""
Напишіть скрипт, який створює новий вихідний файл з назвою myfile.txt
 та записує в нього рядок "Hello file world!". Потім напишіть ще один
 скрипт, який відкриває myfile.txt, зчитує та друкує його вміст
"""

# створюємо файл myfile.txt open, 'w'
with open("myfile.txt", "w", encoding="utf-8") as file:
    # записуємо в файл Hello file world та \n для додавання переходу на новий рядок
    file.write("Hello file world!\n")

# відкриваємо файл, зчитуємо та друкуємо вміст
with open("myfile.txt") as cont_file:
    print(">>>", cont_file.read())
