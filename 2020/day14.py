from collections import Counter


def first_part(input_data):
    lines = input_data.split('\n')
    mem, mask = {}, []
    for line in lines:
        res = line.split()
        if 'mem' in line:
            adrs, val = res[0][4:-1], bin(int(res[2]))[2:]
            val = "0" * (len(mask) - len(val)) + val
            mem[adrs] = int("".join([mask[ind] if itm != "X" else val[ind]
                                     for ind, itm in enumerate(mask)]), base=2)
        else:
            mask = [x for x in res[2]]
    return sum(mem.values())


def iterations(res):
    x_count = Counter(res[0])['X']
    for i in range(x_count):
        for entry in res.copy():
            zero, one, ind = entry.copy(), entry.copy(), entry.index('X')
            zero[ind], one[ind] = '0', '1'
            res.remove(entry)
            res.extend([one, zero])
    return [int("".join(entry), base=2) for entry in res]


def second_part(input_data):
    mem, mask, lines = {}, [], input_data.split('\n')
    for line in lines:
        res = line.split()
        if 'mem' in line:
            adrs, val = bin(int(res[0][4:-1]))[2:], int(res[2])
            adrs = "0" * (len(mask) - len(adrs)) + adrs
            res = [adrs[ind] if mask[ind] == "0" else mask[ind]
                   for ind in range(len(mask))]
            mem.update({address: val for address in iterations([res])})
        else:
            mask = [x for x in res[2]]
    return sum([val for val in mem.values()])


if __name__ == '__main__':
    with open('2020/inputs/day14.txt', 'r') as inp:
        input_string = inp.read()
        print('First part: %d' % first_part(input_string))
        print('Second part: %d' % second_part(input_string))
