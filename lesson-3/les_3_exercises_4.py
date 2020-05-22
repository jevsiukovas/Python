'''Урок 3. Функции. 4. Программа принимает действительное положительное число x и целое отрицательное число y.
 Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
 При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
 Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
 Второй — более сложная реализация без оператора **, предусматривающая использование цикла. '''


def my_func(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(my_func(float(input("Enter a number: ")), int(input("Enter a negative integer: "))))
