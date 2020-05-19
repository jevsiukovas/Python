# Урок 2. Встроенные типы и операции с ними
#
# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
# индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# t = [54.5, [3, 7], 9257, True, "Morocco", 'cool', 1812, "XIP"]


user_numbers = list(input("Please enter numbers "))

if len(user_numbers) % 2 == 0:
    a = 0
    while a < len(user_numbers):
        element = user_numbers[a]
        user_numbers[a] = user_numbers[a + 1]
        user_numbers[a + 1] = element
        a += 2
else:
    a = 0
    while a < len(user_numbers) - 1:
        element = user_numbers[a]
        user_numbers[a] = user_numbers[a + 1]
        user_numbers[a + 1] = element
        a += 2
print(user_numbers)
