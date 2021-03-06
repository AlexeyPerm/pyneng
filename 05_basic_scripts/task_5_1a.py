#!/usr/bin/env python3
'''Если пользователь ввел адрес хоста, а не адрес сети, то
надо адрес хоста преобразовать в адрес сети и вывести адрес сети и маску
'''

#Вводим IP. Разбиваем список на элементы слешем
ip_address = input('Введите IP-сети в формате: 10.1.1.0/24 :\n').split('/')
IP = ip_address[0].split('.')       #разделяем список на элементы
prefix = ip_address[1]              #Взяли префикс

#количество единичек в маске = префиксу. Кол-во нулей: 32 - перфикс.
bin_mask = '1' * int(prefix) + '0'*(32 - int(prefix))       #перевели в двоичный формат маску
mask_octet1, mask_octet2, mask_octet3, mask_octet4 = bin_mask[0:8], bin_mask[8:16], bin_mask[16:24], bin_mask[24:32]

mask_int1 = int(mask_octet1, 2)       #перевели mask_octet в десятичную
mask_int2 = int(mask_octet2, 2)       #перевели mask_octet в десятичную
mask_int3 = int(mask_octet3, 2)       #перевели mask_octet в десятичную
mask_int4 = int(mask_octet4, 2)       #перевели mask_octet в десятичную

first  = int(IP[0]) & mask_int1     #первый октет IP + делаем побитовое И для "выключения" битов
second = int(IP[1]) & mask_int2     #второй октет IP + делаем побитовое И для "выключения" битов
third  = int(IP[2]) & mask_int3     #третий октет IP + делаем побитовое И для "выключения" битов
fourth = int(IP[3]) & mask_int4     #четвёртый октет IP + делаем побитовое И для "выключения" битов

network_template = """Network:
{first:<8} {second:<8} {third:<8} {fourth:<8}
{first:08b} {second:08b} {third:08b} {fourth:08b}
Mask:
/{prefix}
{mask_int1:<8} {mask_int2:<8} {mask_int3:<8} {mask_int4:<8}
{mask_octet1} {mask_octet2} {mask_octet3} {mask_octet4}
""".format(first = first, second = second, third = third, fourth = fourth, prefix = prefix,
mask_octet1 = mask_octet1, mask_octet2 = mask_octet2, mask_octet3 = mask_octet3, mask_octet4 = mask_octet4,
mask_int1 = mask_int1, mask_int2 = mask_int2, mask_int3 = mask_int3, mask_int4 = mask_int4)

print(network_template)