'''Урок 5. Работа с файлами
 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
 количества слов в каждой строке.
'''


text = open("my_text_2.txt", "r", encoding="utf-8")
content = text.read()
print(f'Content: \n {content}')
text = open("my_text_2.txt", "r", encoding="utf-8")
content = text.readlines()
print(f'Amount lines in a file - {len(content)}')
text = open("my_text_2.txt", "r", encoding="utf-8")
content = text.readlines()
for i in range(len(content)):
    print(f"Amount of sign in the {i + 1} line {len(content[i])}")
text = open("my_text_2.txt", "r", encoding="utf-8")
content = text.read()
content = content.split()
print(f"Total amount of words - {len(content)}")
text.close()