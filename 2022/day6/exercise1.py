def add_char_to_last_four(char, last_chars):
    if len(last_chars) >= 4:
        last_chars.pop(0)
    last_chars.append(char)
    return last_chars


def is_four_different_chars(chars):
    if len(chars) < 4:
        return False
    
    for i in range(len(chars) - 1):
        for j in range( (i + 1), (len(chars)) ):
            if chars[i] == chars[j]:
                return False
    
    return True


last_chars = []
position = 0

with open(r"input.txt", "r") as input:
    while input:
        char = input.read(1)
        position += 1
        last_chars = add_char_to_last_four(char, last_chars)
        if is_four_different_chars(last_chars):
            print(position)
            break
