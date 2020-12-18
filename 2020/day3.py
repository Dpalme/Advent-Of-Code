with open('2020/inputs/day3.txt', 'r') as inp:
    lines = inp.readlines()


def check_slope(right, down):
    pos, trees = 0, 0
    for line in range(0, len(lines), down):
        trees += 1 if lines[line][pos % 31] == "#" else 0
        pos += right
    return trees


def first_part():
    return check_slope(3, 1)


def second_part():
    return (check_slope(1, 1) * check_slope(3, 1) *
            check_slope(5, 1) * check_slope(7, 1) * check_slope(1, 2))


if __name__ == "__main__":
    print('First part: %d' % first_part())
    print('Second part: %d' % second_part())
