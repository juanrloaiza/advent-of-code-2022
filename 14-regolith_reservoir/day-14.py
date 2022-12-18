from dataclasses import dataclass
from PIL import Image


@dataclass
class Sand:
    x: int = 500
    y: int = 0
    rest: bool = False


class Grid:
    def __init__(self):
        self.current_sand = None
        self.sand_at_rest = 0
        self.part1 = False
        self.part2 = False
        self.frames = []

        with open('input.txt') as file:
            raw_paths = file.readlines()

        self.max_x = 0
        self.max_y = 0
        paths = []
        for path in raw_paths:
            vertices = []
            for path_string in path.split('->'):
                x, y = [int(x) for x in path_string.strip().split(',')]
                vertices.append((x, y))
                if x > self.max_x:
                    self.max_x = x
                if y > self.max_y:
                    self.max_y = y
            paths.append(vertices)

        self.spots = [[None for _ in range(self.max_x + 1)]
                      for _ in range(self.max_y + 2)]

        for path in paths:
            for v1, v2 in zip(path, path[1:]):
                min_x, max_x = min(v1[0], v2[0]), max(v1[0], v2[0])
                min_y, max_y = min(v1[1], v2[1]), max(v1[1], v2[1])

                for y in range(min_y, max_y + 1):
                    for x in range(min_x, max_x + 1):
                        self.spots[y][x] = 'Rock'

    def print(self):
        pixels = []
        for row in self.spots:
            for spot in row:
                if isinstance(spot, Sand):
                    pixels.append((255, 0, 0))
                elif spot == 'Rock':
                    pixels.append((255, 255, 255))
                else:
                    pixels.append((0, 0, 0))

        width = len(self.spots[0])
        height = self.max_y + 15

        img = Image.new('RGB', (width, height))
        img.putdata(pixels)

        img.resize((width * 10, height * 10), Image.Resampling.NEAREST)
        self.frames.append(img)
        img.show()

    def update(self):
        if not self.current_sand:
            self.current_sand = Sand()

        new_y = self.current_sand.y + 1

        if new_y >= len(self.spots):
            self.part1 = True

        diagonal_left = (self.current_sand.x - 1, new_y)
        below = (self.current_sand.x, new_y)
        diagonal_right = (self.current_sand.x + 1, new_y)

        for new_x, new_y in [below, diagonal_left, diagonal_right]:
            if new_x > len(self.spots[0]) - 1:
                for row in self.spots:
                    row.append(None)

            if new_y < len(self.spots) and not self.spots[new_y][new_x]:
                self.spots[self.current_sand.y][self.current_sand.x] = None
                self.spots[new_y][new_x] = self.current_sand

                self.current_sand.x = new_x
                self.current_sand.y = new_y
                return

        self.current_sand.rest = True
        self.sand_at_rest += 1

        if self.current_sand.x == 500 and self.current_sand.y == 0:
            self.part2 = True

        self.current_sand = None


if __name__ == '__main__':

    # Part 1
    grid = Grid()
    while not grid.part1:
        grid.update()
    print(grid.sand_at_rest - 1)

    # Part 2
    grid = Grid()
    while not grid.part2:
        grid.update()
    print(grid.sand_at_rest)
