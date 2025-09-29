print('Д/з №03')
#1

name = "Віталій"
day = "понеділок"

print('1.')
# 1. Конкатенація
message1 = 'Good day ' + name + '! ' + day.title() + ' is a perfect day to learn some python.'

# 2. Форматування через .format()
message2 = 'Good day {}! {} is a perfect day to learn some python.'.format(name.title(), day.title())

# 3. f-рядки (f-strings)
message3 = f'Good day {name}! {day.title()} is a perfect day to learn some python'
# 4. %
message4 = 'Good day %s! %s is a perfect day to learn some python.' % (name, day.title())


# Вивід результатів
print("Варіант 1 (конкатенація):")
print(message1)
print("\nВаріант 2 (.format()):")
print(message2)
print("\nВаріант 3 (f-string):")
print(message3)

#2
name_first = 'vitaliy'
name_last = 'tynyanko'
full_name = name_first.title() + ' ' + name_last.title()
print('2.')
print('Hello', full_name, end='!\n\n')

#3
a = 7
b = 2
print('3.')
print('a + b =', a + b)
print('a - b =', a - b)
print('a : b =', a / b)
print('a * b =', a * b)
print('a ** b =', a ** b)
print('[b - a] =', abs(b - a))
print('a // b =',  a // b)
print('a % b =',  a % b)