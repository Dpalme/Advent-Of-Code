def first_part(input_data, offset=25):
    numbers = [int(numb) for numb in input_data.split('\n')]
    for index, curr in enumerate(numbers[offset:]):
        prev_24 = numbers[index: index + offset]
        for numb in prev_24:
            if curr - numb in prev_24:
                break
        else:
            return curr
    return -1


def second_part(input_data, offset=25):
    numbers = [int(numb) for numb in input_data.split('\n')]
    for index, curr in enumerate(numbers[offset:]):
        prev_24 = numbers[index: index + offset]
        for numb in prev_24:
            if curr - numb in prev_24:
                break
        else:
            sub_arr = numbers[:index]
            for ind in range(len(sub_arr)):
                itt_arr = sub_arr[ind:]
                while sum(itt_arr) > curr:
                    itt_arr = itt_arr[:-1]
                    if sum(itt_arr) == curr:
                        return min(itt_arr) + max(itt_arr)
    return -1


if __name__ == '__main__':
    with open('2020/inputs/day9.txt', 'r') as inp:
        input_string = inp.read()
        print('First part: %d' % first_part(input_string))
        print('Second part: %d' % second_part(input_string))
