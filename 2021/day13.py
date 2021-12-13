from sys import stdout

class XYPlane(dict):
    def __init__(self):
        super().__init__()

    def coord(self, crd, val=None):
        if crd not in self:
            return -1
        if val is not None:
            self[crd] = val
        return self[crd]


def first_part(paper: set, f_inst: list):
    axis, v = 1 if f_inst[0][11] == 'y' else 0, int(f_inst[0][13:])
    folded = tuple(filter(lambda a: a[axis] > v, paper))
    paper = paper.difference(folded)
    for c in folded:
        paper.add((c[0], v - (c[axis] - v)) if axis else (v - (c[axis] - v), c[1]))
    return len(paper)


def second_part(paper: set, f_inst: list):
    for inst in f_inst:
        axis, v = 1 if inst[11] == 'y' else 0, int(inst[13:])
        folded = tuple(filter(lambda a: a[axis] > v, paper))
        paper = paper.difference(folded)
        for c in folded:
            paper.add((c[0], v - (c[axis] - v)) if axis else (v - (c[axis] - v), c[1]))
    for y in range(6):
        print(''.join('■' if (x,y) in paper else ' ' for x in range(39)))
    return len(paper)


with open('2021/inputs/day13.txt', 'r') as inp:
    dots, f_inst = inp.read().rsplit('\n\n')
    paper = {tuple(map(int, dot.split(','))) for dot in dots.split('\n')}
    f_inst = f_inst.splitlines()
    stdout.write(f'Day 13\nFirst part: {first_part(paper, f_inst)}\n')
    stdout.write(f'Second part: {second_part(paper, f_inst)}\n')
