import re
from pprint import pprint


def parse_sh_cdp_neighbors(output):
    loc_host = re.search('(\w+)>', output).group(1)
    neighbors = {}
    # На данный момент в душе не ебу как быть с WS-C3750, чтобы он сука попадал под шаблон
    regexp = '(?P<rem_host>\S+) +(?P<loc_intf>\S+ ?\S+) +\d+ +.*?\d+ +(?P<rem_intf>\S+ ?\S+)'
    for line in output.split('\n'):
        match = re.search(regexp, line)
        if match:
            rem_host, loc_intf, rem_intf = match.groups()
            neighbors[loc_intf] = {rem_host: rem_intf}

    return {loc_host: neighbors}

if __name__ == "__main__":
    with open('sh_cdp_n_sw1.txt', 'r') as f:
        pprint(parse_sh_cdp_neighbors(f.read()))