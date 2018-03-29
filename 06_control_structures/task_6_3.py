"""
Сделать аналогичный генератор конфигурации для портов trunk.

В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать, что с ними делать.

Поэтому в соответствии каждому порту стоит список и первый (нулевой) элемент списка указывает как воспринимать номера
VLANов, которые идут дальше:

    add - значит VLANы надо будет добавить (команда switchport trunk allowed vlan add 10,20)
    del - значит VLANы надо удалить из списка разрешенных (команда switchport trunk allowed vlan remove 17)
    only - значит, что на интерфейсе должны остаться разрешенными только указанные VLANы
(команда switchport trunk allowed vlan 11,30)

Задача для портов 0/1, 0/2, 0/4:

    сгенерировать конфигурацию на основе шаблона trunk_template
    с учетом ключевых слов add, del, only
"""

access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'},
            'trunk':{'0/1':['add','10','20'],
                     '0/2':['only','11','30'],
                     '0/4':['del','17']} }

for intf, vlan in fast_int['access'].items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))


for intf_t, list_t in fast_int['trunk'].items():    # Перебор значений ключа 'trunk'. Значение закидываем в переменные
    vlan_t = str([int(a) for a in list_t[1:]]).strip('[]')  # Обработка списка list_t. Закидываем в переменную элементы, начиная со второго, убираем скобки, делаем их int.
    print('interface FastEthernet' + intf_t)
    for command_t in trunk_template:    # Перебираем шаблон
        if command_t.endswith('allowed vlan'):  # Если заканчивается на 'allowed vlan', то
            for k in list_t:    # переборка списка list_t. Upd:Переборку смысла делать нет. Нужно переделать!!!
                if k == 'add':  # если в списке есть 'add', то...
                    print(' {} add {}'.format(command_t, vlan_t))
                elif k == 'del':
                    print(' {} remove {}'.format(command_t, vlan_t))
                elif k == 'only':
                    print(' {} {}'.format(command_t, vlan_t))
        else:
            print(' {}'.format(command_t))
