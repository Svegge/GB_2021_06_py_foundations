"""
3. Создать текстовый файл (не программно), построчно записать фамилии
   сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад
   менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
   величины дохода сотрудников.
"""

stuff_dict = {}

with open('task_03.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        (name, salary) = line.replace('\n', '').split()
        stuff_dict[name] = salary

big_salary_list = [i[0] for i in stuff_dict.items() if int(i[1]) > 20000]
avg_salary = sum(map(int, stuff_dict.values())) / len(stuff_dict)


print(big_salary_list)
print(avg_salary)
