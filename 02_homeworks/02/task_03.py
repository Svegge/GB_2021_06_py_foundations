'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''

season_list = [
    'winter', 'winter', 'spring', 'spring',
    'spring', 'summer', 'summer', 'summer',
    'autumnn', 'autumnn', 'autumnn', 'winter'
]

season_dict = {

    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter',

}

month_num = int(input('Please enter the month number (int 1-12):\n>>> '))

season_val_list = season_list[month_num - 1]
season_val_dict = season_dict[month_num]

print(
    f'Entered month number corresponds to {season_val_list} (list_val), {season_val_dict} (dict_val).')
