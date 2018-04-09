# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
            if k.startswith('switchport access'):
                access_ports[interface] = int(k.split()[-1])  # Если встречается строка, то кидаем в значение номер влан
            elif 'trunk allowed' in k:
                trunk_ports[interface] = [int(j) for j in k.split()[-1].split(',')]  # выковыриваем вланы
            elif 'switchport mode access' in k:     # если не первые два условия, то сработает это условие
                access_ports[interface] = int(1)    # закидываем в значение ключа единичку

    return access_ports, trunk_ports

pprint(get_int_vlan_map('config_sw2.txt'))  # pprint для удобства чтения. никаких переводов строки при этом нет

