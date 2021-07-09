"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна
   содержать данные о фирме: название, форма собственности, выручка, издержки.
   Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно прочитать
   файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
   получила убытки, в расчет средней прибыли ее не включать. Далее реализовать
   список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
   со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
   (со значением убытков). Пример списка: [{“firm_1”: 5000, “firm_2”: 3000,
   “firm_3”: 1000}, {“average_profit”: 2000}]. Итоговый список сохранить в виде
   json-объекта в соответствующий файл. Пример json-объекта: [{"firm_1": 5000,
   "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import re
import json
business_dict = {}

with open('task_07.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        (name, *args) = line.replace('\n', '').split()
        li = list(map(int, re.findall('\\d+', ' '.join(args))))
        business_dict[name] = li[0] - li[1]

avg_list_values = [int(i) for i in business_dict.values() if i > 0]
avg_dic = {}
avg_dic['average_profit'] = sum(avg_list_values) / len(avg_list_values)

result_list = [business_dict, avg_dic]
print(result_list)

with open('task_07.json', 'w') as file:
    json.dump(result_list, file)
