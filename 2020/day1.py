from itertools import combinations


def first_part(numbers):
    for n in numbers:
        if 2020 - n in numbers:
            return n * (2020 - n)


def second_part(numbers):
    for n1, n2 in combinations(numbers, 2):
        if 2020 - n1 - n2 in numbers:
            return (2020 - n1 - n2) * n1 * n2


if __name__ == '__main__':
    with open('2020/inputs/day1.txt', 'r') as inp:
        numbers = set([int(x) for x in inp.readlines()])
        print('First part: %d' % first_part(numbers))
        print('Second part: %d' % second_part(numbers))
