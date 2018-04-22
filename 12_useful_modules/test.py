# ip = ['8.8.8.8', '254.254.254.254', '1.1.1.1-10', '254.254.253.254']

ip_list = ['8.8.8.8-9','1.2.3.4-10', '254.254.254.254', '127.0.0.1-10']
i = len(ip_list)
while i > 0:
    for ip in ip_list:
        if '-' in ip.rsplit('.', maxsplit=1)[1]:
            ip_list.remove(ip)
            ip_list1 = []
            ip_first = ip.rsplit('.', maxsplit=1)[0]
            ip_end = ip.rsplit('.', maxsplit=1)[1].split('-')
            octet_range = [i for i in range(int(ip_end[0]), int(ip_end[1]) + 1)]
            #print(octet_range)
            for k in octet_range:
                ip_list.append(ip_first + '.' + str(k))

    i -= 1
print(ip_list)
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