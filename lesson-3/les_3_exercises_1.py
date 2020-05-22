''' Урок 3. Функции. 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
 пользователя, предусмотреть обработку ситуации деления на ноль. '''


def div():
    try:
        number_1 = int(input("Enter an integer: "))
        number_2 = int(input("Enter an integer: "))
        answer = number_1 / number_2

    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Division by zero is impossible!"

    return answer


print(f'Result: {div()}')
