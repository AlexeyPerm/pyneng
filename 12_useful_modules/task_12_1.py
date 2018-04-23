# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess


def check_ip_addresses(ip_address):
    ping_ok = []
    ping_not_ok = []

    for k in ip_address:
        reply = subprocess.run(['ping', '-c', '3', k],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
        if reply.returncode == 0:
            ping_ok.append(k)
        elif reply.returncode == 1:
            ping_not_ok.append(k)
    return ping_ok, ping_not_ok


if __name__ == '__main__':
    ip = ['8.8.8.8', '254.254.254.254', '1.1.1.1', '254.254.253.254']
    result = check_ip_addresses(ip)
    print(f'Available IP: {result[0]} \nUnavailable IP: {result[1]}')
