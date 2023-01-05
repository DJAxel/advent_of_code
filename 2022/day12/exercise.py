def load_data(path):
    map = []
    start_pos = ()
    end_pos = ()
    with open(path, "r") as input:
        for line in input.readlines():
            mapLine = []
            for character in line:
                if character == '\n':
                    continue
                if character == 'S':
                    start_pos = (len(map), len(mapLine))
                if character == 'E':
                    end_pos = (len(map), len(mapLine))
                
                mapLine.append(character)
            map.append(mapLine)
    return map, start_pos, end_pos


def get_map(width: int, height: int, default_value):
    map = []
    for _ in range(height):
        mapLine = []
        for _ in range(width):
            mapLine.append(default_value)
        map.append(mapLine)
    return map


def get_next_node_to_process(value_map, processed_map):
    distinct_values = []
    for row in value_map:
        for value in row:
            if value == None:
                continue
            if value not in distinct_values:
                distinct_values.append(value)
    distinct_values.sort()

    for value in distinct_values:
        for y in range(len(value_map)):
            for x in range(len(value_map[y])):
                if value_map[y][x] == value and not processed_map[y][x]:
                    return y, x
    
    raise IndexError('There are no possible nodes to process next')


def get_adjacent_unprocessed_nodes(y, x, processed_map):
    nodes = []
    if x+1 < len(value_map[y]) and not processed_map[y][x+1]:
        nodes.append((y, x+1))
    if y+1 < len(value_map) and not processed_map[y+1][x]:
        nodes.append((y+1, x))
    if y-1 >= 0 and not processed_map[y-1][x]:
        nodes.append((y-1, x))
    if x-1 >= 0 and not processed_map[y][x-1]:
        nodes.append((y, x-1))
    return nodes


def get_level(character: str):
    if character == 'S':
        return 1
    if character == 'E':
        return 26
    return ord(character) - 96


def letter_can_be_reached_from(source_character: str, destination_character: str):
    return get_level(source_character) + 1 >= get_level(destination_character)


def update_adjacent_nodes(y, x, processed_map, data_map, value_map):
    adjacent_nodes = get_adjacent_unprocessed_nodes(y, x, processed_map)
    for node in adjacent_nodes:
        if not letter_can_be_reached_from(data_map[node[0]][node[1]], data_map[y][x]):
            continue
        if not value_map[node[0]][node[1]] == None and value_map[y][x] + 1 >= value_map[node[0]][node[1]]:
            continue
        value_map[node[0]][node[1]] = value_map[y][x] + 1
    return value_map


def get_a_node_coordinates(data_map):
    coordinates = []
    for y in range(len(data_map)):
        for x in range(len(data_map[y])):
            if get_level(data_map[y][x]) == 1:
                coordinates.append((y, x))
    return coordinates


def get_min_steps_from_any_a(data_map, value_map):
    a_nodes = get_a_node_coordinates(data_map)
    lowest_value: int = None
    lowest_value_coordinates = ()
    for (y, x) in a_nodes:
        value = value_map[y][x]
        if value is None:
            continue
        if lowest_value is None or lowest_value > value:
            lowest_value = value
            lowest_value_coordinates = (y, x)
    return lowest_value, lowest_value_coordinates


data_map, start_pos, end_pos = load_data(r'input.txt')
parent_map = get_map(len(data_map[0]), len(data_map), None)
processed_map = get_map(len(data_map[0]), len(data_map), False)
value_map = get_map(len(data_map[0]), len(data_map), None)
value_map[end_pos[0]][end_pos[1]] = 0

for _ in range(len(data_map) * len(data_map[0])):
    try:
        (y, x) = get_next_node_to_process(value_map, processed_map)
    except IndexError:
        break

    processed_map[y][x] = True
    value_map = update_adjacent_nodes(y, x, processed_map, data_map, value_map)

print(f'Ex. 1: Shortest path from S to E is {value_map[start_pos[0]][start_pos[1]]} steps')
(min_steps_from_any_a, coordinates) = get_min_steps_from_any_a(data_map, value_map)
print(f'Ex. 2: Shortest path from any a to E is {min_steps_from_any_a} steps (start at position (x, y) = ({coordinates[1]}, {coordinates[0]}))')
