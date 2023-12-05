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
    def seed_ranges(self) -> list[int]:
        for i in range(int(len(self.seeds) / 2)):
            start_seed = self.seeds[i * 2]
            range_length = self.seeds[i * 2 + 1]
            for seed in range(start_seed, start_seed + range_length):
                yield seed

    @property
    def maps(self) -> dict[str, list[RangeConverter]]:
        return self._maps

    def _get_nums_list_from_string(self, string: str) -> list[int]:
        return list(map(lambda n: int(n), string.split()))

    def get_location_for_seed(self, seed: int) -> int:
        value = seed
        for range_converters in self.maps.values():
            for range_converter in range_converters:
                converted = range_converter.convert(value)
                if converted != value:
                    value = converted
                    break

        return value


if __name__ == "__main__":
    with open("./2023/day05/test_input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file]
        almanac = Almanac(lines)

        for seed_range in [almanac.seeds, almanac.seed_ranges]:
            lowest_location_number: int | None = None
            for seed in seed_range:
                location = almanac.get_location_for_seed(seed)
                if not lowest_location_number or lowest_location_number > location:
                    lowest_location_number = location
            print(lowest_location_number)
