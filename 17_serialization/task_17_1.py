# -*- coding: utf-8 -*-
"""
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает аргумент output в котором находится вывод команды sh version (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

Функция write_to_csv:
* ожидает два аргумента:
 * имя файла, в который будет записана информация в формате CSV
 * данные в виде списка списков, где:
    * первый список - заголовки столбцов,
    * остальные списки - содержимое
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает

Остальное содержимое скрипта может быть в скрипте, а может быть в ещё одной функции.

Скрипт должен:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в файл routers_inventory.csv

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
"""

import glob
import re
import csv

sh_version_files = glob.glob('sh_vers*')
# print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']


def parse_sh_version(output):
    ios_regex = r'Version (?P<ios>.+),'  # В конце обязательня запятая для отсечения этой же запятой из группы.
    image_regex = r'image file is "(?P<image>.+)"'  # двойные кавычки для отсечения их же из группы
    uptime_regex = r'uptime is (?P<uptime>.+)'

    ios = re.search(ios_regex, output).group('ios')  # закидываем в переменную нашу грппу
    image = re.search(image_regex, output).group('image')
    uptime = re.search(uptime_regex, output).group('uptime')

    return ios, image, uptime


def write_to_csv(file, data):
    with open(file, 'w') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


for file in sh_version_files:
    hostname = re.search(r'\w+_(.+)\.txt', file).group(1)
    with open(file) as f:
        ios, image, uptime = parse_sh_version(f.read())
        result = [[hostname, ios, image, uptime]]
        # print(result)

write_to_csv('routers_inventory.csv', result)
