"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
   разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
   выводить ее на экран.
"""

num_list = map(str, list(range(11)))

num_str = ' '.join(num_list)

with open('task_05.txt', 'w', encoding='utf-8') as file:
    file.write(num_str)


with open('task_05.txt', 'r', encoding='utf-8') as file:
    file_str = file.read()

file_li = map(int, file_str.split())

sum_ = sum(file_li)
print(sum_)
