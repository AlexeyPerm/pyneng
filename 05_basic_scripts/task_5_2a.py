#!/usr/bin/env python3

""" Пример выполнения скрипта:
Enter device name: r1
Enter parameter name: ios
15.4
"""

london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

device = london_co.get(input('Enter device name: '))  # Запросили ключ словаря через dict.get() и закинули его в device
result = device.get(input('Enter parameter name: '))  # Запрос ключа словаря device и запись его в result
print(result)