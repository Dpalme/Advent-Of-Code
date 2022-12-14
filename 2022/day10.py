from sys import stdout


def first_part(lns):
    register = 1
    signals = []
    cycles = 0

    def cycle(signals, cycles, register):
        cycles += 1
        if cycles in (20, 60, 100, 140, 180, 220):
            signals.append(register * cycles)
        return cycles, signals

    for instruction in lns:
        cycles, signals = cycle(signals, cycles, register)
        if instruction != 'noop':
            cycles, signals = cycle(signals, cycles, register)
            register += int(instruction.split()[1])
    return sum(signals)


def second_part(lns):
    register = 1
    pointer = 0

    def cycle(pointer, register):
        print('██' if abs((pointer % 40) - (register % 40)) <= 1 else '░░', end='')
        pointer += 1
        if pointer % 40 == 0:
            print()
        return pointer

    for instruction in lns:
        pointer = cycle(pointer, register)
        if instruction != 'noop':
            pointer = cycle(pointer, register)
            register += int(instruction.split()[1])
    return -1


with open('2022/inputs/day10.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    stdout.write(f'Day 10\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
