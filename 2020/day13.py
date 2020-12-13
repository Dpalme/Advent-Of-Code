# region input_string
ttime = 939
tschedule = '7,13,x,x,59,x,31,19'
time = 1000434
schedule = '17,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,983,x,29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,23,x,x,x,x,x,x,x,397,x,x,x,x,x,37,x,x,x,x,x,x,13'
# endregion


def prod(nlist):
    carry = nlist[0]
    for numb in nlist[1:]:
        carry *= numb
    return carry


def invm(a, b):
    # https://github.com/MartinSeeler/Advent-of-Code-2020/blob/master/day13/day13_2.py
    return 0 if a == 0 else 1 if b % a == 0 else b - invm(b % a, a) * b//a


def first_part(input_time=time, input_schedule=schedule):
    busses = [int(x) for x in input_schedule.split(',') if x != "x"]
    min_bus, timm = 0, 1000950
    for bus in busses:
        if ((input_time // bus) + 1) * bus < timm:
            timm, min_bus = ((input_time // bus) + 1) * bus, bus
    return min_bus * (timm - input_time)


def second_part(input_schedule=schedule):
    # https://github.com/MartinSeeler/Advent-of-Code-2020/blob/master/day13/day13_2.py
    busses = [(int(x), idx)
              for idx, x in enumerate(input_schedule.split(",")) if x != "x"]
    N = prod([bs[0] for bs in busses])
    x = sum([bs[1] * (N//bs[0]) * invm(N//bs[0], bs[0]) for bs in busses])
    return N - x % N


if __name__ == '__main__':
    print('First part: %d' % first_part())
    print('Second part: %d' % second_part())
