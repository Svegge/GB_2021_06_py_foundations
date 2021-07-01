'''
6. Реализовать функцию int_func(),
принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием.
В программу должна попадать строка из слов,
разделенных пробелом.
Каждое слово состоит из латинских букв
в нижнем регистре. Сделать вывод исходной строки,
но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''


def int_func(process_string):
    process_string = process_string.capitalize()
    return process_string


input_string = input('Please enter your string:\n>>> ')

split_string = input_string.split(' ')


print(' '.join(int_func(sub_string) for sub_string in split_string))
