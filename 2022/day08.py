from sys import stdout
import functools


def first_part(trees):
    def check_neighbors(x, y):
        def check_linear(dx, dy):
            try:
                if trees[(x, y)] <= trees[(x+dx, y+dy)]:
                    return False
            except KeyError:
                return True
            nx = dx // abs(dx) if dx else 0
            ny = dy // abs(dy) if dy else 0
            return check_linear(dx + nx, dy + ny)

        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            try:
                if trees[(x, y)] > trees[(x + dx, y + dy)]:
                    if check_linear(dx, dy):
                        return True
            except KeyError:
                return True
        return False
    return sum(check_neighbors(x, y) for x, y in trees.keys())


def second_part(trees):
    def check_neighbors(x, y):
        def check_linear(dx, dy):
            try:
                if trees[(x, y)] <= trees[(x+dx, y+dy)]:
                    return 1
            except KeyError:
                return 0
            nx = dx // abs(dx) if dx else 0
            ny = dy // abs(dy) if dy else 0
            return 1 + check_linear(dx + nx, dy + ny)

        sides = []
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            try:
                sides.append(check_linear(dx, dy))
            except KeyError:
                sides.append(0)
        return functools.reduce(lambda a, b: a*b, sides)
    return max(check_neighbors(x, y) for x, y in trees.keys())


with open('2022/inputs/day08.txt', 'r') as inp:
    trees = {}
    for y, row in enumerate(inp.read().rsplit('\n')):
        for x, tree in enumerate(row):
            trees[(x, y)] = int(tree)
    stdout.write(f'Day 8\nFirst part: {first_part(trees)}\n')
    stdout.write(f'Second part: {second_part(trees)}\n')
