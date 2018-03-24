#!/usr/bin/env python3

""" При запросе параметра, должен отображаться список возможных параметров
Enter device name: r1
Enter parameter name (ios,model,vendor,location,ip): ip
10.255.0.1
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

# device.get - запрос значения ключа словаря device. input() - показывает возможные ключи словаря
result = device.get(input('Enter parameter name (' + device_keys + '):'))
print(result)

