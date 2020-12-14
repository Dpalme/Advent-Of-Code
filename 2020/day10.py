def first_part(input_data):
    adapts = set([int(nbr) for nbr in input_data.split('\n')])
    adds = [0, 0, 0, 1]
    for adap in adapts:
        adds[adap - adds[0]] += 1
        adds[0] = adap
    return adds[1] * adds[3]


def second_part(input_data):
    adapts = sorted([0] + [int(nbr) for nbr in input_data.split('\n')])
    acum = [1] + [0 for i in range(len(adapts) - 1)]
    for ind in range(len(adapts)):
        acum[ind] += sum([acum[ind2] for ind2, imp in enumerate(adapts[:ind])
                          if adapts[ind] - adapts[ind2] <= 3])
    return acum[-1]


if __name__ == '__main__':
    with open('2020/inputs/day10.txt', 'r') as inp:
        input_string = inp.read()
        print('First part: %d' % first_part(input_string))
        print('Second part: %d' % second_part(input_string))
