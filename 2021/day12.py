from sys import stdout
from collections import Counter


def first_part(caves):
    routes = []
    queue = {('start',)}
    while len(queue):
        path = queue.pop()
        if path[-1] == 'end':
            routes.append(path)
            continue
        for neighbor in caves[path[-1]]:
            if neighbor[0].islower() and neighbor in path:
                continue
            queue.add((*path, neighbor))
    return len(routes)


def second_part(caves):
    routes = set()
    queue = {('start',)}
    while len(queue):
        path = queue.pop()
        if path[-1] == 'end':
            routes.add(path)
            continue
        for neighbor in caves[path[-1]]:
            if neighbor == 'start' or (neighbor[0].islower() and neighbor in path and Counter(filter(lambda a: a.islower(), path)).most_common(1)[0][1] > 1):
                continue
            queue.add((*path, neighbor))
    return len(routes)


with open('2021/inputs/day12.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    caves = {}
    for c in lns:
        f, t = c.split('-')
        if f not in caves:
            caves[f] = set()
        if t not in caves:
            caves[t] = set()
        caves[f].add(t)
        caves[t].add(f)
    stdout.write(f'Day 12\nFirst part: {first_part(caves)}\n')
    stdout.write(f'Second part: {second_part(caves)}\n')
