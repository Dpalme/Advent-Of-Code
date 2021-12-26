import functools
from sys import stdout
import itertools


def alu(lns, model_number):
    registers = {'x': 0, 'y': 0, 'z': 0, 'w': 0, 'i': 0}
    def mul(a,b): registers[a] =  registers[a] *  registers[b]
    def add(a,b): registers[a] =  registers[a] +  registers[b]
    def div(a,b): registers[a] =  registers[a] // registers[b]
    def mod(a,b): registers[a] =  registers[a] %  registers[b]
    def eql(a,b): registers[a] = (registers[a] == registers[b]) << 0
    INSTRUCTIONS = {'mul': mul, 'add': add, 'div': div,'mod': mod, 'eql': eql}

    inp_counter = 0
    for inst, *reg in map(lambda a: a.split(), lns):
        if inst != 'inp':
            try:
                registers['i'] = int(reg[1])
                INSTRUCTIONS[inst](reg[0], 'i')
            except ValueError:
                INSTRUCTIONS[inst](*reg)
        else:
            registers[reg[0]] = int(model_number[inp_counter])
            inp_counter += 1
    return registers


def run_step(a,b,c, w, z):
    z1 = z//c
    if w == (z%26) + a:
        return z1
    else:
        return (z1 * 26) + w + b


def backward(A, B, C, z2, w):
    zs = []
    x = z2 - w - B
    if x % 26 == 0:
        zs.append(x//26 * C)
    if 0 <= w-A < 26:
        z0 = z2 * C
        zs.append(w-A+z0)
    return zs


def solve(ws, a, b, c):
    zs = {0}
    result = {}
    for A,B,C in zip(a[::-1], b[::-1], c[::-1]):
        newzs = set()
        for w,z in itertools.product(ws,zs):
            for z0 in backward(A, B, C, z, w):
                newzs.add(z0)
                result[z0] = (w,) + result.get(z, ())
        zs = newzs
    return ''.join(str(digit) for digit in result[0])


def first_part(a,b,c):
    return solve(range(1, 10), a, b, c)


def second_part(a,b,c):
    return solve(range(9, 0, -1), a, b, c)


def get_consts(stages):
    stage_sets = tuple(map(set, (stage.split('\n') for stage in stages)))
    repeating_lines = functools.reduce(lambda a,b: a.intersection(b), stage_sets)
    a,b,c = [], [], []
    for stage in stage_sets:
        stage.difference_update(repeating_lines)
        stage.discard('')
        for ln in stage:
            inst, reg, v = ln.split()
            if inst == 'div':
                c.append(int(v))
            elif reg == 'y':
                b.append(int(v))
            else:
                a.append(int(v))
    return a, b, c


with open('2021/inputs/day24.txt', 'r') as inp:
    stages = inp.read().rsplit('inp w\n')[1:]
    a,b,c = get_consts(stages)
    stdout.write(f'Day 24\nFirst part: {first_part(a,b,c)}\n')
    stdout.write(f'Second part: {second_part(a,b,c)}\n')
