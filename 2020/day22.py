from sys import stdout
from copy import deepcopy


def get_score(decks):
    return sum(x*(i+1) for i, x in enumerate([*decks[0], *decks[1]][::-1]))


def first_part(decks):
    while [] not in decks:
        vls = tuple(x.pop(0) for x in decks)
        decks[vls[0] < vls[1]].extend(vls[::2*(vls[0] > vls[1])-1])
    return get_score(decks)


def rec_cmbt(decks):
    rounds = set()
    while [] not in decks:
        r_hash = {tuple(decks[0]), tuple(decks[1])}
        if rounds.intersection(r_hash) != set():
            return True
        rounds.update(r_hash)

        vls = tuple(x.pop(0) for x in decks)
        winner = (rec_cmbt([decks[0][:vls[0]], decks[1][:vls[1]]])
                  if len(decks[0]) >= vls[0] and len(decks[1]) >= vls[1]
                  else vls[0] > vls[1])
        decks[not winner].extend(vls[::2*winner-1])
    return decks[1] == []


def second_part(decks):
    rec_cmbt(decks)
    return get_score(decks)


with open('2020/inputs/day22.txt', 'r') as inp:
    decks = tuple([int(x) for x in i.split('\n')[1:]]
                 for i in inp.read().split('\n\n'))
    stdout.write(f'Day 22\nFirst part: {first_part(deepcopy(decks))}\n')
    stdout.write(f'Second part: {second_part(decks)}\n')
