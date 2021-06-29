'''
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и
выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''

total_secs = int(input('Please enter seconds:\n>>> '))

hh_var = str(total_secs // 360).zfill(2)
mm_var = str(int((total_secs % 360) / 60)).zfill(2)
ss_var = str(int((total_secs % 360) % 60)).zfill(2)

print(f'{hh_var}:{mm_var}:{ss_var}')
