"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
   выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
   обработку ситуации деления на ноль.
"""

from typing import Union


def divide_numbers(num_one: Union[int, float],
                   num_two: Union[int, float]) -> Union[int, float]:
    """
    Function asks two numbers and returns division result
    if null returns message
    """

    try:
        result = float(num_one) / float(num_two)
    except ZeroDivisionError:
        result = None
        print('Zero division is not allowed!')
    return result


num_one = input('Please enter first number:\n>>> ')
num_two = input('Please enter second number:\n>>> ')

res = divide_numbers(num_one, num_two)

print(res)
