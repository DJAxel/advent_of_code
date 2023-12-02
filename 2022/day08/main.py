from functools import reduce


class Forest:
    def __init__(self, trees: list[list[int]]) -> None:
        self.trees = trees

    def get_row(self, index) -> list[int]:
        return self.trees[index]

    def get_column(self, index) -> list[int]:
        return [row[index] for row in self.trees]

    def get_trees_left_of_tree(self, x, y) -> list[int]:
        return list(reversed(self.get_row(y)[:x]))

    def get_trees_right_of_tree(self, x, y) -> list[int]:
        return self.get_row(y)[x + 1 :]

    def get_trees_above_tree(self, x, y) -> list[int]:
        return list(reversed(self.get_column(x)[:y]))

    def get_trees_below_tree(self, x, y) -> list[int]:
        return self.get_column(x)[y + 1 :]

    def is_tree_visible(self, x: int, y: int) -> bool:
        if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
            return True

        max_left = max(self.get_trees_left_of_tree(x, y))
        max_right = max(self.get_trees_right_of_tree(x, y))
        max_top = max(self.get_trees_above_tree(x, y))
        max_bottom = max(self.get_trees_below_tree(x, y))

        return min(max_left, max_right, max_top, max_bottom) < self.trees[y][x]

    def _get_viewing_distance(self, tree_height: int, view: list[int]) -> int:
        distance = 0

        for i, tree in enumerate(view):
            distance += 1

            if tree >= tree_height:
                return distance

        return distance

    def get_scenic_score(self, x: int, y: int) -> int:
        tree_height = self.trees[y][x]
        viewing_distances = [
            self._get_viewing_distance(tree_height, self.get_trees_left_of_tree(x, y)),
            self._get_viewing_distance(tree_height, self.get_trees_right_of_tree(x, y)),
            self._get_viewing_distance(tree_height, self.get_trees_above_tree(x, y)),
            self._get_viewing_distance(tree_height, self.get_trees_below_tree(x, y)),
        ]
        return reduce(lambda x, y: x * y, viewing_distances)

    @property
    def width(self) -> int:
        return len(self.trees[0])

    @property
    def height(self) -> int:
        return len(self.trees)


def load_data(path: str) -> Forest:
    trees: Forest = list()
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
            trees.append(tree_list)
    return Forest(trees)


def get_visible_trees_from_outside(forest: Forest) -> int:
    visible = 0

    for y, row in enumerate(forest.trees):
        for x in range(len(row)):
            if forest.is_tree_visible(x, y):
                visible += 1

    return visible


def get_heighest_scenic_score(forest: Forest) -> int:
    top_score = 0
    for y, row in enumerate(forest.trees):
        for x in range(len(row)):
            score = forest.get_scenic_score(x, y)
            top_score = max(top_score, score)

    return top_score


if __name__ == "__main__":
    forest: Forest = load_data("./2022/day08/input.txt")
    print(
        get_visible_trees_from_outside(forest),
        get_heighest_scenic_score(forest),
    )
