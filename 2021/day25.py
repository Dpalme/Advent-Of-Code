from sys import stdout


def first_part(init_right, init_down, y_max, x_max):
    moved, i = True, 0
    def update(right_facing, down_facing):
        new_right, new_down = set(), set()
        f_check = right_facing.union(down_facing)
        for crd in right_facing:
            if ((crd[0] + 1) % x_max, crd[1]) in f_check:
                new_right.add(crd)
            else:
                new_right.add(((crd[0] + 1) % x_max, crd[1]))
        s_check = new_right.union(down_facing)
        for crd in down_facing:
            if (crd[0], (crd[1] + 1) % y_max) in s_check:
                new_down.add(crd)
            else:
                new_down.add((crd[0], (crd[1] + 1) % y_max))
        return new_right, new_down, right_facing.union(down_facing) != new_right.union(new_down)
    while moved:
        init_right, init_down, moved = update(init_right, init_down)
        i += 1
    return i


with open('2021/inputs/day25.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    y_max, x_max = len(lns), len(lns[0])
    right_facing, down_facing = set(), set()
    for y, row in enumerate(lns):
        for x, v in enumerate(row):
            if v == '>':
                right_facing.add((x,y))
            elif v == 'v':
                down_facing.add((x,y))

    stdout.write(f'Day 25\nFirst part: {first_part(right_facing, down_facing, y_max, x_max)}\n')
