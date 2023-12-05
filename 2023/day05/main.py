import time


class RangeConverter:
    source_range_start: int
    source_range_end: int
    offset: int

    def __init__(self, destination: int, source: int, range_length: int):
        self.source_range_start = source
        self.source_range_end = source + range_length - 1
        self.offset = destination - source

    def convert(self, value: int) -> int:
        if self.source_range_start <= value <= self.source_range_end:
            return value + self.offset

        return value

    def convert_range(self, range: tuple[int, int]) -> tuple[int, int]:
        return (range[0] + self.offset, range[1] + self.offset)

    def to_range(self) -> tuple[int, int]:
        return (self.source_range_start, self.source_range_end)


class Almanac:
    _seeds: list[int] = []
    _maps: dict[str, list[RangeConverter]] = {}

    def __init__(self, lines: list[str]):
        self._seeds = self._get_nums_list_from_string(lines[0].split(":")[1])

        map_name: str
        for line in lines[2:]:
            if line == "":
                continue

            if line.find("map") >= 0:
                map_name = line.split()[0]
                continue

            parameters = self._get_nums_list_from_string(line)
            range_converter = RangeConverter(*parameters)
            if map_name not in self._maps:
                self._maps[map_name] = []
            self._maps[map_name].append(range_converter)

    @property
    def seeds(self) -> list[int]:
        return self._seeds

    @property
    def seed_ranges(self) -> list[tuple[int, int]]:
        seed_ranges: list[tuple[int, int]] = []

        for i in range(int(len(self.seeds) / 2)):
            start_seed = self.seeds[i * 2]
            range_length = self.seeds[i * 2 + 1]
            seed_ranges.append((start_seed, start_seed + range_length - 1))

        return seed_ranges

    @property
    def maps(self) -> dict[str, list[RangeConverter]]:
        return self._maps

    def _get_nums_list_from_string(self, string: str) -> list[int]:
        return list(map(lambda n: int(n), string.split()))

    def merge_overlapping_ranges(self, ranges: list[tuple[int, int]]):
        ranges = ranges.copy()
        for i, r1 in enumerate(ranges):
            if r1 is None:
                continue
            for j, r2 in enumerate(ranges):
                if i == j or r2 is None:
                    continue

                overlap = self.get_range_overlap(r1, r2)

                if overlap == None and r1[1] != r2[0] - 1 and r2[1] != r1[0] - 1:
                    continue

                ranges[i] = (min(r1[0], r2[0]), max(r1[1], r2[1]))
                ranges[j] = None

        return list(filter(lambda r: r is not None, ranges))

    @staticmethod
    def get_range_overlap(
        range1: tuple[int, int], range2: tuple[int, int]
    ) -> tuple[int, int] | None:
        overlap = (
            max(range1[0], range2[0]),
            min(range1[1], range2[1]),
        )

        if overlap[0] <= overlap[1]:
            return overlap

        return None

    def convert_ranges_with_converter(
        self, ranges: list[tuple[int, int]], converter: RangeConverter
    ) -> list[tuple[int, int]]:
        unchanged_ranges: list[tuple[int, int]] = []
        new_ranges: list[tuple[int, int]] = []
        for r in ranges:
            overlap = Almanac.get_range_overlap(r, (converter.to_range()))

            if overlap is None:
                unchanged_ranges.append(r)
                continue

            if r[0] < overlap[0]:
                unchanged_ranges.append((r[0], overlap[0] - 1))

            new_ranges.append(converter.convert_range(overlap))

            if r[1] > overlap[1]:
                unchanged_ranges.append((overlap[1] + 1, r[1]))

        return (
            unchanged_ranges,
            new_ranges,
        )

    def convert_range_with_converters(
        self, r: tuple[int, int], converters: list[RangeConverter]
    ):
        unchanged_ranges: list[tuple[int, int]] = [r]
        new_ranges: list[tuple[int, int]] = []

        for converter in converters:
            outcome = self.convert_ranges_with_converter(unchanged_ranges, converter)
            unchanged_ranges = outcome[0]
            if len(outcome[1]):
                new_ranges += outcome[1]

        merged = unchanged_ranges + new_ranges
        return merged

    def convert_ranges_with_map(
        self, ranges: list[tuple[int, int]], map_rules: list[RangeConverter]
    ):
        new_ranges = []
        for r in ranges:
            ranges_to_add = self.convert_range_with_converters(r, map_rules)
            new_ranges += ranges_to_add

        return self.merge_overlapping_ranges(new_ranges)


if __name__ == "__main__":
    with open("./2023/day05/input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file]
        almanac = Almanac(lines)

        part1_ranges = [(s, s) for s in almanac.seeds]
        part2_ranges = almanac.seed_ranges

        for ranges in [part1_ranges, part2_ranges]:
            start = time.perf_counter()
            lowest_location_number: int | None = None
            for map_name, map_rules in almanac.maps.items():
                ranges = almanac.convert_ranges_with_map(ranges, map_rules)

            for r in ranges:
                if not lowest_location_number or r[0] < lowest_location_number:
                    lowest_location_number = r[0]

            print(lowest_location_number)
            print(f"Running time: {time.perf_counter() - start}")
