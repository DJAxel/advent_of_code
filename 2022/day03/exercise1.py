def getCompartmentContents(contents)-> tuple:
    half_length = int(len(contents)/2)
    return (contents[0:half_length], contents[half_length:])


def getDuplicateItemInCompartments(compartmentContents: tuple)-> str:
    for item in compartmentContents[0]:
        if item in compartmentContents[1]:
            return item


def getPriorityForItem(item: str):
    ascii_value = ord(item)
    if(97 <= ascii_value <= 122):
        return ascii_value - 96
    return ascii_value - 64 + 26


total = 0

with open(r"input.txt", 'r') as input:
    for line in input.readlines():
        compartmentContents: tuple = getCompartmentContents(line)
        duplicate_item: str = getDuplicateItemInCompartments(compartmentContents)
        total += getPriorityForItem(duplicate_item)

print(total)