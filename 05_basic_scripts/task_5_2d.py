#!/usr/bin/env python3

""" 
При запросе параметра пользователь может вводить название параметра в любом регистре
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
device_keys = ','.join(device)      # Разделяем каждый элемент строки запятыми, чтобы не было всяких кавычек и прочего

# Методом get() запрашиваем ключ. Если он есть, то заносим его значение в result, в противном случае
# возвращается не None, а значение "такого параметра нет" и это значение попадает в result.
# Метод lower() для возможности ввода параметра в любом регистре
param = input('Enter parameter name (' + device_keys + '):')
result = device.get((param.lower()), 'Такого параметра нет')
print(result)
