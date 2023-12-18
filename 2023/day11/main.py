import re


def get_empty_rows_and_columns(grid: list[list[str]]) -> list[list[str]]:
    empty_rows_cols = [[], []]
    for i in [1, 0]:
        grid = list(zip(*[line for line in grid]))  # Mirror galaxy on diagonal axis
        for j, row in enumerate(grid):
            if re.match(r"^\.*$", "".join(row)) is not None:
                empty_rows_cols[i].append(j)

    return empty_rows_cols


def get_galaxy_positions(space: list[list[str]]) -> list[tuple[int, int]]:
    positions = []

    for row, line in enumerate(space):
        for col, char in enumerate(line):
            if char == "#":
                positions.append((row, col))

    return positions


if __name__ == "__main__":
    with open("./2023/day11/input.txt", "r", encoding="utf8") as file:
        lines: list[list[str]] = [list(line.rstrip()) for line in file.readlines()]

    empty_rows, empty_columns = get_empty_rows_and_columns(lines)
    galaxy_positions = get_galaxy_positions(lines)

    for expand_multiplier in [2, 1000000]:
        distance = 0
        for i, position in enumerate(galaxy_positions):
            other_positions = galaxy_positions[i + 1 :]
            for j, other_position in enumerate(other_positions):
                for index, empty_list in [(0, empty_rows), (1, empty_columns)]:
                    for _, empty_coord in enumerate(empty_list):
                        A = min(position[index], other_position[index])
                        B = max(position[index], other_position[index])
                        if A < empty_coord < B:
                            distance += expand_multiplier - 1

                distance += abs(other_position[0] - position[0]) + abs(
                    other_position[1] - position[1]
                )

        print(distance)
