from sys import stdout


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
        arr, cnt = nmbrs[ind:ind + 1], 1
        while sum(arr) < curr:
            cnt += 1
            arr = nmbrs[ind:ind + cnt]
            if sum(arr) == curr:
                return min(arr) + max(arr)


with open('2020/inputs/day9.txt', 'r') as inp:
    nmbrs = [int(numb) for numb in inp.read().split('\n')]
    ind, curr = first_part(nmbrs)
    stdout.write(f'Day 9\nFirst part: {curr}\n')
    stdout.write(f'Second part: {second_part(nmbrs[:ind], ind, curr)}\n')
