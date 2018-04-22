#ip = ['8.8.8.8', '254.254.254.254', '1.1.1.1-10', '254.254.253.254']

ip = ['1.1.1.1-10']
for k in ip:
    if '-' in k.rsplit('.', maxsplit=1)[1]:
        k = k.rsplit('.', maxsplit=1)
        a = [i for i in range(int(k[1].split('-')[0]), int(k[1].split('-')[1])+1)]
        print(a)

