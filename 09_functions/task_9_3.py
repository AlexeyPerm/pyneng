# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from pprint import pprint


def get_int_vlan_map(config_file):
    with open(config_file) as src:
        config = {}
        for line in src:  # Пробегаемся по каждой строке в файле
            if line.startswith('interface'):  # Ищем строку, где встречается нужно слово
                interface = line.split(' ')[1].strip()
                config[interface] = []  # создаём пустой словарь, где ключ interface
            elif line.startswith(' '):
                config[interface].append(line.strip())  # Добавляем в словарь значения (конфиг интерфейса)

    trunk_ports = {}
    access_ports = {}

    for interface, comand in config.items():  # закидываем в переменные ключ и значения словаря
        for k in comand:
            if str(k).startswith('switchport access'):
                access_ports[interface] = int(k.split()[-1])  # Если встречается строка, то кидаем в значение номер влан
            elif 'trunk allowed' in k:
                trunk_ports[interface] = [int(j) for j in k.split()[-1].split(',')]  # выковыриваем вланы

    return access_ports, trunk_ports

pprint(get_int_vlan_map('config_sw1.txt'))  # pprint для удобства чтения. никаких переводов строки при этом нет

