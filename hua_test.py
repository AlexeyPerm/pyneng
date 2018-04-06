"""
Конфиг для замены коммутатора Dlink на Huawei.
"""
# вводим айпишник
ip_address = input('Введите IP-сети в формате: 10.1.1.0/24 : \n').split('/')
ip = ip_address[0].split('.')  # разделяем список на элементы b и берём IP

incorrect = 'Вы ввели ерунду :) '
correct_ip = False

while not correct_ip:  # Пока НЕ True , повторять цикл
    if len(ip) != 4:  # если кол-во октетов в айпишнике не равно 4, то выводится incorrect
        print(incorrect)
        ip = input('Введите ip-адрес ещё раз: ')
    for k in ip:  # проходимся по каждому октету и сравниваем его с нужными числами
        if not k.isdigit() and int(k) < 0 or int(k) > 255:
            print(incorrect)
            ip = input('Введите ip-адрес ещё раз: ')
            break
        else:
            correct_ip = True

prefix = ip_address[1]  # Взяли префикс

bin_mask = '1' * int(prefix) + '0' * (32 - int(prefix))  # перевели в двоичный формат маску
mask_octet1, mask_octet2, mask_octet3, mask_octet4 = bin_mask[0:8], bin_mask[8:16], bin_mask[16:24], bin_mask[24:32]

mask_int1 = int(mask_octet1, 2)  # перевели mask_octet в десятичную
mask_int2 = int(mask_octet2, 2)
mask_int3 = int(mask_octet3, 2)
mask_int4 = int(mask_octet4, 2)

first = int(ip[0]) & mask_int1  # первый октет IP + делаем побитовое И для "выключения" битов
second = int(ip[1]) & mask_int2
third = int(ip[2]) & mask_int3
fourth = int(ip[3]) & mask_int4
gw = f'{first}.{second}.{third}.{fourth + 1}'

# Конфигурация для management

if correct_ip == True:
    man_vlan = int((input('Enter Management VLAN \n')))
    if 1 < man_vlan < 4096:  # проверяем корректность ввода влана
        pass
    else:
        print(incorrect)
        man_vlan = int((input('Введите номер VLAN ещё раз \n')))

template_manage = f"""
vlan {man_vlan}
 description Uprava_{man_vlan}

interface Vlanif {man_vlan}
 ip address {ip_address[0]} {prefix}

ip route-static 0.0.0.0 0.0.0.0 {gw}

"""

# Создаём список вланов.

vlans = []  # создаём пустой список вланов
with open('import.txt') as src, open('test.txt','w') as dst:
    for string in src:    # перебираем каждую строку в файле
        if 'create' in string:
            tag = string.strip().split(' ')     # убрали перевод строк + разделили на элементы пробелом
            if int(tag[4]) == man_vlan:
                vlans.append(tag[4])
                continue
            else:
                vlans.append(tag[4])  # добавляем в созданный список вланы
                result_vlans = (f"vlan {tag[4]}\n"
                                f" description {tag[2]}\n")
                dst.write(result_vlans)
                print(result_vlans)

vlans_up = ' '.join(vlans)     # вставляем пробелы между элементами в строке и кидаем в переменную для uplink

# Выводим конфиг uplink-интерфейса

int_uplink = input('\nEnter Uplink: \n')
uplink_template = f"""
interface {int_uplink}
 description uplink
 port link-type trunk
 port trunk allow-pass vlan {vlans_up}
"""

with open('test.txt','a') as dst:
    dst.write(template_manage)
    dst.write(uplink_template)

print(template_manage, uplink_template)

