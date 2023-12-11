from sys import stdout
import functools
import collections

ORDER = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')

ORDER2 = ('A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J')


def highest_count(cards_count: dict[str, int]):
    return max(c for f, c in cards_count.items() if f != 'J')


@functools.lru_cache(None)
def get_base_strength(labels, stage=1):
    card_count = collections.Counter(labels)
    if stage == 2:
        if 'J' in card_count:
            if card_count['J'] == 5:
                return 6
            max_count = highest_count(cards_count=card_count)
            highest = sorted(filter(
                lambda a: a[1] == max_count and a[0] != 'J',
                card_count.most_common()),
                key=lambda a: 12 - ORDER2.index(a[0]),
                reverse=True)[0][0]
            card_count[highest] += card_count['J']
            del card_count['J']
    found = []
    for v in card_count.values():
        if v == 5:
            return 6
        if v == 4:
            return 5
        if v == 3:
            found.append(3)
        if v == 2:
            found.append(2)
    if 3 in found:
        if 2 in found:
            return 4
        return 3
    if len(found) == 2:
        return 2
    if 2 in found:
        return 1
    return 0


def order_by_face(h1, h2, stage=1):
    for i in range(5):
        o1, o2 = ORDER.index(h1[0][i]), ORDER.index(h2[0][i])
        if stage == 2:
            o1, o2 = ORDER2.index(h1[0][i]), ORDER2.index(h2[0][i])
        if o1 > o2:
            return False
        if o2 > o1:
            return True


def update_jokers(hand: tuple[str, str]):
    cards, bet = hand
    card_count = collections.Counter(cards)
    cards.replace('J', card_count.most_common(1)[0][0])
    return (cards, bet)


def compare_strength(h1, h2, stage=1):
    h1_s, h2_s = get_base_strength(
        h1[0], stage=stage), get_base_strength(h2[0], stage=stage)
    if h1_s > h2_s:
        return 1
    if h1_s < h2_s:
        return -1
    orders = order_by_face(h1, h2, stage=stage)
    orders = (orders * 2) - 1
    return orders


def first_part(hands):
    hands = sorted(hands,
                   key=functools.cmp_to_key(compare_strength))
    return sum(int(hand[1])*(i+1)
               for i, hand in enumerate(hands))


def second_part(hands):
    hands = sorted(hands,
                   key=functools.cmp_to_key(
                       functools.partial(compare_strength, stage=2)))
    return sum(int(hand[1])*(i+1)
               for i, hand in enumerate(hands))


with open('2023/inputs/day07.txt', 'r') as inp:
    lns = inp.read().rsplit('\n')
    hands = tuple(map(
        lambda a: a.split(' '),
        lns
    ))
    stdout.write(f'Day 7\nFirst part: {first_part(hands)}\n')
    stdout.write(f'Second part: {second_part(hands)}\n')
