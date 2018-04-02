"""
Переделать скрипт из задания 7.2b:

передавать как аргументы скрипту:
 имя исходного файла конфигурации
 имя итогового файла конфигурации
Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore. И затем записать оставшиеся строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.
"""

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

with open(argv[1], 'r') as f,  open(argv[2], 'w') as result:
    for list in f:
        for k in ignore:
            if k in list:
                break
        else:
            result.write(list)

