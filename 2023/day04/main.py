def get_numbers_from_card(card: str) -> tuple[list[int], list[int]]:
    values_str = card.split(":")[1]
    win_nums_str, own_nums_str = values_str.split("|")
    win_nums, own_nums = lambda nums_str: list(map(lambda n: int(n), nums_str.split()))
    win_nums = list(map(lambda n: int(n), win_nums_str.split()))
    own_nums = list(map(lambda n: int(n), own_nums_str.split()))
    return win_nums, own_nums


def get_points_from_card_nums(winning_nums: list[int], own_nums: list[int]) -> int:
    points = 0
    for own_number in own_nums:
        if own_number in winning_nums:
            points = points * 2 if points > 0 else 1

    return points


if __name__ == "__main__":
    total_points = 0
    with open("./2023/day04/input.txt", "r", encoding="utf8") as data:
        for line in data.readlines():
            winning_nums, own_nums = get_numbers_from_card(line)
            total_points += get_points_from_card_nums(winning_nums, own_nums)

    print(total_points)
