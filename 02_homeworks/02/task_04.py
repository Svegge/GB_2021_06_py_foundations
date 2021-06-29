'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''

user_str = input('Please enter some space separated words:\n >>> ')

word_list = user_str.split(' ')

print(word_list)

for i in word_list:
    if len(i) > 10:
        print(word_list.index(i) + 1, i[:10])
    else:
        print(word_list.index(i) + 1, i)
