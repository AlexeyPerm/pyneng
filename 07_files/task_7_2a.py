"""
Дополнить скрипт:
Скрипт не должен выводить команды, в которых содержатся слова, которые
указаны в списке ignore.
"""

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

with open(argv[1],'r') as f:    # Передали название файла скрипту
    for list in f:  # Перебираем каждую строку файла
        if list.startswith('!'):      # перепрыгнули через ! и пошли на начало цикла
            continue
        for k in ignore:    # перебираем элементы ignore
            if k in list:   # если есть в строке элемент из ignore, то прерываем цикл и переходит к след. строке.
                break
        else:
            print(list)
