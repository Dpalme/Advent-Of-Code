from sys import stdout
import re
import itertools


def process_line(line):
    return (*map(int, re.findall(r'\d+', line)),)


class Range:
    def __init__(self, start, _range) -> None:
        self.start = start
        self.range = _range
        self.end = self.start + self.range

    def in_range(self, value):
        return self.start <= value <= self.end


class Transform:
    def __init__(self, destination, source, reach) -> None:
        self.range = Range(source, reach)
        self.destination = destination
        self.diff = self.destination - self.range.start


class Map:
    def __init__(self, section) -> None:
        lines = section.split('\n')
        metadata = lines[0][:-5]
        self.source, self.destination = metadata.split('-to-')
        self.transforms = [
            Transform(*process_line(line))
            for line in lines[1:]
        ]

    def transform(self, number):
        for transform in self.transforms:
            if transform.range.in_range(number):
                return number + transform.diff
        return number


TRANSLATION_PATH = (('seed', 'soil'),
                    ('soil', 'fertilizer'),
                    ('fertilizer', 'water'),
                    ('water', 'light'),
                    ('light', 'temperature'),
                    ('temperature', 'humidity'),
                    ('humidity', 'location'))


def translate_seed_to_location(seed_number, translation_maps):
    current_value = seed_number
    for step in TRANSLATION_PATH:
        current_value = translation_maps[step].transform(current_value)
    return current_value


def build_maps(maps) -> dict[tuple[str, str], Map]:
    translation_maps = {}
    for map_section in maps:
        new_map = Map(map_section)
        translation_maps[(new_map.source, new_map.destination)] = new_map
    return translation_maps


def first_part(seeds, maps):
    translation_maps = build_maps(maps)
    return min(translate_seed_to_location(seed, translation_maps)
               for seed in seeds)


def second_part(seeds, maps):
    seed_pairs = tuple(zip(seeds[::2], seeds[1::2]))
    translation_maps = build_maps(maps)

    def min_location_from_seed_range(seed_range):
        def mapping(stage, seed_range):
            ranges = []
            for t in translation_maps[stage].transforms:
                translated_seed = t.diff + seed_range.start
                if (t.range.start <= seed_range.start < t.range.end and
                        t.range.start <= seed_range.end <= t.range.end):
                    ranges.append(
                        Range(translated_seed, seed_range.range))
                    seed_range.range = 0
                elif (t.range.start <= seed_range.start < t.range.end and
                      t.range.end < seed_range.end):
                    range_difference = t.range.end - seed_range.start - 1
                    ranges.append(Range(translated_seed, range_difference))
                    seed_range.range -= range_difference
                    seed_range.start = t.range.end
                elif (seed_range.start < t.range.start and
                      t.range.start <= seed_range.end <= t.range.end):
                    range_difference = seed_range.end - t.range.start
                    ranges.append(
                        Range(t.diff + t.range.start, range_difference))
                    seed_range.range -= range_difference
            if seed_range.range != 0:
                ranges.append(Range(seed_range.start, seed_range.range))
            return ranges

        seed_ranges = [seed_range]
        for stage in TRANSLATION_PATH:
            seed_ranges = itertools.chain(*(
                mapping(stage, seed_range)
                for seed_range in seed_ranges))
        return min(seed_range.start for seed_range in seed_ranges)

    return min(
        min_location_from_seed_range(Range(seed_start, seed_range_length))
        for seed_start, seed_range_length in seed_pairs
    )


with open('2023/inputs/day05.txt', 'r') as inp:
    sections = inp.read().rsplit('\n\n')
    seeds = (*map(int, sections[0][7:].split(' ')),)
    stdout.write(
        f'Day 5\nFirst part: {first_part(seeds=seeds, maps=sections[1:])}\n')
    stdout.write(
        f'Second part: {second_part(seeds=seeds, maps=sections[1:])}\n')
