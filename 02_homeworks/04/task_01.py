"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
   заработной платы сотрудника. В расчете необходимо использовать формулу:
   (выработка в часах * ставка в час) + премия. Для выполнения расчета для
   конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

file_name, hours, rate, bonus = argv


def get_salary(args_list):
    hours, rate, bonus = [float(i) for i in args_list]
    salary = (hours * rate) + bonus
    return salary


print(get_salary(argv[1:]))
