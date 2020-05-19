# Урок 2. Встроенные типы и операции с ними
#
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
seasons_dict = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'}
month = int(input("Please enter a month number from 1 to 12: "))
if month == 12 or month == 1 or month == 2:
    print(seasons_dict.get(1))
    print(month_list[month - 1])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    print(month_list[month - 1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(month_list[month - 1])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(month_list[month - 1])
else:
    print("Error. We have only 12 months")
