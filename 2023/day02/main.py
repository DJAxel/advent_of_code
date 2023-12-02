from typing import List


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


if __name__ == "__main__":
    games = get_games_from_input(r"./2023/day02/input.txt")
    cubes_in_bag = {"red": 12, "green": 13, "blue": 14}
    total = 0

    for game in games:
        b = is_game_possible_with_cubes(game["sets"], cubes_in_bag)
        if b:
            total += game["id"]

    print(total)


# 1. Puzzle input to list of objects
# {
#     id: 1
#     sets: [
#         {
#             "red": 7,
#             "blue": 8,
#         },
#         {
#             "blue": 6,
#             "red": 6,
#             "green": 2
#         },
#     ]
# }
#
# 2. for each game
# 3. for each set, check if the set is possible with the game (12 red, 13 green, 14 blue)
# 4. If so (for all sets in the game), add the game id to the total
