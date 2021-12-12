from sys import stdout

gift = {
    "children": 3, "cats": 7,
    "samoyeds": 2, "pomeranians": 3,
    "akitas": 0, "vizslas": 0,
    "goldfish": 5, "trees": 3,
    "cars": 2, "perfumes": 1
}


def first_part(sues):
    for k, v in gift.items():
        for sue, sv in sues.copy().items():
            if k in sv and sv[k] != v:
                del sues[sue]
    return tuple(sues.keys())[0]


def second_part(sues):
    for k, v in gift.items():
        for sue, sv in sues.copy().items():
            if k in sv:
                if k in 'catstrees':
                    if sv[k] <= v:
                        del sues[sue]
                elif k in 'pomeraniansgoldfish':
                    if sv[k] >= v:
                        del sues[sue]
                elif sv[k] != v:
                    del sues[sue]
    return tuple(sues.keys())[0]



with open('2015/inputs/day16.txt', 'r') as inp:
    sues = {
        sue[:sue.find(':')].split()[1]:
        {
            q[:q.find(':')]:int(q[q.find(':') + 1:])
            for q in sue[sue.find(':') + 2:].split(', ')
        }
        for sue in inp.read().rsplit('\n')
    }
    stdout.write(f'Day 16\nFirst part: {first_part(sues.copy())}\n')
    stdout.write(f'Second part: {second_part(sues.copy())}\n')
