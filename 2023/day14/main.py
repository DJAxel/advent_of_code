def tilt_platorm(platform: list[str]) -> list[str]:
    for col in range(len(platform[0])):
        last_block_row = -1
        for row in range(len(platform)):
            char = platform[row][col]

            if char == ".":
                continue

            if char == "#":
                last_block_row = row

            if char == "O":
                next_block_row = last_block_row + 1
                platform[row] = platform[row][:col] + "." + platform[row][col + 1 :]
                platform[next_block_row] = (
                    platform[next_block_row][:col]
                    + "O"
                    + platform[next_block_row][col + 1 :]
                )
                last_block_row = next_block_row

    return platform


def get_load_on_north_support_beams(platform: list[str]) -> int:
    load = 0
    for i, row in enumerate(platform):
        for char in row:
            if char == "O":
                load += len(platform) - i

    return load


if __name__ == "__main__":
    with open("./2023/day14/input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file.readlines()]

    tilted_platform = tilt_platorm(lines)
    part1 = get_load_on_north_support_beams(tilted_platform)

    print(part1)
