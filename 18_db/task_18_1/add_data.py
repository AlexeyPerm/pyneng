# -*- coding: utf-8 -*-
"""
Задание 18.1

add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах


В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора
 определяется по имени файла с данными

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
"""

import sqlite3
from create_db import create_db


def add_sw_data():
    """
    Добавляет в базу switches данные об имени и местоположении устройства
    Используются локальный переменные и импорт, поэтому в функцию
    не передаются никакие параметры и аргументы.
    """

    import yaml
    con = sqlite3.connect('dhcp_snooping.db')
    data = []

    with open('switches.yml') as f:
        template = yaml.load(f)
    for k in template['switches'].items():
        data.append(k)

    try:
        with con:
            query = 'INSERT into switches values (?, ?)'
            con.executemany(query, data)

    except sqlite3.IntegrityError as e:
        print('Error occured: ', e)
    con.close()


def add_dhcp_data():
    import re
    import glob

    dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
    con = sqlite3.connect('dhcp_snooping.db')
    result = []

    for file_name in dhcp_snoop_files:
        hostname = file_name.split('_')[0]

        with open(file_name) as data:
            for line in data:
                regex = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
                match = regex.search(line)
                if match:
                    mac, ip, vlan, interface = match.groups()
                    result.append((mac, ip, vlan, interface, hostname))

    for row in result:
        try:
            while con:
                query = 'INSERT into dhcp values (?, ?, ?, ?, ?)'
                con.executemany(query, row)
        except sqlite3.IntegrityError as e:
            print('Error occured: ', e)


if __name__ == '__main__':
    create_db()
    add_sw_data()
    add_dhcp_data()
