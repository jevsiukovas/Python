'''Урок 5. Работа с файлами
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
 Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
 числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

rus_eng = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open("text_4.1.txt", 'a', encoding="utf-8") as transformed:
    with open("text_4.txt", encoding="utf-8") as source:
        line = source.read().split("\n")
        for i in line:
            i = i.split(" - ")
            transformed.writelines(rus_eng[i[0]] + ' - ' + i[1] + "\n")

