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

# Для Python3.6 и выше, так как используются f-строки

import subprocess


def check_list_ip(ip_list):
    """ Функция проверяет, присутствует ли диапазон айпишников
    в каком-либо элементе списка. While используется, чтобы
    делать проверку для каждого элемента списка, так как диапазонов
    может быть несколько. Возвращает обновлённый список.
    Пример: Было ip_list = ['12.3.4.5-7]
            Стало ip_list = ['12.3.4.5', '12.3.4.6', '12.3.4.7']

    """
    i = len(ip_list)
    while i > 0:
        for ip in ip_list:
            if '-' in ip.rsplit('.', maxsplit=1)[1]:    # сплитить начинаем справа и только один раз.
                ip_list.remove(ip)  # удаляем прошедший провеку элемент,
                ip_first = ip.rsplit('.', maxsplit=1)[0]
                ip_end = ip.rsplit('.', maxsplit=1)[1].split('-')
                octet_range = [i for i in range(int(ip_end[0]), int(ip_end[1]) + 1)]    # "разбиваем" диапазон
                for k in octet_range:
                    ip_list.append(ip_first + '.' + str(k))
        i -= 1
    return ip_list


def check_ip_addresses(ip_address):
    ping_ok = []
    ping_not_ok = []

    for k in ip_address:
        reply = subprocess.run(['ping', '-c', '1', k],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
        if reply.returncode == 0:
            ping_ok.append(k)
        elif reply.returncode == 1:
            ping_not_ok.append(k)
    return ping_ok, ping_not_ok


if __name__ == '__main__':
    # ip_list = ['8.8.8.8', '254.254.254.254', '1.1.1.1', '127.0.0.1-4', '254.254.253.254']
    ip_list = ['8.8.8.8', '254.254.254.250-252', '1.1.1.1-3', '127.0.0.1-4', '254.254.253.255']
    result = check_ip_addresses(check_list_ip(ip_list))
    print(f'Available IP: {result[0]} \nUnavailable IP: {result[1]}')
