def print_surroundings(lines: list[str], line_start, pos_start, length):
    to_print = "\n"
    for l in range(3):
        for i in range(length):
            try:
                to_print += lines[line_start + l][pos_start + i]
            except IndexError:
                pass

        to_print += "\n"
    print(to_print)


if __name__ == "__main__":
    with open("./2023/day03/test_input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file]

    part_numbers = []

    for line_nr, line in enumerate(lines):
        number_string = ""
        for i, char in enumerate(line + "."):
            if char.isdigit():
                number_string += char
            elif number_string != "":
                print_surroundings(
                    lines,
                    line_nr - 1,
                    i - len(number_string) - 1,
                    len(number_string) + 2,
                )
                positions = [
                    (line_nr - 1, i - x) for x in range(len(number_string) + 2)
                ]
                positions.append((line_nr, i))
                positions.append((line_nr, i - len(number_string) - 1))
                positions += [
                    (line_nr + 1, i - x) for x in range(len(number_string) + 2)
                ]
                for pos in positions:
                    try:
                        ch = lines[pos[0]][pos[1]]
                        if ch not in "0123456789.":
                            part_numbers.append(int(number_string))
                            break
                    except IndexError:
                        pass

                number_string = ""

    print(sum(part_numbers))
