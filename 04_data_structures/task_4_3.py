CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
config = CONFIG.split()   #разбили строку на части. по умолчанию разделитель 
VLANS = config[-1].split(',') #разбили строку на части через запятую, чтобы был вид ['1', '3', '10], а не ['1,3,10']
print(VLANS)

