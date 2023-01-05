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


def itemIsInAllCollections(item: str, collections: tuple):
    for collection in collections:
        if item not in collection:
            return False
    return True


def getBadgeItem(contents: tuple):
    for item in contents[0]: # loop through items in first elve
        if itemIsInAllCollections(item, contents[1:]):
            return item
                


total = 0
elveGroup = []

with open(r"input.txt", 'r') as input:
    for line in input.readlines():
        elveGroup.append( line.strip() )

        if len(elveGroup) >= 3:
            badge_item = getBadgeItem(tuple(elveGroup))
            total += getPriorityForItem(badge_item)
            elveGroup = []

print(total)