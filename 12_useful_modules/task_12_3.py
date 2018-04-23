# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''

from task_12_1 import check_ip_addresses
from task_12_2 import check_list_ip
from tabulate import tabulate


def ip_table(avail, unavail):
    ip_dict = {'Reachable': avail, 'Unreachable': unavail}

    return tabulate(ip_dict, headers='keys')


if __name__ == '__main__':
    ip_list = ['8.8.8.8', '1.1.1.1-1.1.1.3', '127.0.0.1-3', '2.2.2.2-2.2.2.4']
    result = check_ip_addresses(check_list_ip(ip_list))
    print(ip_table(result[0], result[1]))
