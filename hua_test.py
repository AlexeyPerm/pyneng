
ip_address = input('Введите IP-сети в формате: 10.1.1.0/24 : \n').split('/')
ip = ip_address[0].split('.')       # разделяем список на элементы
prefix = ip_address[1]              # Взяли префикс

bin_mask = '1' * int(prefix) + '0'*(32 - int(prefix))       # перевели в двоичный формат маску
mask_octet1, mask_octet2, mask_octet3, mask_octet4 = bin_mask[0:8], bin_mask[8:16], bin_mask[16:24], bin_mask[24:32]

mask_int1 = int(mask_octet1, 2)       # перевели mask_octet в десятичную
mask_int2 = int(mask_octet2, 2)
mask_int3 = int(mask_octet3, 2)
mask_int4 = int(mask_octet4, 2)
mask = '{}.{}.{}.{}'.format(mask_int1, mask_int2, mask_int3, mask_int4)

first  = int(ip[0]) & mask_int1     # первый октет IP + делаем побитовое И для "выключения" битов
second = int(ip[1]) & mask_int2
third  = int(ip[2]) & mask_int3
fourth = int(ip[3]) & mask_int4
gw = '{}.{}.{}.{}'.format(first,second,third, fourth+1)

incorrect = 'Вы ввели ерунду :) '
correct_ip = False

while not correct_ip:       # Пока НЕ True , повторять цикл
    if len(ip) != 4:   # если кол-во октетов в айпишнике не равно 4, то выводится incorrect
        print(incorrect)
        ip = input('Введите ip-адрес ещё раз: ')
    for k in ip:       # проходимся по каждому октету и сравниваем его с нужными числами
        if not k.isdigit() and int(k) < 0 or int(k) > 255:
            print(incorrect)
            ip = input('Введите ip-адрес ещё раз: ')
            break
        else:
            correct_ip = True


if correct_ip == True:
    man_vlan = int((input('Enter Management VLAN \n')))
    if 1 < man_vlan < 4096:     # проверяем корректность ввода влана
        pass
    else:
        print(incorrect)
        man_vlan = int((input('Введите номер VLAN ещё раз \n')))

template_manage = """
vlan {man_vlan}
 description Uprava_{man_vlan}

interface Vlanif {man_vlan}
 ip address {ip_address} {mask}
 
ip route-static 0.0.0.0 0.0.0.0 {gw}

""".format(man_vlan = man_vlan, ip_address = ip_address[0], mask = mask, gw=gw)

print(template_manage)