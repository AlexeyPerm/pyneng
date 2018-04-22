# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''


import subprocess


def check_ip_addresses(ip_address):

    ping_ok = []
    ping_not_ok = []

    for k in ip_address:
        if '-' in k.split('.'):

            reply = subprocess.run(['ping', '-c', '1', k],
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL)
        if reply.returncode == 0:
            ping_ok.append(k)
        elif reply.returncode == 1:
            ping_not_ok.append(k)
    return ping_ok, ping_not_ok


def check_list_ip(list_ip):

    for k in list_ip:
        if '-' in k.rsplit('.', maxsplit=1)[1]:
            k = k.rsplit('.', maxsplit=1)
            a = [i for i in range(int(k[1].split('-')[0]), int(k[1].split('-')[1]) + 1)]
            print(a)


if __name__ == '__main__':
    ip = ['8.8.8.8', '254.254.254.254', '1.1.1.1', '254.254.253.254']
    result = check_ip_addresses(ip)
    print(f'Available IP: {result[0]} \nUnavailable IP: {result[1]}')
