def find_common(top_compartment: str, bottom_compartment: str) -> str:
    sec = set(bottom_compartment)
    for element in top_compartment:
        if element in sec:
            return element


def get_compartments(collection: str) -> tuple[str, str]:
    mid = len(collection) >> 1
    return collection[:mid], collection[mid:]


def get_priority(character: str) -> int:
    return ord(character) - (ord('a') if not character.istitle() else ord('A') - 26) + 1


def first_part(rucksacks: list[str]) -> int:
    return sum(map(get_priority, map(lambda a: find_common(*a), map(get_compartments, rucksacks))))


def find_badge(elf1: str, elf2: str, elf3: str) -> str:
    elf2, elf3 = set(elf2), set(elf3)
    for el in elf1:
        if el in elf2 and el in elf3:
            return el

def second_part(rucksacks: list[str]) -> int:
    return sum(map(get_priority, map(lambda a: find_badge(*a),
    zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3]))))


if __name__ == '__main__':
    with open('./2022/inputs/day03.txt', 'r', encoding="UTF-8") as inp:
        rucksacks = inp.read().split('\n')
        print(first_part(rucksacks))
        print(second_part(rucksacks))
