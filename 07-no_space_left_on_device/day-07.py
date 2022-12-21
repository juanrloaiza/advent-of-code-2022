from dataclasses import dataclass


class Directory():
    def __init__(self, name: str, parent: str = None):
        self.contents = {}
        self.name = name
        self.parent = parent

    def add_subdirectory(self, name: str):
        self.contents[name] = Directory(name, parent=self)
        return self.contents[name]

    def add_file(self, name: str, size: int):
        self.contents[name] = File(name, size)

    def get_size(self) -> int:
        return sum([content.get_size() for content in self.contents.values()])


@dataclass
class File():
    name: str
    size: int

    def get_size(self) -> int:
        return self.size


with open('input.txt') as file:
    commands = file.readlines()

root = Directory('/')
directories = [root]
current_directory = root
for line in commands:
    # Split the line in three parts.
    line_split = line.strip().split(' ')

    # If we are changing directory, set current directory.
    if line_split[1] == 'cd' and line_split[2] != '/':
        if line_split[2] == '..':
            current_directory = current_directory.parent
        else:
            current_directory = current_directory.contents[line_split[2]]

    # Otherwise we are listing or showing files and directories.
    elif line_split[1] not in current_directory.contents:
        if line_split[0] == 'dir':
            d = current_directory.add_subdirectory(line_split[1])
            directories.append(d)
        elif line_split[0].isnumeric():
            current_directory.add_file(line_split[1], size=int(line_split[0]))

# Part 1
less_than_limit = [d.get_size() for d in directories if d.get_size() <= 100000]

print("Part 1:", sum(less_than_limit))

# Part 2

TOTAL_DISK_SPACE = 70000000
free_space = TOTAL_DISK_SPACE - root.get_size()
NEEDED_SPACE = 30000000

candidates = [d for d in directories if free_space + d.get_size()
              >= NEEDED_SPACE]
print("Part 2:", sorted(candidates, key=lambda x: x.get_size())[0].get_size())
