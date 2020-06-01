'''Урок 5. Работа с файлами
 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
 должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''


def summary():
    try:
        with open("file_5.txt", "w+", encoding="utf-8") as my_file:
            my_inputs = input("Please enter integers separated by a space, then press Enter \n")
            my_file.writelines(my_inputs)
            my_numb = my_inputs.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print("Error")
    except ValueError:
        print("ValueError. Please enter integers")


summary()
