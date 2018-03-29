"""
    Запросить у пользователя ввод IP-адреса в формате 10.0.1.1.
    Определить какому классу принадлежит IP-адрес.
    В зависимости от класса адреса, вывести на стандартный поток вывода:
        'unicast' - если IP-адрес принадлежит классу A, B или C
        'multicast' - если IP-адрес принадлежит классу D
        'local broadcast' - если IP-адрес равен 255.255.255.255
        'unassigned' - если IP-адрес равен 0.0.0.0
        'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):

    A: 1-127
    B: 128-191
    C: 192-223
    D: 224-239
"""

ip = input('Введите ip-адрес: ')
# bin_ip = bin(int(ip.replace('.','')))[2:]  # Переводим в двоичную систему. Убрал за ненадобностью
ip_first= int(ip.split('.')[0])     # Берём первый октет

if ip == '0.0.0.0':
    print('unassigned IP-address')
elif ip_first in range(1,128):
    print('Class A, unicast')
elif ip_first in range(128,192):
    print('Class B, unicast')
elif ip_first in range(192,224):
    print('Class B, unicast')
elif ip_first in range(224,240):
    print('Class D, multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
else:
    print('unused IP-address')


