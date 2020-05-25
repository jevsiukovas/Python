''' Урок 4. Полезные инструменты

1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для
конкретных значений необходимо запускать скрипт с параметрами.'''


def salary():
    try:
        hour = float(input('Enter the number of hours: '))
        rate = int(input('Enter the hourly pay rate: '))
        premium = int(input('Enter the amount of the premium: '))
        total = hour * rate + premium
        print(f'The employee will be paid a salary of {total}')
    except ValueError:
        return print('Not a number')


salary()
