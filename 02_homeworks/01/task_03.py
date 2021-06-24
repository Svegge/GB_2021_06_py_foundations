'''
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
'''

first_num  = input('Please enter any number:\n>>> ')

second_num = first_num * 2
third_num = first_num * 3

total_num = int(first_num) + int(second_num) + int(third_num)

print(total_num)