#task_04
print('Д/з №04')
#1
# Sample String: 'helloworld'
# Expected Result : 'held'
# Sample String: 'my'
# Expected Result : 'mymy'
# Sample String: 'x'
# Expected Result: Empty String

strings =['helloworld', 'my', 'x']

for string in strings:
    if len(string) <= 1:
        print('Empty String')
    elif len(string) <= 3:
        print(string[0:2] * 2)
    else:
        print(string[0:2] + string[-1:-3:-1])



#2 The valid phone number program.

ph_number = '1234567890'

if ph_number.isdigit() and len(ph_number) == 10:
    print('Номер телефона', ph_number)
else:
    print('Введені данні не є номером телефона')
    

#3  The math quiz program.
quests = [[4, 5], [7, 8], [9, 6]]
for indx, list_indx in enumerate(quests):
    # print(indx)
    # print(list_indx)
    # print(list_indx[1])
    # print(list_indx[0] * list_indx[1])
    print('Ваша відповідь на: ',list_indx[0], '*',list_indx[1])
    quest = input('= ')
    if quest.isdigit():
        if int(quest) == list_indx[0] * list_indx[1]:
            print('Вірно!')
        else:
            print("Помилка!!!")
    else:
        print('Не числова відповідь!')
        
#4
name = 'vitaliy'
name_inp = input("Введіть ваше ім'я: ")
if name_inp.upper() == name.upper():
    print(True)
else: print(False)

