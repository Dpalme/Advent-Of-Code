from sys import stdout


class XYPlane(dict):
    def __init__(self):
        super().__init__()

    def touch(self, x, y):
        coord = f'{x} {y}'
        if coord in self:
            self[coord] += 1
        else:
            self[coord] = 1
    
    def __str__(self) -> str:
        sb = "  0123456789"
        for y in range(10):
            sb += f'\n{y} '
            for x in range(10):
                coord = f'{x} {y}'
                sb += str(self[coord]) if coord in self else '.'
        return sb + '\n'


def first_part(lns):
    nMap = XYPlane()
    for ln in lns:
        x, y = zip(*(map(int, p.split(',')) for p in ln.split(' -> ')))
        if x[0] == x[1]:
            for i in range(min(y), max(y) + 1):
                nMap.touch(x[0], i)
        elif y[0] == y[1]:
            for i in range(min(x), max(x) + 1):
                nMap.touch(i, y[0])
    return len(tuple(filter(lambda x: x > 1, nMap.values())))


def second_part(lns):
    nMap = XYPlane()
    for ln in lns:
        x, y = zip(*(map(int, p.split(',')) for p in ln.split(' -> ')))
        if x[0] == x[1]:
            for i in range(min(y), max(y) + 1):
                nMap.touch(x[0], i)
        elif y[0] == y[1]:
            for i in range(min(x), max(x) + 1):
                nMap.touch(i, y[0])
        else:
            for i in range(0, (max(x) - min(x)) + 1):
                nMap.touch(
                    x[0] + (i * (1 - (2 * (x[0] > x[1])))),
                    y[0] + (i * (1 - (2 * (y[0] > y[1])))))
    return len(tuple(filter(lambda x: x > 1, nMap.values())))


with open('2021/inputs/day5.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    stdout.write(f'Day 5\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
