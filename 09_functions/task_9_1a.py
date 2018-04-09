# -*- coding: utf-8 -*-
'''
Ввести дополнительный параметр, который контролирует будет ли настроен port имя параметра 'psecurity'
по умолчанию значение False
Проверить работу функции на примере словаря access_dict, с генерацией
конфигурации port-security и без

'''

from pprint import pprint


def generate_access_config(access, psecurity=True):
    '''
    access - словарь access-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/12':10,
          'FastEthernet0/14':11,
          'FastEthernet0/16':17}

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''
    access_template = [
        'switchport mode access',
        'switchport access vlan',
        'switchport nonegotiate',
        'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]
    port_security = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]

    access_port = []

    for interface, vlan in access_dict.items():
        access_port.append(f'interface {interface}')
        for k in access_template:
            if k.endswith('vlan'):
                k = k + ' ' + str(vlan)
            access_port.append(k)
        if psecurity:
            for j in port_security:
                access_port.append(j)
    return access_port


access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

pprint(generate_access_config(access_dict))
