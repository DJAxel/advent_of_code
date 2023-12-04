def get_nums_list_from_string(string: str) -> list[int]:
    return list(map(lambda n: int(n), string.split()))


def read_card(card: str) -> tuple[list[int], list[int]]:
    card_definition, numbers_str = card.split(":")
    card_nr = int(card_definition.split()[-1])
    nums = numbers_str.split("|")
    return card_nr, map(lambda nums_str: get_nums_list_from_string(nums_str), nums)


def get_points_for_wins(amount_of_wins: int) -> int:
    points = 0

    for i in range(amount_of_wins):
        points = points * 2 if points > 0 else 1

    return points


def get_matches(winning_nums: list[int], own_nums: list[int]) -> int:
    points = 0

    for own_number in own_nums:
        if own_number in winning_nums:
            points += 1

    return points


def make_dict_value_at_least_one_for_key(
    dictionary: dict[int, int], key: int
) -> dict[int, int]:
    if key not in dictionary:
        dictionary[key] = 1

    return dictionary


if __name__ == "__main__":
    total_points = 0
    card_amounts = {}
    with open("./2023/day04/input.txt", "r", encoding="utf8") as data:
        for line in data.readlines():
            card_nr, (winning_nums, own_nums) = read_card(line)
            card_amounts = make_dict_value_at_least_one_for_key(card_amounts, card_nr)
            wins = get_matches(winning_nums, own_nums)

            for i in range(wins):
                i += card_nr + 1
                card_amounts = make_dict_value_at_least_one_for_key(card_amounts, i)
                card_amounts[i] += card_amounts[card_nr]

            total_points += get_points_for_wins(wins)

    print(
        total_points,
        sum(card_amounts.values()),
    )
