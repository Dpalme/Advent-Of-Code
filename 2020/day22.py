from sys import stdout
from copy import deepcopy


def get_score(deck):
    return sum(x * (i + 1) for i, x in enumerate(deck[::-1]))


def first_part(dcks):
    while [] not in dcks:
        vls = tuple(x.pop(0) for x in dcks)
        dcks[vls[0] < vls[1]].extend(vls[::2*(vls[0] > vls[1])-1])
    return get_score([*dcks[0], *dcks[1]])


def rec_cmbt(dcks):
    rounds = set()
    while [] not in dcks:
        r_hash = {tuple(dcks[0]), tuple(dcks[1])}
        if rounds.intersection(r_hash) != set():
            return True
        rounds.update(r_hash)

        vls = tuple(x.pop(0) for x in dcks)
        winner = (rec_cmbt([dcks[0][:vls[0]], dcks[1][:vls[1]]])
                  if (len(dcks[0]) >= vls[0] and len(dcks[1]) >= vls[1])
                  else vls[0] > vls[1])
        dcks[not winner].extend(vls[::2*winner-1])
    return dcks[1] == []


def second_part(dcks):
    rec_cmbt(dcks)
    return get_score([*dcks[0], *dcks[1]])


with open('2020/inputs/day22.txt', 'r') as inp:
    dcks = tuple([int(x) for x in i.split('\n')[1:]]
                 for i in inp.read().split('\n\n'))
    stdout.write(f'Day 22\nFirst part: {first_part(deepcopy(dcks))}\n')
    stdout.write(f'Second part: {second_part(dcks)}\n')
