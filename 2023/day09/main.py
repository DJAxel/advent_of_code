def get_next_value(numbers: list[int]) -> int:
    if numbers[:-1] == numbers[1:]:
        return numbers[0]

    diff_list: list[int] = []
    for i in range(len(numbers) - 1):
        diff_list.append(numbers[i + 1] - numbers[i])

    return numbers[-1] + get_next_value(diff_list)


if __name__ == "__main__":
    with open("./2023/day09/input.txt", "r", encoding="utf8") as file:
        part1, part2 = 0, 0
        for line in file.readlines():
            line = line.strip()
            numbers = [int(n) for n in line.split()]
            part1 += get_next_value(numbers)
            part2 += get_next_value(list(reversed(numbers)))

    print(part1, part2)
