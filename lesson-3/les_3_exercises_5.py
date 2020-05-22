'''Урок 3. Функции. 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
 выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
 Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный
 символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно
 добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.'''


def my_sum():
    sum_num = 0
    out = False
    while out == False:
        number = input('Enter integer or Q for exit: ').split()

        result = 0
        for element in range(len(number)):
            if number[element] == 'q' or number[element] == 'Q':
                out = True
                break
            else:
                result = result + int(number[element])
        sum_num = sum_num + result
        print(f'Sum is {sum_num}')
    print(f'Total sum is {sum_num}')


my_sum()
