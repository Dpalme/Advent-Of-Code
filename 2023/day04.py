from sys import stdout

import re
import collections


def get_number_of_matches(have_numbers: set[int], winning_numbers: set[int]):
    return len(have_numbers.intersection(winning_numbers))


def process_card(card):
    card_info, numbers = card.split(':')
    card_number = int(re.findall(r'\d+', card_info)[0])
    winning, have = numbers.split(' | ')
    winning_numbers = set(map(int, re.findall(r'\d+', winning)))
    have_numbers = set(map(int, re.findall(r'\d+', have)))
    return winning_numbers, have_numbers, card_number


def first_part(lns):
    def get_card_value(card):
        winning_numbers, have_numbers, _ = process_card(card)
        matches = get_number_of_matches(have_numbers=have_numbers,
                                        winning_numbers=winning_numbers)
        return 2 ** (matches) >> 1
    return sum(map(get_card_value, lns))


def second_part(lns):
    cards = collections.defaultdict(lambda: 0)
    largest_actual_card = 1
    for card in lns:
        winning_numbers, have_numbers, card_number = process_card(card)
        cards[card_number] += 1
        matches = get_number_of_matches(have_numbers=have_numbers,
                                        winning_numbers=winning_numbers)
        for i in range(1, matches + 1):
            cards[card_number + i] += cards[card_number]
        if card_number > largest_actual_card:
            largest_actual_card = card_number
    for number in range(largest_actual_card, max(cards.keys())):
        del cards[number + 1]
    return sum(cards.values())


with open('2023/inputs/day04.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    stdout.write(f'Day 4\nFirst part: {first_part(lns)}\n')
    stdout.write(f'Second part: {second_part(lns)}\n')
