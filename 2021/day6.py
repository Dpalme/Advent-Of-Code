from sys import stdout

def first_part(fish):
    for day in range(80):
        fish[0], fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7], fish[8] = fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7] + \
            fish[0], fish[8], fish[0]
    return sum(fish.values())


def second_part(fish):
    for day in range(256-80):
        fish[0], fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7], fish[8] = fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7] + \
            fish[0], fish[8], fish[0]
    return sum(fish.values())


with open('2021/inputs/day6.txt', 'r') as inp:
    fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for ln in map(int, inp.read().split(',')):
        fish[ln] += 1
    stdout.write(f'Day 1\nFirst part: {first_part(fish)}\n')
    stdout.write(f'Second part: {second_part(fish)}\n')
