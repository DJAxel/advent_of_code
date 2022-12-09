score = 0

def getChoiceScore(choice):
    if choice == 'X':
        return 1
    if choice == 'Y':
        return 2
    if choice == 'Z':
        return 3


def getOutcomeScore(outcome):
    if outcome == 'X':
        return 0
    if outcome == 'Y':
        return 3
    if outcome == 'Z':
        return 6


def getUserChoice(opponentChoice, gameOutcome):
    if ((opponentChoice == 'A' and gameOutcome == 'Y') or
        (opponentChoice == 'B' and gameOutcome == 'X') or
        (opponentChoice == 'C' and gameOutcome == 'Z')):
        return 'X'
    if ((opponentChoice == 'A' and gameOutcome == 'Z') or
        (opponentChoice == 'B' and gameOutcome == 'Y') or
        (opponentChoice == 'C' and gameOutcome == 'X')):
        return 'Y'
    return 'Z'
    


with open(r"input.txt", "r") as input:
    for line in input.readlines():
        line = line.strip()
        
        #  get user choice
        choice = getUserChoice(line[0], line[2]) 
        #  calc choice score and add to total
        score += getChoiceScore(choice)
        #  calc game outcome score
        score += getOutcomeScore(line[2])

print(score)