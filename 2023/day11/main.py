import re


Space = list[list[str]]


def expand_space(grid: Space) -> Space:
    for _ in range(2):
        grid = list(zip(*[line for line in grid]))  # Mirror galaxy on diagonal axis
        space: Space = []
        for row in grid:
            space.append(row)

            if re.match(r"^\.*$", "".join(row)) is not None:
                space.append(row)

        grid = space

    return grid


def get_galaxy_positions(space: Space) -> list[tuple[int, int]]:
    positions = []

    for row, line in enumerate(space):
        for col, char in enumerate(line):
            if char == "#":
                positions.append((row, col))

    return positions


def print_galaxy(galaxy: Space):
    print()
    for line in galaxy:
        print("".join(line))
    print()


if __name__ == "__main__":
    with open("./2023/day11/input.txt", "r", encoding="utf8") as file:
        lines: Space = [list(line.rstrip()) for line in file.readlines()]

    space = expand_space(lines)
    galaxy_positions = get_galaxy_positions(space)

    distance = 0
    for i, position in enumerate(galaxy_positions):
        other_positions = galaxy_positions[i + 1 :]
        for j, other_position in enumerate(other_positions):
            distance += abs(other_position[0] - position[0]) + abs(
                other_position[1] - position[1]
            )

    print(distance)
