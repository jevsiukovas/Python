'''Урок 5. Работа с файлами
 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
 кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
 дохода сотрудников.
'''

with open("text_3.txt", "r", encoding="utf-8") as my_file:
    salary = []
    less = []
    my_list = my_file.read().split("\n")
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            less.append(i[0])
        salary.append(i[1])
print(f"Lower salary 20.000 {less}, Average salary {sum(map(float, salary)) / len(salary)}")
