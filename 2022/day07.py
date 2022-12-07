from sys import stdout
from functools import lru_cache


class AOCFile():
    def __init__(self, name: str, size: int) -> None:
        self.size = size
        self.name = name

    def __str__(self):
        return f'- {self.name} (file, size={self.size})'


class Directory(dict):
    def __init__(self, name: str, parent=None) -> None:
        super()
        self.parent = parent
        self.name = name

    @property
    @lru_cache(None)
    def size(self):
        return sum(element.size for element in self.values())

    def __str__(self):
        return '\n'.join((f'- {self.name} (dir)', *(str(el) for el in self.values())))

    def __repr__(self):
        return '\n'.join((f'- {self.name} (dir)', *(str(el) for el in self.values())))

    def __hash__(self):
        return int(''.join(map(str, map(ord, self.name))))


def build_file_structure(commands: list[list[str]]) -> dict[str, Directory]:
    directories = {'/': Directory('/')}
    current_dir = directories['/']
    for command in commands:
        # print(current_dir, command)
        if command[0] == '$':
            if command[1] == 'cd':
                if command[2] == '/':
                    current_dir = directories['/']
                elif command[2] == '..':
                    current_dir = current_dir.parent
                else:
                    current_dir[command[2]] = Directory(
                        command[2], current_dir)
                    current_dir = current_dir[command[2]]
        else:
            if command[0].isdigit():
                current_dir[command[1]] = AOCFile(
                    command[1], int(command[0]))
            else:
                current_dir[command[1]] = Directory(command[1])
    return directories


def calculate_directory_sizes(directories: dict[str, Directory]):
    sizes = []
    dirs = [directories['/']]
    while True:
        if len(dirs) == 0:
            break
        directory = dirs.pop()
        for el in directory.values():
            if isinstance(el, Directory):
                dirs.append(el)
        sizes.append(directory.size)
    return sizes


def first_part(commands: list[list[str]]):
    directories = build_file_structure(commands)
    sizes = calculate_directory_sizes(directories)
    return sum(filter(lambda a: a < 100000, sizes))


def second_part(commands):
    directories = build_file_structure(commands)
    sizes = calculate_directory_sizes(directories)
    HDD = 70000000
    UPDATE_SIZE = 30000000
    free = HDD - directories['/'].size
    print(directories['/'].size, free)
    dirs = [directories['/']]
    while True:
        if len(dirs) == 0:
            break
        directory = dirs.pop()
        for el in directory.values():
            if isinstance(el, Directory):
                dirs.append(el)
        sizes.append(directory.size)
    return min(filter(lambda a: free + a >= UPDATE_SIZE, sizes))


with open('2022/inputs/day07.txt', 'r') as inp:
    commands = (*map(lambda a: a.split(), inp.read().rsplit('\n')),)
    stdout.write(f'Day 7\nFirst part: {first_part(commands)}\n')
    stdout.write(f'Second part: {second_part(commands)}\n')
