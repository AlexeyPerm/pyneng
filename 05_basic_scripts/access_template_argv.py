#!/usr/bin/env python3

from sys import argv

interface, vlan = argv[1:]  #срез списка. начинать со второго элемента списка. То есть с interface. 

access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))
