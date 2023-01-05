import re


def is_one_range_contained_in_other(range1: tuple, range2: tuple):
    return (range1[0] >= range2[0] and range1[1] <= range2[1]) or \
           (range2[0] >= range1[0] and range2[1] <= range1[1])


def range_string_to_tuples(input: str):
    integers = re.split(r"[\-,]+", input)
    return ((int(integers[0]), int(integers[1])), (int(integers[2]), int(integers[3])))


total = 0

with open(r"input.txt", "r") as input:
    for line in input.readlines():
        (range1, range2) = range_string_to_tuples( line.strip() )
        if is_one_range_contained_in_other(range1, range2):
            total += 1

print( total )