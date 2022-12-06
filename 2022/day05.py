def parse_stacks(stacks_lines: str) -> list[list[str]]:
    separated_lines = stacks_lines.split('\n')
    number_of_stacks = separated_lines[-2].count('[')
    stacks = [[] for _ in range(number_of_stacks)]
    for line in separated_lines[:-1]:
        for stack, value in enumerate(line[1::4]):
            if value != ' ':
                stacks[stack].append(value)
    return stacks

def first_part(stacks: list[list[str]], instructions: list[str]):
    for instruction in instructions:
        semantics = instruction.split()
        n, source, destination = map(int, semantics[1::2])
        tmp = []
        for _ in range(n):
            tmp.append(stacks[source - 1].pop(0))
        stacks[destination - 1] = [*tmp[::-1], *stacks[destination - 1]]
    return ''.join(map(lambda a: a.pop(0), stacks))


def second_part(stacks: list[list[str]], instructions: list[str]):
    for instruction in instructions:
        semantics = instruction.split()
        n, source, destination = map(int, semantics[1::2])
        tmp = []
        for _ in range(n):
            tmp.append(stacks[source - 1].pop(0))
        stacks[destination - 1] = [*tmp, *stacks[destination - 1]]
    return ''.join(map(lambda a: a.pop(0), stacks))

if __name__ == '__main__':
    with open('./2022/inputs/test.txt', 'r', encoding="UTF-8") as inp:
        stacks, instructions = inp.read().split('\n\n')
        stacks, instructions = parse_stacks(stacks), instructions.split('\n')
        print(first_part([[*stack] for stack in stacks], instructions))
        print(second_part([[*stack] for stack in stacks], instructions))