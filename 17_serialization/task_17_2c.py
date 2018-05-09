# -*- coding: utf-8 -*-
"""
Задание 17.2c

С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

Не копировать код функции draw_topology.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_2c_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""
from draw_network_graph import draw_topology
import yaml
from pprint import pprint

result = {}
with open("topology.yaml") as f:
    templates = yaml.load(f)

# Вытаскиваем ключи и значения словарей, чтобы сделать нужного вида словарь для draw_topology. Пока только это придумал.
for k in templates:
    for local_device, a in k.items():
        for local_int, b in a.items():
            for remote_dev, remote_int in b.items():
                break
            result[local_device, local_int] = (remote_dev, remote_int)

# проверка на дублирование линков.
for j in list(result.values()):
    if j in result.keys() and result[j] in result.keys():
        del(result[j])

draw_topology(result)

