from typing import Dict, List


def get_set_from_str(set_str: str) -> dict:
    set_dict = {}

    for cubes_str in set_str.split(", "):
        space_pos = cubes_str.index(" ")
        amount = int(cubes_str[:space_pos])
        color = cubes_str[space_pos + 1 :]
        set_dict[color] = amount

    return set_dict


def get_game_from_line(line: str) -> dict:
    colon_pos = line.index(":")
    game_id = int(line[5:colon_pos])
    game = {"id": game_id, "sets": []}

    sets_string = line[colon_pos + 2 :]
    for set_str in sets_string.split("; "):
        game["sets"].append(get_set_from_str(set_str))

    return game


def get_games_from_input(path: str) -> List[dict]:
    games = []

    with open(path, "r", encoding="utf8") as data:
        for line in data.readlines():
            line = line.strip()
            games.append(get_game_from_line(line))

    return games


def is_game_possible_with_cubes(sets: List[dict], cubes_in_bag: dict) -> bool:
    for set in sets:
        for color, amount in set.items():
            if not color in cubes_in_bag or cubes_in_bag[color] < amount:
                return False

    return True


def get_max_cube_amounts(sets: List[Dict[str, int]]) -> Dict[str, int]:
    max_cube_amounts = {}
    for set in sets:
        for color, amount in set.items():
            if color not in max_cube_amounts or max_cube_amounts[color] < amount:
                max_cube_amounts[color] = amount

    return max_cube_amounts


def part1(games: List[dict], cubes_in_bag: Dict[str, int]) -> int:
    total = 0

    for game in games:
        b = is_game_possible_with_cubes(game["sets"], cubes_in_bag)
        if b:
            total += game["id"]

    return total


def part2(games: List[Dict[str, int]]) -> int:
    total = 0

    for game in games:
        amounts = get_max_cube_amounts(game["sets"])
        power = 1
        for amount in amounts.values():
            power *= amount

        total += power

    return total


if __name__ == "__main__":
    games = get_games_from_input(r"./2023/day02/input.txt")
    answer1 = part1(games, {"red": 12, "green": 13, "blue": 14})
    answer2 = part2(games)

    print(answer1)
    print(answer2)
