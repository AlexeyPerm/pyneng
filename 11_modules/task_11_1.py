# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from pprint import pprint

def parse_cdp_neighbors(src_file):
    list = src_file.split('\n')
    local_device = list[0].split('>')[0]    # нулевую строку разделяем и берём первый элемент
    result = {}
    for line in list:
        if '/' in line:
            remote_device = line.split()[0]
            local_interface = line.split()[1] + line.split()[2]     # собираем интерфейс вида fa0/0
            remote_interface = line.split()[-2] + line.split()[-1]  # собираем интерфейс вида fa0/0.
            result[local_device, local_interface] = (remote_device, remote_interface)
    return result

# Если функция запускается как самостоятельный элемент, а не импортируется куда-то как модуль, то выполняется следующее
if __name__ == '__main__':
    with open('sw1_sh_cdp_neighbors.txt') as src:  # открывает указанный файл
        src_file = src.read()  # считываем открытый файл и кидаем его в переменную
    pprint(parse_cdp_neighbors(src_file))  # выводим результат работы функции, с аргументом file
