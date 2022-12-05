def fully_encloses(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1])


def first_part(assignments: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
    return sum(1 for a in assignments if fully_encloses(a[0], a[1]))


def overlaps(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return ((a[0] <= b[0] <= a[1]) or (b[0] <= a[0] <= b[1]) or
            (a[0] <= b[1] <= a[1]) or (b[0] <= a[1] <= b[1]))


def second_part(assignments: list[tuple[tuple[int, int], tuple[int, int]]]) -> int:
    return sum(1 for a in assignments if overlaps(a[0], a[1]))


if __name__ == '__main__':
    with open('./2022/inputs/day04.txt', 'r', encoding="UTF-8") as inp:
        assignments = (*map(lambda a: (*map(lambda b: (*map(int, b.split('-')),),
                       a.split(',')),), inp.read().split('\n')),)
        print(first_part(assignments))
        print(second_part(assignments))
