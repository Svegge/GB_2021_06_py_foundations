'''
4. Программа принимает действительное положительное число x и целое
   отрицательное число y. Необходимо выполнить возведение числа x в степень y.
   Задание необходимо реализовать в виде функции my_func(x, y). При решении
   задания необходимо обойтись без встроенной функции возведения числа в
   степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в
степень с помощью оператора **. Второй — более сложная реализация без оператора
**, предусматривающая использование цикла.
'''


def my_func_first(x, y):
    """
    Returns x ** y
    """
    result = x ** y
    return result


def my_func_second(x, y):
    """
    Returns x ** y
    """
    result = 1
    for i in range(abs(y)):
        result = x * result
    result = 1 / result

    return result


result = my_func_first(3, -5)
print(result)

result = my_func_second(3, -5)
print(result)
