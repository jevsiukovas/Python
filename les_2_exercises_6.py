# Урок 2. Встроенные типы и операции с ними
#
# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж храни
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
# название, а значение — список значений-характеристик, например список названий товаров.

product = int(input("Каково количество товара: "))
n = 1
my_dict = []
my_list = []
my_analys = {}
while n <= product:
    my_dict = dict({'название': input("введите название товара"), 'цена': input("Введите цену товара"),
                    'количество': input('Введите количество товара'), 'eд': input("Введите единицу измерения ")})
    my_list.append((n, my_dict))
    n += 1
    my_analys = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
print(my_list)
print(my_analys)
