'''
4. Пользователь вводит целое 
положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и 
арифметические операции.
'''

input_num = input('Please, enter any number:\n>>> ')

count_numbers = len(input_num)

curr_num = 0

bigest_number = 0

while curr_num != count_numbers:
    current_number = int(input_num[curr_num])

    if bigest_number - current_number < 0:
        bigest_number = current_number
        
    curr_num += 1

print(f'The biggest number is: {bigest_number}')