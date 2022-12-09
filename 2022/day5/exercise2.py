ex_stacks = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]

def get_stacks():
    stacks = []
    with open(r"input.txt", "r") as input:
        stack_index = 0
        while True:
            crate = input.read(4)
            if '1' in crate:
                break

            if len(stacks) < stack_index + 1:
                stacks.append([])
            if crate[1] != ' ':
                stacks[stack_index].insert(0, crate[1])

            if '\n' in crate:
                stack_index = 0
            else:
                stack_index += 1
    return stacks


def get_moves():
    moves = []
    with open(r"input.txt", "r") as input:
        while input:
            line = input.readline()
            if line == "":
                break
            if not line.startswith('move'):
                continue
            
            words = line.split()
            moves.append((int(words[1]), int(words[3]), int(words[5])))
    return moves


def execute_moves_on_stacks(moves, stacks):
    for move in moves:
        # visualize_stacks(stacks)
        (repeats, source, destination) = move
        crates = []
        for _ in range(repeats):
            crates.insert(0, stacks[source-1].pop())
        stacks[destination-1] += crates
    return stacks


def get_top_crates_from_stacks(stacks):
    top_crates = []
    for stack in stacks:
        top_crates.append( stack[len(stack)-1] )
    return top_crates

def visualize_stacks(stacks):
    """ For debug purposes """
    max_length = 0;
    for stack in stacks:
        max_length = max(max_length, len(stack))
    
    output = ""
    for i in reversed(range(max_length)):
        for stack in stacks:
            if(len(stack) < i + 1):
                output += "    "
            else:
                output += "[" + stack[i] + "] "
        output += '\n'
    
    for i in range(len(stacks)):
        output += " " + str(i+1) + "  "
    output += '\n'
    print(output)

stacks = get_stacks()
moves = get_moves()
stacks = execute_moves_on_stacks(moves, stacks)
# visualize_stacks(stacks)
top_crates = get_top_crates_from_stacks(stacks)
print( "".join(top_crates) )