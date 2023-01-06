pwd: str = ''
library = {
    '/': {}
}


def is_command(line: str) -> bool:
    return line[0] == '$'


def cd(path: str) -> None:
    global pwd
    if path == '/':
        pwd = ''
    elif path.startswith("/"):
        pwd = path
    elif path == "..":
        last_slash_index = pwd.rindex("/")
        pwd = pwd[:last_slash_index]
    else:
        pwd += "/" + path


def execute_command(line: str) -> None:
    command = line[1:].strip()
    if command.startswith("cd"):
        cd(command[2:].strip())


def add_to_library(file_definition: str) -> None:
    global pwd, library
    elements = file_definition.split()
    if(elements[0].isdigit()): #  It's a file
        lib_location = library['/']
        for directory in pwd.split('/'):
            if directory == '':
                continue
            if not directory in lib_location:
                lib_location[directory] = {}
            lib_location = lib_location[directory]
        lib_location[elements[1]] = int(elements[0])
    # else: #  It's a directory
    #     pass


def get_library(path: str) -> dict:
    with open(path, "r") as input:
        while True:
            line = input.readline().strip()
            if len(line) == 0:
                break
            if is_command(line):
                execute_command(line)
            else:
                add_to_library(line)


def calculate_dir_size(directory: dict) -> int:
    size: int = 0
    for key in directory.keys():
        if type(directory[key]) is dict:
            size += calculate_dir_size(directory[key])
        else:
            size += directory[key]
    return size



def get_directories(library: dict) -> list:
    directories = []
    for key in library.keys():
        if type(library[key]) is dict:
            directories.append({"name": key, "size": calculate_dir_size(library[key])})
            directories += get_directories(library[key])
    return directories


def get_total_directory_size_with_maximum(directories: list, max_dir_size: int) -> int:
    total_size = 0
    for directory in directories:
        if directory['size'] <= max_dir_size:
            total_size += directory['size']
    return total_size


def get_directory_with_size_just_above(directories: list, amount: int) -> dict:
    dir = None
    for directory in directories:
        if directory['size'] > amount and (dir is None or directory['size'] < dir['size']):
            dir = directory
    return dir



if __name__ == '__main__':
    get_library("input.txt")
    directories: list = get_directories(library)

    #  Exercise 1
    print(f"Part 1: The total size of all directories < 100000 is {get_total_directory_size_with_maximum(directories, 100000)}")

    #  Exercise 2
    used = next(directory['size'] for directory in directories if directory['name'] == '/')
    space_to_be_freed = 30000000 - (70000000 - used)
    dir_to_remove = get_directory_with_size_just_above(directories, space_to_be_freed)
    print(f"Part 2: Directory {dir_to_remove['name']} with size {dir_to_remove['size']} should be removed")