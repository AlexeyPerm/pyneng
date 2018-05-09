# -*- coding: utf-8 -*-
"""
Задание 15.3b

Проверить работу функции parse_cfg из задания 15.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 15.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""

import re


def parse_cfg(config):
    regex = (r'interface (?P<intf>\S+)'
             r'| ip address (?P<ip>[\d.]+ [\d.]+)')

    result = []
    with open(config) as f:
        match_iter = re.finditer(regex, f.read())
        for match in match_iter:
            if match.lastgroup == 'intf':
                interface = match.group(match.lastgroup)
                result[interface] = []
            elif interface:
                result[interface].append(match.group('ip'))
    return {key: result[key] for key in result if result[key]}


if __name__ == '__main__':
    print(parse_cfg('/home/rustok/git/pyneng/15_module_re/config_r2.txt'))
