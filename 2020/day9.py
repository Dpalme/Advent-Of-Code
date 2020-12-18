def first_part(nmbrs, off=25):
    for ind, curr in enumerate(nmbrs[off:]):
        prev = set(nmbrs[ind: ind + off])
        for numb in prev:
            if curr - numb in prev:
                break
        else:
            return (ind, curr)


def second_part(nmbrs, ind, curr, off=25):
    nmbrs = list(reversed(nmbrs))
    for ind in range(ind):
        cnt = 1
        arr = nmbrs[ind:ind + cnt]
        while sum(arr) < curr:
            cnt += 1
            arr = nmbrs[ind:ind + cnt]
            if sum(arr) == curr:
                return min(arr) + max(arr)


if __name__ == '__main__':
    with open('2020/inputs/day9.txt', 'r') as inp:
        nmbrs = [int(numb) for numb in inp.read().split('\n')]
        ind, curr = first_part(nmbrs)
        print('First part: %d' % curr)
        print('Second part: %d' % second_part(nmbrs[:ind], ind, curr))
