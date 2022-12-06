from sys import stdout


def detect_start(message: str, number_of_characters: int) -> int:
    for i, vals in enumerate(zip(*(message[n:]
                                   for n in range(number_of_characters)))):
        if len(set(vals)) == number_of_characters:
            return i + number_of_characters


def first_part(message):
    return detect_start(message, 4)


def second_part(message):
    return detect_start(message, 14)


with open('2022/inputs/day06.txt', 'r') as inp:
    message = inp.read()
    stdout.write(f'Day 6\nFirst part: {first_part(message)}\n')
    stdout.write(f'Second part: {second_part(message)}\n')
