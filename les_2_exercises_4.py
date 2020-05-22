# Урок 2. Встроенные типы и операции с ними
#
# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_word = input("Please enter a string of several words: ")
a = user_word.split(' ')
for i, element in enumerate(a, 1):
    if len(element) > 10:
        element = element[0:10]
    print(f"{i}. {element}")
