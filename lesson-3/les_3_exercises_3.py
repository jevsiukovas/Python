'''Урок 3. Функции. 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
 наибольших двух аргументов.'''


def my_func(i_1, i_2, i_3):
    if i_1 >= i_3 and i_2 >= i_3:
        return i_1 + i_2
    elif i_1 > i_2 and i_1 < i_3:
        return i_1 + i_3
    else:
        return i_2 + i_3


print(
    f'Result: {my_func(int(input("Enter first integer: ")), int(input("Enter second integer: ")), int(input("Enter third integer: ")))}')
