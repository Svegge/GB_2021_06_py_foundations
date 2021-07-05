'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные
   пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
   Функция должна принимать параметры как именованные аргументы. Реализовать
   вывод данных о пользователе одной строкой.
'''


def user_data(**kwargs):
    """
    Prints user data with one string
    """
    [print(f'{k} = {v}', end='; ') for k, v in kwargs.items()]


user_data(
    name='Karl',
    lastname='Barth',
    birth_year='1886',
    city='Basel',
    email='karl_barth@email.com',
    phone='123654786548')
