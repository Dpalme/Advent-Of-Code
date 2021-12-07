from sys import stdout

def first_part(fish):
    for day in range(80):
        fish[0], fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7], fish[8] = fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7] + \
            fish[0], fish[8], fish[0]
    return sum(fish)


def second_part(fish):
    for day in range(256-80):
        fish[0], fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7], fish[8] = fish[1], fish[2], fish[3], fish[4], fish[5], fish[6], fish[7] + \
            fish[0], fish[8], fish[0]
    return sum(fish)


with open('2021/inputs/day6.txt', 'r') as inp:
    fish = [0]*9
    for days in map(int, inp.read().split(',')):
        fish[days] += 1
    stdout.write(f'Day 6\nFirst part: {first_part(fish)}\n')
    stdout.write(f'Second part: {second_part(fish)}\n')
