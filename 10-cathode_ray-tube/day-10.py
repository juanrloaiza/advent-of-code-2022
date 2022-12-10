with open('input.txt') as file:
    instructions = file.readlines()

x = 1
stack = []
screen = [['.' for _ in range(40)] for _ in range(6)]

for num, instruction in enumerate(instructions):
    stack += [0]
    if instruction.split()[0] == 'addx':
        stack += [int(instruction.split()[1])]


def draw_CRT(x: int, x_cursor: int, y_cursor: int):
    c = '.'
    if x <= x_cursor + 1 and x >= x_cursor - 1:
        c = '#'
    screen[y_cursor][x_cursor] = c
    for row in screen:
        print(''.join(row))
    print('-' * 40)


signal_strengths = []
for num, instruction in enumerate(stack):
    if num + 1 in [20, 60, 100, 140, 180, 220]:
        signal_strengths.append(x * (num + 1))
    draw_CRT(x, num % 40, num // 40)
    x += instruction

print("Part 1:", sum(signal_strengths))
