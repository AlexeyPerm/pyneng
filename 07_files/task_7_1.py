# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.


'''


with open('ospf.txt','r') as txt:
    for ospf_route in txt:
        ospf_route = ospf_route.replace(',', '').split()  # заменяем запятые пробелами и разделяем значения пробелами.
        ospf_route.remove('via')
        O = ospf_route[0].replace('O', 'OSPF')
        Prefix = ospf_route[1]
        AD = ospf_route[2].strip('[]')  # удалили квадратные скобки в начале и конце
        NextHop = ospf_route[3]
        LUpd = ospf_route[4]
        OutInt = ospf_route[5]

        # создаём "шаблон"
        view_ospf_route = """
        Protocol:              {O}
        Prefix:                {Pref}
        AD/Metric:             {AD}
        Next-Hop:              {Next}
        Last update:           {Lupd}
        Outbound Interface:    {Out}
        """

        # форматируем вывод, используя "шаблон"
        print(view_ospf_route.format(O=O, Pref=Prefix, AD=AD, Next=NextHop, Lupd=LUpd, Out=OutInt))