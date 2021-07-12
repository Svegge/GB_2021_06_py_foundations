"""
4. Создать (не программно) текстовый файл со следующим содержимым: One — 1
   Two — 2 Three — 3 Four — 4 Необходимо написать программу, открывающую файл на
   чтение и считывающую построчно данные. При этом английские числительные
   должны заменяться на русские. Новый блок строк должен записываться в новый
   текстовый файл.
"""

translate_dic = {
    'One': 'Раз',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

data_dict = {}

with open('task_04_input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        (word, number) = line.replace('\n', '').replace('—', '').split()
        data_dict[translate_dic[word]] = number
li = []
for k, v in data_dict.items():
    li.append(k + ' — ' + v)

translated_str = '\n'.join(li)
with open('task_04_output.txt', 'w', encoding='utf-8') as file:
    file.write(translated_str)
