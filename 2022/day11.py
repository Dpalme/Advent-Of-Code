from sys import stdout
import re
import math


class Monkey:
    def __init__(self, items, op, test, true, false) -> None:
        self.items = [*map(int, items.split(', '))]
        self.op = op
        self.test = int(test)
        self.true = int(true)
        self.false = int(false)
        self.inspected = 0

    def __repr__(self) -> str:
        return str(self.items)


def monkey_see(monkeys: list[Monkey], rounds: int, relief: int):
    mod_factor = math.prod(monkey.test for monkey in monkeys)

    def inspect(monkey: Monkey):
        while len(monkey.items):
            old = monkey.items.pop(0)
            worry = eval(monkey.op) // relief
            if rounds >= 1000:
                worry %= mod_factor
            next_monkey = monkey.true if worry % monkey.test == 0 else monkey.false
            next_monkey = monkeys[next_monkey]
            next_monkey.items.append(worry)
            monkey.inspected += 1

    for _ in range(rounds):
        for monkey in monkeys:
            inspect(monkey)
    return max(a.inspected * b.inspected for a in monkeys for b in monkeys if a != b)

def first_part(monkeys):
    return monkey_see(monkeys, 20, 3)


def second_part(monkeys):
    return monkey_see(monkeys, 10_000, 1)


with open('2022/inputs/day11.txt', 'r') as inp:
    lns = inp.read()
    monkeys_data = re.findall(
        r'''Monkey \d+:
  Starting items: ((?:\d+|,\s)+)
  Operation: new = (old [+*] (?:\d+|old))
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)''',
        lns)
    monkeys = [Monkey(*data) for data in monkeys_data]
    stdout.write(f'Day 11\nFirst part: {first_part(monkeys)}\n')
    monkeys = [Monkey(*data) for data in monkeys_data]
    stdout.write(f'Second part: {second_part(monkeys)}\n'),
