def cycle_fp(seats):
    copied = [[val for val in row] for row in seats]
    xmax, ymax = len(seats[0]), len(seats)
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1)]
    for y, row in enumerate(seats):
        for x, seat in enumerate(row):
            crowded = 0
            for i, j in dirs:
                if 0 <= x + i and x + i < xmax and 0 <= y + j and y + j < ymax:
                    crowded += 1 if seats[y + j][x + i] == '#' else 0

            if seat == 'L' and crowded == 0:
                copied[y][x] = '#'
            elif seat == '#' and crowded > 3:
                copied[y][x] = 'L'
    return copied


def first_part(input_data):
    seats = [[char for char in line] for line in input_data.split('\n')]
    res = None
    while res != seats:
        res = seats
        seats = cycle_fp(seats)
    return sum([sum([1 for val in row if val == '#']) for row in seats])


def cycle_sp(seats):
    copied = [[val for val in row] for row in seats]
    xmax, ymax = len(seats[0]), len(seats)
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1)]
    for y in range(ymax):
        for x, seat in enumerate(seats[y]):
            crowded = 0
            for i, j in dirs:
                dx, dy = x + i, y + j
                while 0 <= dx and dx < xmax and 0 <= dy and dy < ymax:
                    if seats[dy][dx] != '.':
                        crowded += 1 if seats[dy][dx] == '#' else 0
                        break
                    dx, dy = dx + i, dy + j

            if seat == 'L' and crowded == 0:
                copied[y][x] = '#'
            elif seat == '#' and crowded > 4:
                copied[y][x] = 'L'
    return copied


def second_part(input_data):
    seats = [[char for char in line] for line in input_data.split('\n')]
    res = None
    cont = 0
    while res != seats:
        cont += 1
        res = seats
        seats = cycle_sp(seats)
    return sum([sum([1 for val in row if val == '#']) for row in seats])


if __name__ == '__main__':
    with open('2020/inputs/day11.txt', 'r') as inp:
        input_string = inp.read()
        print('First part: %d' % first_part(input_string))
        print('Second part: %d' % second_part(input_string))
