from sys import stdout


def first_part(inp_str):
    return sum(len(set((le for le in f.replace('\n', '')))) for f in inp_str)


def second_part(inp_str):
    return sum(len(set.intersection(*(set(f)
                                      for f in fs.split('\n'))))
               for fs in inp_str)


with open('2020/inputs/day6.txt', 'r') as inp:
    inp_str = inp.read().split('\n\n')
    stdout.write(f'Day 6\nFirst part: {first_part(inp_str)}\n')
    stdout.write(f'Second part: {second_part(inp_str)}\n')
