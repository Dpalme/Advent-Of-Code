from sys import stdout


def fold(paper: set, f_inst: list):
    for axis, v in f_inst:
        folded = tuple(filter(lambda a: a[axis] > v, paper))
        paper.difference_update(folded)
        for c in folded:
            paper.add((c[0], v - (c[axis] - v)) if axis else (v - (c[axis] - v), c[1]))
    for y in range(6):
        stdout.write(''.join('■' if (x,y) in paper else ' ' for x in range(39)) + '\n')
    return len(paper)


with open('2021/inputs/day13.txt', 'r') as inp:
    dots, f_inst = inp.read().rsplit('\n\n')
    paper = {tuple(map(int, dot.split(','))) for dot in dots.split('\n')}
    f_inst = tuple((inst[11] == 'y', int(inst[13:])) for inst in f_inst.splitlines())
    stdout.write(f'Day 13\nFirst part: {fold(paper, [f_inst[0]])}\n')
    stdout.write(f'Second part: {fold(paper, f_inst)}\n')
