from collections import defaultdict
from functools import reduce
from typing import Dict, List


def get_collection_from_str(collection_str: str) -> dict:
    collection_dict = {}

    for cubes_str in collection_str.split(", "):
        amount, color = cubes_str.split()
        amount = int(amount)
        collection_dict[color] = amount

    return collection_dict


def get_game_from_line(line: str) -> dict:
    id_, line = line.split(":")
    game_id = int(id_.split()[-1])
    game = {"id": game_id, "collections": []}

    for collection_str in line.split("; "):
        game["collections"].append(get_collection_from_str(collection_str))

    return game


def get_games_from_input(path: str) -> List[dict]:
    games = []

    with open(path, "r", encoding="utf8") as data:
        for line in data.readlines():
            games.append(get_game_from_line(line))

    return games


def is_game_possible_with_cubes(collections: List[dict], cubes_in_bag: dict) -> bool:
    for collection in collections:
        for color, amount in collection.items():
            if not color in cubes_in_bag or cubes_in_bag[color] < amount:
                return False

    return True


def get_max_cube_amounts(collections: List[Dict[str, int]]) -> Dict[str, int]:
    max_cube_amounts = defaultdict(int)
    for collection in collections:
        for color, amount in collection.items():
            max_cube_amounts[color] = max(max_cube_amounts[color], amount)

    return max_cube_amounts


def part1(games: List[dict], cubes_in_bag: Dict[str, int]) -> int:
    total = 0

    for game in games:
        if is_game_possible_with_cubes(game["collections"], cubes_in_bag):
            total += game["id"]

    return total


def part2(games: List[Dict[str, int]]) -> int:
    total = 0

    for game in games:
        amounts = get_max_cube_amounts(game["collections"])
        total += reduce(lambda x, y: x * y, amounts.values())

    return total


if __name__ == "__main__":
    games = get_games_from_input(r"./2023/day02/input.txt")

    answer1 = part1(games, {"red": 12, "green": 13, "blue": 14})
    answer2 = part2(games)

    print(answer1, answer2)
