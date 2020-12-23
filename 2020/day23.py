from sys import stdout as std


def play(start, cups, rounds):
    highest, pivot = len(cups), start
    for i in range(rounds):
        t1 = cups[pivot]
        t2 = cups[t1]
        t3 = cups[t2]
        three, cups[pivot] = (t1, t2, t3), cups[t3]
        nxt = pivot - 1
        while nxt in three or nxt < 1:
            nxt -= 1
            if nxt < 1:
                nxt = highest
        cups[nxt], cups[t3], pivot = t1, cups[nxt], cups[pivot]
    return cups


def first_part(cups, strt, end):
    cups[end] = strt
    cups = play(strt, cups, 100)
    curr, data = 1, []
    for _ in range(1, len(cups)):
        data.append(str(cups[curr]))
        curr = cups[curr]
    return ''.join(data)


def second_part(cups, start, end):
    nxt = len(inp_str) + 1
    cups[end], cups[1000000] = nxt, strt
    cups.update({i: i+1 for i in range(nxt, 1000000)})
    cups = play(strt, cups, 10000000)
    n1 = cups[1]
    return n1 * cups[n1]


with open('2020/inputs/day23.txt', 'r') as inp:
    inp_str = tuple((int(x) for x in inp.read()))
    cups = {n: inp_str[i+1] for i, n in enumerate(inp_str[:-1])}
    strt, end = inp_str[0], inp_str[-1]
    std.write('Day 23\nFirst part: ')
    std.write(f'{first_part(cups.copy(), strt, end)}\nSecond part: ')
    std.write(f'{second_part(cups, strt, end)}')
