def first_part(elfs: list[list[int]]) -> int:
    return max(map(sum, elfs))


def second_part(elfs: list[list[int]]) -> int:
    elfs = [*map(sum, elfs)]
    top_three_elfs = []
    for _ in range(3):
        top_three_elfs.append(max(elfs))
        elfs.remove(max(elfs))
    return sum(top_three_elfs)


if __name__ == '__main__':
    with open('./2022/inputs/day01.txt', 'r', encoding="UTF-8") as inp:
        elfs = [*map(lambda a: [*map(int, a.split())],
                     inp.read().split('\n\n'))]
        print(first_part(elfs))
        print(second_part(elfs))
