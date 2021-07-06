"""
6. Реализовать два небольших скрипта: а) итератор, генерирующий целые числа,
   начиная с указанного, б) итератор, повторяющий элементы некоторого списка,
   определенного заранее. Подсказка: использовать функцию count() и cycle()
   модуля itertools. Обратите внимание, что создаваемый цикл не должен быть
   бесконечным. Необходимо предусмотреть условие его завершения. Например, в
   первом задании выводим целые числа, начиная с 3, а при достижении числа 10
   завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
   повторение элементов списка будет прекращено.
"""
from itertools import count, cycle, takewhile, islice


# def iter_numbers(start_number):
#     for i, j in enumerate(count(start_number)):
#         if i < 100:
#             yield j
#         else:
#             break

def iter_numbers(start_number):
    """
    Creates generator of int numbers started from function argument
    """
    for i in takewhile(lambda x: x < 101, count(start_number)):
        yield i


def repeat_list_values(li):
    """
    Creates generator of given list, which keeps 10 times repeated list values
    """
    for i in islice(cycle(li), 10 * len(li)):
        yield i


def go_through_generator(generator_obj):
    """
    Function walks through given generator and prints each items.
    In the end prints corresponding status in terminal.
    """
    try:
        while True:
            print(next(generator_obj))
    except BaseException:
        print('end of iterator')


iter_gen = iter_numbers(11)

go_through_generator(iter_gen)

repeat_gen = repeat_list_values([True, 2.12, 'sdfdf'])

go_through_generator(repeat_gen)
