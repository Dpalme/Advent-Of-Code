from os import read
from posixpath import realpath
from sys import stdout
from itertools import product
import heapq as heap


def first_part(graph, target):
    def neighbors(c):
        return (
            (c[0] + 1, c[1]),
            (c[0], c[1] + 1),
            (c[0] - 1, c[1]),
            (c[0], c[1] - 1)
        )

    def manh(c):
        return target[0] - c[0] + target[1] - c[1]

    queue = [(0, manh((0, 0)), (0, 0))]
    visited = {(0, 0)}
    while queue:
        [risk, _, curr] = heap.heappop(queue)
        for neighbor in neighbors(curr):
            if neighbor == target:
                return risk + graph[target]
            elif neighbor not in visited and neighbor in graph:
                visited.add(neighbor)
                heap.heappush(
                    queue, (graph[neighbor] + risk, manh(neighbor), neighbor))
    return -1


def second_part(graph, target):
    mx, my, ngraph = target[0] + 1, target[1] + 1, {}
    for dy, dx in product(range(0, 5), repeat=2):
        for y, x in product(range(mx), repeat=2):
            nsum = (graph[x, y] + dx + dy)
            ngraph[(dx*mx + x, dy*my + y)] = nsum % 9 if nsum > 9 else nsum
    return first_part(ngraph, (mx*5 - 1, my*5 - 1))


with open('2021/inputs/day15.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    ymax, xmax = len(lns) - 1, len(lns[0]) - 1
    nMap = {}
    for y, row in enumerate(lns):
        for x, v in enumerate(row):
            nMap[(x, y)] = int(v)
    stdout.write(f'Day 15\nFirst part: {first_part(nMap, (xmax, ymax))}\n')
    stdout.write(f'Second part: {second_part(nMap, (xmax, ymax))}\n')
