import re
import time


def get_pattern_and_groups(line: str) -> tuple[str, tuple[int]]:
    pattern, groups_str = line.split()
    groups = tuple([int(x) for x in groups_str.split(",")])
    return pattern, groups


def is_pattern_matching_groups(pattern: str, groups: tuple[int]) -> bool:
    regex = ["^\.*"]
    for amount in groups:
        if len(regex) > 1:
            regex.append("\.+")
        regex.append("#{" + str(amount) + "}")
    regex.append("\.*$")

    s = "".join(regex)
    r = re.compile(s)

    match = re.search(r, pattern)
    ans = match is not None
    return ans


def get_total_possibilities(string: str, groups: tuple[int]) -> int:
    pattern = re.compile(r"\?")
    match = pattern.search(string)
    if match is None:
        return 1 if is_pattern_matching_groups(string, groups) else 0

    possibilities = 0
    for spring in [".", "#"]:
        pos = match.start()
        new_pattern = string[:pos] + spring + string[pos + 1 :]
        possibilities += get_total_possibilities(new_pattern, groups)
    return possibilities


if __name__ == "__main__":
    with open("./2023/day12/input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file.readlines()]

    start = time.perf_counter()
    total_possibilities = 0
    for line in lines:
        string, groups = get_pattern_and_groups(line)
        possibilities = get_total_possibilities(string, groups)
        total_possibilities += possibilities

    print(total_possibilities)
    print(f"Running time: {time.perf_counter() - start}")
