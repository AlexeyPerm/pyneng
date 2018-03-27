#!/usr/bin/env python3
"""
Найти индекс последнего вхождения элемента.
Например, для списка num_list, число 10 последний раз встречается с индексом 4; в
списке word_list, слово 'ruby' последний раз встречается с индексом 6.
Сделать решение общим (то есть, не привязываться к конкретному элементу в
конкретном списке) и проверить на двух списках, которые указаны и на разных
элементах.
Для этого надо запросить у пользователя сначала ввод числа из списка num_list и
затем вывести индекс его последнего появления в списке. А затем аналогично для
списка word_list.
"""

num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
num_input = int((input('Введите число:')))
num_reverse = num_list[::-1]
num_result = len(num_list) - (num_reverse.index(num_input) + 1)

print('Последнее вхождение числа: ', num_result)

word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
word_input = str((input('Введите число:')))
word_reverse = word_list[::-1]
word_result = len(word_list) - (word_reverse.index(word_input) + 1)

print('Последнее вхождение слова: ', word_result)

