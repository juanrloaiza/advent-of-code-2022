with open('input.txt') as file:
    instructions = file.readlines()

x = 1
queue = []
screen = [['⬛' for _ in range(40)] for _ in range(6)]

for cycle, instruction in enumerate(instructions):
    queue += [0]
    if instruction.split()[0] == 'addx':
        queue += [int(instruction.split()[1])]


def draw_CRT():
    for row in screen:
        print(''.join(row))
    print('-' * 40)


def get_character(x: int, cycle: int):
    return '⬜' if x <= cycle % 40 + 1 and x >= cycle % 40 - 1 else '⬛'


signal_strengths = []
for cycle, instruction in enumerate(queue):
    if cycle + 1 in [20, 60, 100, 140, 180, 220]:
        signal_strengths.append(x * (cycle + 1))

    screen[cycle // 40][cycle % 40] = get_character(x, cycle)
    draw_CRT()
    x += instruction

print("Part 1:", sum(signal_strengths))
