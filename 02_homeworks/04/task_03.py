"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
   Необходимо решить задание в одну строку. Подсказка: использовать функцию
   range() и генератор.
"""

# тест алгоритма
# def get_good_numbers(
#         range_left=20,
#         range_right=240,
#         divisibility_arg_one=20,
#         divisibility_arg_two=21):
#     for i in range(range_left, range_right + 1):
#         if not i % divisibility_arg_one and not i % divisibility_arg_two:
#             yield i

# result = list(get_good_numbers(divisibility_arg_two=10))
# print(result)


# итоговый результат в одну строку
print([i for i in range(20, 241) if not i % 20 and not i % 21])
