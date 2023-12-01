from typing import List, Optional

number_strings = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def get_int_from_number_string(string: str) -> Optional[int]:
    for value, number_string in number_strings.items():
        if string.startswith(number_string):
            return value

    return None


def get_digits_from_string(string: str, include_word_digits: bool):
    numbers: List[int] = []
    for i, char in enumerate(string):
        if char.isdigit():
            numbers.append(int(char))
            continue

        if not include_word_digits:
            continue

        number = get_int_from_number_string(string[i:])
        if number:
            numbers.append(number)

    return numbers


def get_config_value(string: str, include_word_digits: bool):
    numbers = get_digits_from_string(string, include_word_digits)

    if len(numbers) < 1:
        raise ValueError

    return int(f"{numbers[0]}{numbers[-1]}")


if __name__ == "__main__":
    with open(r"./2023/day01/input.txt", "r", encoding="utf8") as data:
        total1 = 0
        total2 = 0

        for line in data.readlines():
            line = line.strip()
            try:
                total1 += get_config_value(line, include_word_digits=False)
                total2 += get_config_value(line, include_word_digits=True)
            except ValueError:
                pass

    print(total1, total2)
