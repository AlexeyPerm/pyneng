# ip = ['8.8.8.8', '254.254.254.254', '1.1.1.1-10', '254.254.253.254']

ip_list = ['10.1.1.1-10','127.0.0.1-127.0.0.5']
#ip_list = ['10.1.1.1-10']
for ip in ip_list:
    if '-' in ip:
        ip_begin = ip.split('-')[0].rsplit('.', maxsplit=1)[0]
        if len(ip.split('-')[1]) > 3:
            ip = ip.split('-')
            rng = []
            for j in ip:
                rng.append(j.rsplit('.', maxsplit=1)[-1])
        else:
            rng = ip.rsplit('.', maxsplit=1)[1].split('-')
        octet_range = [i for i in range(int(rng[0]), int(rng[1]) + 1)]

    # if '-' in ip and len(ip.split('-')[1]) > 3:
    #     ip_1, ip_2 = ip.split('-')
    #     last_octet1 = ip_1.split('.')[-1]
    #     last_octet2 = ip_2.split('.')[-1]
    # elif '-' in ip:
    #     ip_begin = ip.rsplit('.', maxsplit=1)[0]
    #     octet_range = ip.rsplit('.', maxsplit=1)[1].split('-')

# def check_list_ip(ip_list):
#     for ip in ip_list:
#         if '-' in ip.rsplit('.', maxsplit=1)[1]:
#             ip_list.remove(ip)
#             ip_first = ip.rsplit('.', maxsplit=1)[0]
#             ip_end = ip.rsplit('.', maxsplit=1)[1].split('-')
#             octet_range = [i for i in range(int(ip_end[0]), int(ip_end[1]) + 1)]
#             # print(octet_range)
#             for k in octet_range:
#                 ip_list.append(ip_first + '.' + str(k))
#     return ip_list
# print(check_list_ip(ip_list))