input_string = 'vzbxkghb'


def debg(numbers):
    print(numbers)
    for ind in range(len(numbers[:-2])):
        print(numbers[:-2])
        print(numbers[ind] == numbers[ind + 1], numbers[ind + 1] == numbers[ind + 2])


def check_valid(numbers):
    letters = 8 not in numbers * 14 not in numbers * 11 not in numbers
    straight, pair = 1, 0
    for ind in range(len(numbers[:-2])):
        straight *= 0 if (numbers[ind] + 1 == numbers[ind + 1]) * (
            numbers[ind] + 2 == numbers[ind + 2]) else 1
        pair += (numbers[ind] == numbers[ind + 1]) + \
            (numbers[ind + 1] == numbers[ind + 2])
    return letters * (not straight) * (pair >= 2)


def first_part(input_data=input_string):
    numbers = [(ord(char) - 97) for char in input_data]
    print(numbers)
    numbers[-1] += 1
    while not check_valid(numbers):
        numbers[-1] += 1
        for ind in reversed(range(len(numbers))):
            if numbers[ind] > 25:
                numbers[ind - 1] += 1
                numbers[ind] = 0
    debg(numbers)
    return "".join([chr(num + 97) for num in numbers])


def second_part(input_data=input_string):
    for char in input_data:
        pass
    return 0


if __name__ == '__main__':
    print('First part: %s' % first_part('ghijklmn'))
    print('Second part: %s' % second_part())
