from math import lcm
import re


class Location:
    def __init__(self, name, left_location_name: str, right_location_name: str) -> None:
        self.name = name
        self.next_locations = (left_location_name, right_location_name)

    def __repr__(self) -> str:
        return (
            f"Location({self.name}, {self.next_locations[0]}, {self.next_locations[1]})"
        )

    def get_next_location_name(self, instruction: str) -> str:
        loc_index = 0 if instruction == "L" else 1
        return self.next_locations[loc_index]


class InstructionList:
    def __init__(self, instructions: str):
        self.instructions = instructions
        self.index = -1

    def get_next(self) -> str:
        self.index = (self.index + 1) % len(self.instructions)
        return self.instructions[self.index]


class LocationIterator:
    def __init__(
        self, locations: list[Location], start_location_name: str, stop_condition: str
    ) -> None:
        self.locations = locations
        self.cur_loc = self.get_location(start_location_name)
        self.stop_condition = stop_condition

    def get_location(self, location_name: str) -> Location:
        return next(loc for loc in self.locations if loc.name == location_name)

    def iterate(self, instruction: str) -> bool:
        self.cur_loc = self.get_location(
            self.cur_loc.get_next_location_name(instruction)
        )

        return bool(re.search(self.stop_condition, self.cur_loc.name))


if __name__ == "__main__":
    with open("./2023/day08/input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file.readlines()]

    instructions = InstructionList(lines.pop(0))
    locations = [
        Location(*params)
        for params in [tuple(re.findall(r"\w{3}", line)) for line in lines[1:]]
    ]

    # Part 1
    part1_iterators = [LocationIterator(locations, "AAA", "ZZZ")]

    # Part 2
    start_locations = filter(lambda loc: bool(re.search("\w\wA", loc.name)), locations)
    part2_iterators = [
        LocationIterator(locations, loc.name, "\w\wZ") for loc in list(start_locations)
    ]

    # Run 'em!
    for iterators in (part1_iterators, part2_iterators):
        steps_needed = []
        for i, iterator in enumerate(iterators):
            steps = 0
            while True:
                steps += 1
                if iterator.iterate(instructions.get_next()):
                    steps_needed.append(steps)
                    break
        print(lcm(*steps_needed))
