'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
   возвращает сумму наибольших двух аргументов.
'''


def my_func(*args):
    """
    Returns sum of two max args
    """
    args_list = sorted(args)
    result = sum(args_list[-2:])
    return result


result = my_func(1200, 123, 100)
print(result)
