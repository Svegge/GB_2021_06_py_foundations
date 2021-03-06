"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
   значения которых больше предыдущего элемента. Подсказка: элементы,
   удовлетворяющие условию, оформить в виде списка. Для формирования списка
   использовать генератор. Пример исходного списка: [300, 2, 12, 44, 1, 1, 4,
   10, 7, 1, 78, 123, 55]. Результат: [12, 44, 4, 10, 78, 123]
"""
source_list = [300, 2, 12, 44, 1, 1, 4,
               10, 7, 1, 78, 123, 55]


def list_gen(li):
    for i in range(len(li)):
        if i > 0 and li[i] > li[i - 1]:
            yield li[i]


result_list = list(list_gen(source_list))

print(result_list)
