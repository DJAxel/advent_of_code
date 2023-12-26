from typing import Optional


ORIENTATION_MULTIPLIERS = (100, 1)


def are_lines_almost_equal(line1: str, line2: str) -> bool:
    char_diffs = 0

    for i, char in enumerate(line1):
        if char != line2[i]:
            if char_diffs > 1:
                return False
            char_diffs += 1

    return char_diffs == 1


def is_mirrored_after_row(pattern: list[str], row_index: int) -> bool:
    rows_to_check = min(row_index, len(pattern) - row_index)

    for i in range(rows_to_check):
        if pattern[row_index + i] != pattern[row_index - 1 - i]:
            return False

    return True


def get_pattern_and_mirrored(pattern: list[str]) -> tuple[list[str]]:
    mirrored_pattern = [
        "".join(line) for line in list(zip(*[line for line in pattern]))
    ]
    return (pattern, mirrored_pattern)


def get_score_for_pattern(pattern: list[str], has_smudge=False) -> int:
    patterns = get_pattern_and_mirrored(pattern)
    for pattern, orientation_multiplier in zip(patterns, ORIENTATION_MULTIPLIERS):
        for i, line in enumerate(pattern[:-1]):
            if (
                not has_smudge
                and pattern[i + 1] == line
                and is_mirrored_after_row(pattern, i + 1)
            ):
                return (i + 1) * orientation_multiplier

            elif has_smudge:
                for j in range(i + 1, len(pattern), 2):
                    if are_lines_almost_equal(line, pattern[j]):
                        check_after_line = int(i + (j - i + 1) / 2)
                        new_pattern = pattern.copy()
                        new_pattern[j] = new_pattern[i]
                        if is_mirrored_after_row(new_pattern, check_after_line):
                            return check_after_line * orientation_multiplier


if __name__ == "__main__":
    with open("./2023/day13/input.txt", "r", encoding="utf8") as file:
        lines = [line.rstrip() for line in file.readlines()]

    scores: list[int, int] = [0, 0]
    pattern: list[str] = []

    for i, line in enumerate(lines):
        if line == "" or i == len(lines) - 1:
            for i, has_smudge in enumerate((False, True)):
                new_score = get_score_for_pattern(pattern, has_smudge)
                scores[i] += new_score
            pattern = []
            continue

        pattern.append(line)

    print(*scores)
