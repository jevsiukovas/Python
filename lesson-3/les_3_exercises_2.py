'''Урок 3. 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год
 рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать
 вывод данных о пользователе одной строкой.Функции. '''


def data_func(**kwargs):
    return kwargs


print(data_func(name=input('enter name: '), surname=input('enter surname: '), age=int(input('enter age: ')),
                city=input('enter city: '), email=input('enter email: '), telephone=input('input telephone: ')))
