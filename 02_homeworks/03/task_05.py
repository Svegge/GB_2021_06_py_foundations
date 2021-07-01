'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При
   нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
   ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
   чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа
   вводится специальный символ, выполнение программы завершается. Если
   специальный символ введен после нескольких чисел, то вначале нужно добавить
   сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''


def sum_numbers(number_sum, user_string):
    stop_marker = False
    for number in user_string.split(' '):
        if number != '/':
            try:
                number_sum = number_sum + float(number)
            except ValueError:
                continue
        else:
            result = number_sum
            stop_marker = True

    return number_sum, stop_marker


number_sum = 0

while True:
    user_string = input(
        'Please input number row if need stop enter "/":\n>>> ')

    number_sum, stop_marker = sum_numbers(number_sum, user_string)
    print(number_sum)
    if stop_marker:
        break
