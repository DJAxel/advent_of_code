import re


class Location:
    def __init__(self, name, left_location_name: str, right_location_name: str) -> None:
        self.name = name
        self.next_locations = (left_location_name, right_location_name)

    def __repr__(self) -> str:
        return f"Location({self.name}, {self.left_location_name}, {self.right_location_name})"

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
        # self.steps = 0

    def get_location(self, location_name: str) -> Location:
        return next(loc for loc in self.locations if loc.name == location_name)

    def iterate(self, instruction: str) -> bool:
        self.cur_loc = self.get_location(
            self.cur_loc.get_next_location_name(instruction)
        )
        # self.steps += 1

        return bool(re.search(self.stop_condition, self.cur_loc.name))


if __name__ == "__main__":
    with open("./2023/day08/input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file.readlines()]

    instructions = InstructionList(lines.pop(0))
    locations = [
        Location(*params)
        for params in [tuple(re.findall(r"\w{3}", line)) for line in lines[1:]]
    ]

    locationIterator = LocationIterator(locations, "AAA", "ZZZ")

    part1 = 1
    while not locationIterator.iterate(instructions.get_next()):
        part1 += 1

    print(part1)
