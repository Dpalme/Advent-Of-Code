input_string = '1321131112'


def first_part(input_data=input_string):
    for itt in range(40):
        nxt = ""
        while input_data != "":
            count, curr = 1, input_data[0]
            for char in input_data[1:]:
                if curr == char:
                    count += 1
                else:
                    break
            nxt += str(count) + curr
            input_data = input_data[count:]
        input_data = nxt
    return len(input_data)


def second_part(input_data=input_string):
    for itt in range(50):
        nxt = ""
        while input_data != "":
            count, curr = 1, input_data[0]
            for char in input_data[1:]:
                if curr == char:
                    count += 1
                else:
                    break
            nxt += str(count) + curr
            input_data = input_data[count:]
        input_data = nxt
    return len(input_data)


if __name__ == '__main__':
    print('First part: %d' % first_part())
    print('Second part: %d' % second_part())
