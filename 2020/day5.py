from sys import stdout


def get_sids(inp_str):
    inp_str = inp_str.replace('F', '0').replace(
        'B', '1').replace('L', '0').replace('R', '1')
    return set([int(ln[:7], base=2) * 8 + int(ln[7:], base=2)
                for ln in inp_str.split('\n')])


def second_part(sids):
    for sid in range(len(sids)):
        if sid not in sids and sid-1 in sids and sid+1 in sids:
            return sid


with open('2020/inputs/day5.txt', 'r') as inp:
    sids = get_sids(inp.read())
    stdout.write(f'Day 5\nFirst part: {max(sids)}\n')
    stdout.write(f'Second part: {second_part(sids)}\n')
