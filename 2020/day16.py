from re import search
from sys import stdout


def parse_input(inp_str):
    secs = [ln for ln in inp_str.split('\n\n')]
    classes, avb = {}, set()
    for line in secs[0].split('\n'):
        rs = search(r'(.*)[:]\s(\d*)-(\d*)\sor\s(\d*)-(\d*)', line)
        c_range = set([*range(int(rs.group(2)), int(rs.group(3))+1),
                       *range(int(rs.group(4)), int(rs.group(5))+1)])
        classes[rs.group(1)] = c_range
        avb.update(c_range)
    return classes, secs[2].split('\n')[1:], avb, secs[1].split('\n')[1]


def first_part(tckts, avb):
    return sum(int(n)*(int(n) not in avb) for t in tckts for n in t.split(','))


def second_part(classes, tckts, avb, tckt):
    for ticket in tckts.copy():
        for data in ticket.split(','):
            if int(data) not in avb:
                tckts.remove(ticket)

    # split ticket numbers into their positions
    clss_rng = {i: [] for i, _ in enumerate(classes)}
    for ticket in tckts:
        for ind, val in enumerate(ticket.split(',')):
            clss_rng[ind].append(int(val))

    # create a list of all possible classes for each number group
    for t_class, values in clss_rng.items():
        poss_classes = set(classes.keys())
        for poss_class in poss_classes.copy():
            curr_range = classes[poss_class]
            for value in values:
                if value not in curr_range:
                    poss_classes.remove(poss_class)
                    break
        clss_rng[t_class] = poss_classes

    # remove duplicates from possible classes
    available = set(classes.keys())
    for clas, posses in sorted(clss_rng.items(), key=lambda x: len(x[1])):
        for poss in posses.copy():
            if poss in available:
                available.remove(poss)
            else:
                clss_rng[clas].remove(poss)

    # get values from own ticket
    my_ticket = {clss_rng[i].pop(): int(n) for i, n in enumerate(
                 tckt.split(','))}
    accum = 1
    for name, value in my_ticket.items():
        accum *= value if 'departure' in name else 1
    return accum


with open('2020/inputs/day16.txt', 'r') as inp:
    classes, tckts, avb, tckt = parse_input(inp.read())
    stdout.write(f'Day 16\nFirst part: {first_part(tckts, avb)}\n')
    stdout.write(f'Second part: {second_part(classes, tckts, avb, tckt)}\n')
