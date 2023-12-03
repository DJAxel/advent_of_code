if __name__ == "__main__":
    with open("./2023/day03/input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file]

    part_numbers = []

    for line_nr, line in enumerate(lines):
        number_string = ""
        for i, char in enumerate(line + "."):
            if char.isdigit():
                number_string += char
            elif number_string != "":
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
