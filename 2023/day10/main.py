from __future__ import annotations
import re


class Tile:
    def __init__(self, row: int, col: int, symbol: str) -> None:
        self._row = row
        self._col = col
        self._symbol = symbol

    @property
    def connects_up(self) -> bool:
        return self._symbol in ["|", "L", "J"]

    @property
    def connects_down(self) -> bool:
        return self._symbol in ["|", "7", "F"]

    @property
    def connects_left(self) -> bool:
        return self._symbol in ["-", "7", "J"]

    @property
    def connects_right(self) -> bool:
        return self._symbol in ["-", "L", "F"]

    @property
    def symbol(self) -> str:
        return self._symbol

    def connects_to_coords(self, row: int, col: int) -> bool:
        row_diff = row - self._row
        col_diff = col - self._col

        if row_diff == 1 and col_diff == 0:
            return self.connects_down

        if row_diff == -1 and col_diff == 0:
            return self.connects_up

        if col_diff == 1 and row_diff == 0:
            return self.connects_right

        if col_diff == -1 and row_diff == 0:
            return self.connects_left

        return False

    def __eq__(self, other: Tile) -> bool:
        return self._row == other._row and self._col == other._col

    def __repr__(self) -> str:
        return f'Tile({self.row}, {self.col}, "{self._symbol}")'

    @property
    def row(self) -> int:
        return self._row

    @property
    def col(self) -> int:
        return self._col


def find_char(needle: str, grid: list[str]) -> tuple[int, int]:
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == needle:
                return (i, j)

    raise ValueError(f"{needle} is not present in the given grid")


def is_in_loop(col: int, line: str) -> bool:
    return len(re.findall(r"\||F-*J|L-*7", line[col:])) % 2 == 1


def replace_tile_map(map: list[str], tile: Tile) -> list[str]:
    map[tile.row] = (
        map[tile.row][: tile.col] + tile.symbol + map[tile.row][tile.col + 1 :]
    )
    return map


if __name__ == "__main__":
    with open("./2023/day10/input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file.readlines()]

    # 1. Find S ((x, y))
    (start_row, start_col) = find_char("S", lines)

    # 2. Find tiles connected to S
    connected_to_s: list[Tile] = []
    for diff in [1, -1]:
        for compare_row, compare_col in (
            (start_row, start_col + diff),
            (start_row + diff, start_col),
        ):
            compare_tile = Tile(
                compare_row, compare_col, lines[compare_row][compare_col]
            )
            if compare_tile.connects_to_coords(start_row, start_col):
                connected_to_s.append(compare_tile)

    # 3. Find adjacent connecting pipes (should be two) until they have the same coordinate
    start_tile = Tile(
        start_row,
        start_col,
        "L",  # This is hardcoded for my input.txt, might not work on yours
    )
    connected: list[Tile] = connected_to_s
    next_connected: list[Tile] = []
    distance = 1
    visited: list[Tile] = [start_tile]
    loop_map = replace_tile_map(["." * len(s) for s in lines], start_tile)

    while True:
        distance += 1
        for tile in connected:
            for diff in [1, -1]:
                for compare_row, compare_col in (
                    (tile.row, tile.col + diff),
                    (tile.row + diff, tile.col),
                ):
                    if (
                        compare_row > len(lines) - 1
                        or compare_col > len(lines[compare_row]) - 1
                    ):
                        continue

                    compare_tile = Tile(
                        compare_row, compare_col, lines[compare_row][compare_col]
                    )
                    if (
                        tile.connects_to_coords(compare_row, compare_col)
                        and compare_tile not in visited
                    ):
                        next_connected.append(compare_tile)
                        visited.append(tile)
                        loop_map = replace_tile_map(loop_map, tile)

        connected = next_connected
        next_connected = []

        if connected[0] == connected[1]:
            loop_map = replace_tile_map(loop_map, connected[0])
            break

    # Part 2
    tiles_in_loop = 0
    for row, line in enumerate(loop_map):
        for col, _ in enumerate(line):
            symbol = line[col]
            if symbol == ".":
                if is_in_loop(col, loop_map[row]):
                    tiles_in_loop += 1

    print(distance, tiles_in_loop)
