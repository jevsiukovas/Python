'''Урок 4. Полезные инструменты

4. 5. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен
быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также
необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.  '''

from itertools import count
from itertools import cycle


def my_count_f(start_number):
    for el in count(start_number):
        if el > start_number + 10:
            break
        else:
            print(el)


def my_cycle_f(my_list, iteration):
    i = 0
    iterator = cycle(my_list)
    while i < iteration:
        print(next(iterator))
        i += 1


my_count_f(start_number=int(input("Enter integer: ")))
my_cycle_f(my_list=[1, 2, 3], iteration=int(input("Enter iterator: ")))
