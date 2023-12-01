from typing import List


def get_digits_from_string(string: str):
    numbers: List[int] = []
    for char in string:
        if char.isdigit():
            numbers.append(int(char))
    return numbers


def get_config_value(string: str):
    numbers = get_digits_from_string(string)

    if len(numbers) < 1:
        raise ValueError

    return int(f"{numbers[0]}{numbers[-1]}")


if __name__ == "__main__":
    with open(r"./2023/day01/input.txt", "r", encoding="utf8") as data:
        total = 0

        for line in data.readlines():
            line = line.strip()
            try:
                total += get_config_value(line)
            except ValueError:
                pass

    print(total)
