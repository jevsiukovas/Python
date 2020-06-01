''' Урок 5. Работа с файлами
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
 ввода данных свидетельствует пустая строка.'''

'''относительный путь '''
content = open("my_text.txt", "w", encoding="utf-8")
my_text = " "

while my_text != "":
    my_text = input("Please enter text: \n")
    content.write(f"{my_text}\n") if my_text != "" else content.close()

content = open("my_text.txt", "r", encoding="utf-8")
list = content.read()
print(list)
content.close()

# абсолютный путь
# content = open(r"F:\GeekBrains\Python\text_4.txt", "r", encoding="utf-8")
