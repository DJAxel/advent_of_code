Forest = list[list[int]]


def load_data(path: str) -> Forest:
    forest: Forest = list()
    with open(path, "r", encoding="utf8") as file:
        while True:
            line: str = file.readline()
            if line == "":
                break
            tree_list: list(int) = []
            for tree in line:
                if tree == "\n":
                    break
                tree_list.append(int(tree))
            forest.append(tree_list)
    return forest


def is_tree_visible(x: int, y: int, forest: Forest) -> bool:
    if x == 0 or x == len(forest[y]) - 1 or y == 0 or y == len(forest) - 1:
        return True

    row = forest[y]
    column = [row[x] for row in forest]
    max_left = max(row[:x])
    max_right = max(row[x + 1 :])
    max_top = max(column[:y])
    max_bottom = max(column[y + 1 :])

    return min(max_left, max_right, max_top, max_bottom) < forest[y][x]


def get_visible_trees_from_outside(forest: Forest) -> int:
    visible = 0

    for y, row in enumerate(forest):
        for x in range(len(row)):
            if is_tree_visible(x, y, forest):
                visible += 1

    return visible


if __name__ == "__main__":
    forest: Forest = load_data("./2022/day08/input.txt")
    print(get_visible_trees_from_outside(forest))
