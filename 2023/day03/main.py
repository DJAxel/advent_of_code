def get_number_and_start_index(lines: list[str], pos: tuple[int, int]):
    """
    For a digit at a given position, find the full number that this digit
    belongs to and its starting index.

    Args:
        lines (list[str]): A list of strings, representing the lines in the
        puzzle input.
        pos (tuple[int, int]): The line and character indices of the initial digit.

    Returns:
        _type_: A tuple with the number and the position it starts at.
    """
    rest_of_line = list(reversed("." + lines[pos[0]][: pos[1]]))
    for i, char in enumerate(rest_of_line):
        if not char.isdigit():
            start_index = pos[1] - i
            break

    rest_of_line = list(lines[pos[0]][start_index:] + ".")
    for i, char in enumerate(rest_of_line):
        if not char.isdigit():
            number = lines[pos[0]][start_index : start_index + i]
            return (int(number), (pos[0], start_index))


def get_numbers_around_gear(lines: list[str], pos: tuple[int, int]) -> list[int]:
    """
    Find the unique numbers around a gear (*).

    Args:
        lines (list[str]): A list of strings, representing the lines in the
        puzzle input.
        pos (tuple[int, int]): The position of the gear within the `lines`.

    Returns:
        list[int]: _description_
    """
    numbers: list = []
    positions = (
        [(pos[0] - 1, pos[1] - x + 1) for x in range(3)]
        + [(pos[0] + 1, pos[1] - x + 1) for x in range(3)]
        + [(pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
    )
    for pos in positions:
        if lines[pos[0]][pos[1]].isdigit():
            number = get_number_and_start_index(lines, pos)
            if number[1] not in [number[1] for number in numbers]:
                numbers.append(number)

    return numbers


if __name__ == "__main__":
    with open("./2023/day03/input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file]

    part_numbers = []
    gear_ratios = []

    for line_nr, line in enumerate(lines):
        number_string = ""
        for i, char in enumerate(line + "."):
            if char.isdigit():
                number_string += char
            elif number_string != "":
                positions = (
                    [(line_nr - 1, i - x) for x in range(len(number_string) + 2)]
                    + [(line_nr, i), (line_nr, i - len(number_string) - 1)]
                    + [(line_nr + 1, i - x) for x in range(len(number_string) + 2)]
                )
                for pos in positions:
                    try:
                        ch = lines[pos[0]][pos[1]]
                        if ch not in "0123456789.":
                            part_numbers.append(int(number_string))
                            break
                    except IndexError:
                        pass

                number_string = ""

            if char == "*":
                numbers = get_numbers_around_gear(lines, (line_nr, i))
                if len(numbers) == 2:
                    gear_ratios.append(numbers[0][0] * numbers[1][0])

    print(
        sum(part_numbers),
        sum(gear_ratios),
    )
