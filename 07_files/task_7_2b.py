# -*- coding: utf-8 -*-
'''
Задание 7.2b
Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt
При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']
#result = open('config_sw1_cleared.txt', 'w')

with open(argv[1], 'r') as f,  open('config_sw1_cleared.txt', 'w') as result:    # Передали название файла скрипту
    for list in f:  # Перебираем каждую строку файла
        if list.startswith('!'):      # перепрыгнули через ! и пошли на начало цикла for
            continue
        for k in ignore:    # перебираем элементы ignore
            if k in list:   # если есть в строке элемент из ignore, то прерываем цикл и переходит к след. строке.
                break
        else:
            result.write(list)
#result.close()

