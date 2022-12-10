with open('input.txt') as file:
    instructions = file.readlines()


# Initialize
x = 1
stack = []
screen = [['.' for _ in range(40)] for _ in range(6)]

for num, instruction in enumerate(instructions):
    if instruction.split()[0] == 'noop':
        stack += [0]
    if instruction.split()[0] == 'addx':
        stack += [0, int(instruction.split()[1])]


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
        print(num + 1, x, f"({instruction})")
        signal_strengths.append(x * (num + 1))
    x_cursor = num % 40
    y_cursor = num // 40
    draw_CRT(x, x_cursor, y_cursor)
    x += instruction

print("Part 1:", sum(signal_strengths))
