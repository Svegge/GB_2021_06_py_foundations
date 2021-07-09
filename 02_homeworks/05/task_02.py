"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
   выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('task_02.txt', 'r') as file:
    lines = file.readlines()
    for idx, line in enumerate(lines, 1):
        print(idx, len(line.split()))
