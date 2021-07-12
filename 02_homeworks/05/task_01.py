"""
1. Создать программно файл в текстовом формате, записать в него построчно
   данные, вводимые пользователем. Об окончании ввода данных свидетельствует
   пустая строка.
"""
from pathlib import Path


def write_line_to_file(file_name: str, data: str):
    root_path = Path(__file__).parent
    file_path = root_path.joinpath(file_name)

    with open(file_path, 'a') as file:
        file.writelines(data)


while True:
    data_string = input('Please, enter your string\n>>> ')
    if data_string == '':
        break
    else:
        write_line_to_file('task_01.txt', data_string + '\n')
