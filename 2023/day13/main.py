def is_mirrored_after_row(pattern: list[str], row_index: int) -> bool:
    rows_to_check = min(row_index, len(pattern) - row_index)

    for i in range(rows_to_check):
        if pattern[row_index + i] != pattern[row_index - 1 - i]:
            return False

    return True


def get_score_for_pattern(pattern: list[str]) -> int:
    for orientation_multiplier in [1, 100]:
        pattern = list(
            zip(*[line for line in pattern])
        )  # Mirror pattern on diagonal axis

        for i, line in enumerate(pattern):
            if i == 0:
                continue

            if pattern[i - 1] == line:
                if is_mirrored_after_row(pattern, i):
                    return i * orientation_multiplier


if __name__ == "__main__":
    with open("./2023/day13/input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file.readlines()]

    score = 0
    pattern: list[str] = []

    for i, line in enumerate(lines):
        if line == "" or i == len(lines) - 1:
            score += get_score_for_pattern(pattern)
            pattern = []
            continue

        pattern.append(line)

    print(score)
