score = 0

def getChoiceScore(input):
    choice = input[2]
    if choice == 'X':
        return 1
    if choice == 'Y':
        return 2
    if choice == 'Z':
        return 3


def getOutcomeScore(input):
    if((input[0] == 'A' and input[2] == 'X')
        or (input[0] == 'B' and input[2] == 'Y')
        or (input[0] == 'C' and input[2] == 'Z')):
        return 3
    if((input[0] == 'C' and input[2] == 'X')
        or (input[0] == 'A' and input[2] == 'Y')
        or (input[0] == 'B' and input[2] == 'Z')):
        return 6
    return 0


with open(r"input.txt", "r") as input:
    for line in input.readlines():
        line = line.strip()
        
        # calc choice score and add to total
        score += getChoiceScore(line)
        # calc game outcome score
        score += getOutcomeScore(line)

print(score)