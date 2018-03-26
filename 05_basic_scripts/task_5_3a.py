#!/usr/bin/env python3

"""
в зависимости от выбранного режима, должны задаваться разные вопросы в запросе о номере VLANа или списка VLANов:
для access: 'Enter VLAN number:'
для trunk: 'Enter allowed VLANs:'
"""

access_template = [
    'switchport mode access',
    'switchport access vlan {}',
    'switchport nonegotiate',
    'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q',
    'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]


int_mode = {'access': access_template,
            'trunk':trunk_template}  # Создаём словарь, значения ключей которого будут наши шаблоны.

req_vlan = {'access' : 'Enter VLAN number: ',
            'trunk' : 'Enter allowed VLANs: '}    #Создаём словарь, значения которого соответствуют условию задачи


req_mode = input('Enter interface mode (access/trunk): ')   # Вводим режим работы порта. Введёное значение будет являться ключом созданных выше словарей.
interface = input('Enter interface type and number: ')
vlan = input(req_vlan[req_mode])    # Обращаемся к значению словаря req_vlan, ключом которого будет введёное ранее значение в req_mode

print('\ninterface {}'.format(interface))
print('\n'.join(int_mode[req_mode]).format(vlan))   # вывод значения ключа int_mode, которое является шаблоном.