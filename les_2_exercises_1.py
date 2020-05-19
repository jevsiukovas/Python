# Урок 2. Встроенные типы и операции с ними
# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


my_set = [54.5, [3], 9257, True, "Morocco"]
my_call = 'Save our souls!'
my_number = 44
my_float = 77.7
my_bool = True
my_complex = (5 + 2j)
my_int = (5 + 7)

list_1 = [my_set, my_call, my_number, my_float, my_bool, my_complex, my_int]
for a in list_1:
    print(f'{a} is {type(a)}')
