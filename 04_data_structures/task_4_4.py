command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

"""   разбиваем строку на части (разделитель - пробел. [-1] - обратились к последнему значению. 
split - последнее значение разбили на части через запятую:
OUT[] ['1', '3', '10', '20', '30', '100']  
"""
command11 = command1.split()[-1].split(',')  
command22 = command2.split()[-1].split(',')

#Так как значения  являются str, то нужно преобразовать их в int
vlan1 = [int(vlan) for vlan in command11]
vlan2 = [int(vlan) for vlan in command22]

vlan = list(set(vlan1) & set(vlan2))  #находим пересечение множеств set() & set() и перобразуем в list (список)

print(vlan)  #выводим vlan

#print(vlan, type(vlan))   # выводим влан и тип vlan


