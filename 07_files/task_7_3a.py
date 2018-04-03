"""
Дополнить скрипт:
    Отсортировать вывод по номеру VLAN
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
# решение подсмотрел.

result_list = []

with open('CAM_table.txt', 'r') as list:
    for k in list:
        if '.' in k:    # если в строке есть точка, то
            vlan, mac, _, intf = k.split()  # присваиваем переменным элементы строки k.split()
            unsorted = '{vlan:6} {mac}   {intf}'.format(vlan=vlan, mac=mac, intf=intf) # форматированое присваивание переменной элементов
            result_list.append(unsorted)    # добавлять к result_list вёс новые и новые элементы

result_list.sort()      # сортируем
for k in result_list:   # выводим каждый элемент в новой строке.
    print(k)