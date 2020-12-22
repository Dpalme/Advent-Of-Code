from collections import Counter
from sys import stdout


def first_part(lines):
    mem, mask = {}, None
    for cmd, _, val in lines:
        if 'mem' in cmd:
            adrs, val = cmd[4:-1], bin(int(val))[2:]
            val = "0" * (len(mask) - len(val)) + val
            mem[adrs] = int("".join(mask[ind] if itm != "X" else val[ind]
                                    for ind, itm in enumerate(mask)), base=2)
        else:
            mask = tuple(x for x in val)
    return sum(mem.values())


def iterations(res):
    x_count = Counter(res[0])['X']
    for i in range(x_count):
        for entry in res.copy():
            zero, one, ind = entry.copy(), entry.copy(), entry.index('X')
            zero[ind], one[ind] = '0', '1'
            res.remove(entry)
            res.extend([one, zero])
    return tuple(int("".join(entry), base=2) for entry in res)


def second_part(lines):
    mem, mask = {}, None
    for cmd, _, val in lines:
        if 'mem' in cmd:
            adrs, val = bin(int(cmd[4:-1]))[2:], int(val)
            adrs = "0" * (len(mask) - len(adrs)) + adrs
            res = [adrs[i] * (mask[i] == "0") + mask[i] * (mask[i] != "0")
                   for i in range(len(mask))]
            mem.update({address: val for address in iterations([res])})
        else:
            mask = tuple(x for x in val)
    return sum(mem.values())


with open('2020/inputs/day14.txt', 'r') as inp:
    inp_str = [tuple(ln.split()) for ln in inp.readlines()]
    stdout.write(f'Day 14\nFirst part: {first_part(inp_str)}\n')
    stdout.write(f'Second part: {second_part(inp_str)}\n')
