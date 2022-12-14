from dataclasses import dataclass
from itertools import chain
import string


@dataclass
class Spot:
    height: int
    x: int
    y: int
    distance: int = float('inf')


def get_grid():
    with open('input.txt') as file:
        grid_raw = file.readlines()

    grid = []
    for y, row in enumerate(grid_raw):
        row_heights = []
        for x, height in enumerate(row.strip()):
            new_spot = Spot(
                height=string.ascii_letters.index(height),
                x=x,
                y=y)
            row_heights.append(new_spot)

            if height == 'E':
                target = new_spot
                target.height = string.ascii_lowercase.index('z')
        grid.append(row_heights)

    return grid, target


def get_neighbors(spot, part: int):
    neighbors = []
    if spot.x > 0:
        neighbors.append(grid[spot.y][spot.x - 1])
    if spot.x < len(grid[0]) - 1:
        neighbors.append(grid[spot.y][spot.x + 1])
    if spot.y > 0:
        neighbors.append(grid[spot.y - 1][spot.x])
    if spot.y < len(grid) - 1:
        neighbors.append(grid[spot.y + 1][spot.x])

    if part == 1:
        return [n for n in neighbors if n.height <= (spot.height + 1)]
    else:
        return [n for n in neighbors if n.height >= (spot.height - 1)]


def dijkstra(grid, start: Spot, part: int):
    for node in chain(*grid):
        node.distance = float('inf')

    start.distance = 0

    queue = list(chain(*grid))
    while queue:
        queue = sorted(queue, key=lambda x: x.distance)
        current = queue.pop(0)

        valid_neighbors = get_neighbors(current, part)

        for neighbor in valid_neighbors:
            alternative = current.distance + 1
            if alternative < neighbor.distance:
                neighbor.distance = alternative

        if part == 2:
            candidates = [n for n in valid_neighbors if n.height == 0]
            if candidates:
                return sorted(candidates, key=lambda x: x.distance)[0].distance

    return target.distance


if __name__ == '__main__':
    grid, target = get_grid()
    start = [n for n in chain(*grid) if n.height == 44][0]

    print("Part 1:", dijkstra(grid, start, 1))
    print("Part 2:", dijkstra(grid, target, 2))
