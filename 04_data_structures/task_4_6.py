ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route = ospf_route.replace(',','').split() #заменяем запятые пробелами и разделяем значения пробелами.
ospf_route.remove('via')
O = ospf_route[0].replace('O','OSPF')
Prefix = ospf_route[1]
AD = ospf_route[2].strip('[]')                  #удалили квадратные скобки в начале и конце
NextHop = ospf_route[3]
LUpd = ospf_route[4]
OutInt = ospf_route[5]

#создаём "шаблон"
view_ospf_route = """
Protocol:              {O}
Prefix:                {Pref}
AD/Metric:             {AD}
Next-Hop:              {Next}
Last update:           {Lupd}
Outbound Interface:    {Out}
"""

#форматируем вывод, используя "шаблон"
print(view_ospf_route.format(O = O, Pref = Prefix, AD = AD, Next = NextHop, Lupd = LUpd, Out = OutInt))