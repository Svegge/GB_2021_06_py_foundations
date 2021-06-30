'''
6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[

(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
(2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
(3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})

]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик,
например список названий товаров.
Пример:
{

'название': ['компьютер', 'принтер', 'сканер'],
'цена': [20000, 6000, 2000],
'количество': [5, 2, 7],
'ед': ['шт.']

}
'''

goods = []
goods_analysis = {}
goods_id = 1
goods_params = set()

while goods_id > 0:
    goods_id = int(input('Enter goods id, if you want to stop enter 0:\n>>> '))
    if goods_id <= 0:
        break
    goods_name = input('Enter goods name:\n>>> ')
    goods_price = float(input('Enter goods price\n>>>  '))
    goods_qty = int(input('Enter quantity of goods\n>>>  '))
    goods_uom = input('Enter goods unit of measurement:\n>>>  ')

    goods_dict = {
        'name': goods_name,
        'price': goods_price,
        'quantity': goods_qty,
        'units': goods_uom

    }

    goods_tuple = (goods_id, goods_dict)
    goods.append(goods_tuple)

for i in goods:
    for k in i[1]:
        goods_params.add(k)

for key_val in goods_params:
    value_list = set()

    for item in goods:
        value_list.add(item[1][key_val])

    goods_analysis[key_val] = value_list


print('the goods list is', goods)
print('the goods analysis is', goods_analysis)
