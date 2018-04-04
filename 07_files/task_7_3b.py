"""
    Запросить у пользователя ввод номера VLAN.
    Выводить информацию только по указанному VLAN.
"""


vlan_num = input('Введиде номер VLAN: ')
with open('CAM_table.txt', 'r') as list:
    for k in list:  # перебираем каждую строку в файле
        if '.' in k: # если есть точка, то
            vlan, mac, _, intf = k.split()
            result = vlan,mac,intf   # закинули в result другие переменные
            if result[0] == vlan_num:   # если нулевой элемент равен введённому влану, что выводим 1 и 2 элемены
                print(result[1], result[2])
