with open('input.txt') as file:
    moves = file.readlines()

DIRECTIONS = {
    "R": 1,
    "L": -1,
    "U": 1,
    "D": -1
}


def simulation(n_knots: int):
    knots = [[0, 0] for x in range(n_knots)]

    main_head = knots[0]  # y, x
    main_tail = knots[-1]  # y, x

    visited = []
    for move in moves:
        move = move.split()
        for _ in range(int(move[1])):

            if move[0] in ["L", "R"]:
                main_head[1] += DIRECTIONS[move[0]]
            else:
                main_head[0] += DIRECTIONS[move[0]]

            for head, tail in zip(knots, knots[1:]):

                # Move the tail
                distance_x = head[1] - tail[1]
                distance_y = head[0] - tail[0]

                if abs(distance_x) + abs(distance_y) >= 3:
                    tail[0] += int(distance_y / abs(distance_y))
                    tail[1] += int(distance_x / abs(distance_x))

                elif abs(distance_y) == 2:
                    tail[0] += int(distance_y / abs(distance_y))

                elif abs(distance_x) == 2:
                    tail[1] += int(distance_x / abs(distance_x))

            if (main_tail[1], main_tail[0]) not in visited:
                visited.append((main_tail[1], main_tail[0]))

    return len(set(visited))


print(f"Part 1: The tail visited {simulation(2)} spots.")
print(f"Part 2: The tail visited {simulation(10)} spots.")
