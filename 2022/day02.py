GAME = {'A': 1, 'B': 2, 'C': 3}


def play_first_game(p1_pick: str, p2_pick: str) -> int:
    if p1_pick == p2_pick:
        return 3 + GAME[p2_pick]
    if p2_pick == 'A':
        if p1_pick == 'B':
            return GAME[p2_pick]
        if p1_pick == 'C':
            return 6 + GAME[p2_pick]
    if p2_pick == 'B':
        if p1_pick == 'A':
            return 6 + GAME[p2_pick]
        if p1_pick == 'C':
            return GAME[p2_pick]
    if p2_pick == 'C':
        if p1_pick == 'A':
            return GAME[p2_pick]
        if p1_pick == 'B':
            return 6 + GAME[p2_pick]


def play_second_game(p1_pick: str, game_res: str) -> int:
    CASES = ('A', 'B', 'C')
    RESULTS = ('X', 'Y', 'Z')
    p2_pick = CASES[(CASES.index(p1_pick) + (RESULTS.index(game_res)) - 1) % 3]
    return play_first_game(p1_pick, p2_pick)


def first_part(guide: tuple[tuple[str, str]]) -> int:
    return sum(play_first_game(p1, p2.replace('X', 'A')
                               .replace('Y', 'B')
                               .replace('Z', 'C')) for p1, p2 in guide)


def second_part(guide: tuple[tuple[str, str]]) -> int:
    return sum(play_second_game(p1, p2) for p1, p2 in guide)


if __name__ == '__main__':
    with open('./2022/inputs/day02.txt', 'r', encoding="UTF-8") as inp:
        elfs = (*map(lambda a: (*a.split(),),
                     inp.read().split('\n')),)
        print(first_part(elfs))
        print(second_part(elfs))
