def find_visible_trees(trees: list):
    visible_trees = []
    last_visible_tree = -1
    for num, tree in enumerate(trees):
        if tree > last_visible_tree:
            last_visible_tree = tree
            visible_trees.append(num)
    return visible_trees


with open('input.txt') as file:
    grid = [[int(l) for l in line] for line in file.read().split()]

visible = []
for y, row in enumerate(grid):
    # From left
    visible += [(y, x) for x in find_visible_trees(row)]

    # From right
    visible += [(y, len(row) - x - 1)
                for x in find_visible_trees(row[::-1])]


for x, col in enumerate(row):
    tree_line = [grid[y][x] for y, _ in enumerate(grid)]

    # From top
    visible += [(y, x) for y in find_visible_trees(tree_line)]

    # From bottom
    visible += [(len(tree_line) - y - 1, x)
                for y in find_visible_trees(tree_line[::-1])]

print("Visible trees:", len(set(visible)))

# Part 2

best_score = 0
for y, row in enumerate(grid):
    for x, tree in enumerate(row):
        # Look left
        left = 0
        for i in range(x - 1, -1, -1):
            left += 1
            if grid[y][i] >= tree:
                break

        # Look right
        right = 0
        for i in range(x + 1, len(row)):
            right += 1
            if grid[y][i] >= tree:
                break

        # Look top
        top = 0
        for i in range(y - 1, -1, - 1):
            top += 1
            if grid[i][x] >= tree:
                break

        # Look bottom
        bottom = 0
        for i in range(y + 1, len(grid)):
            bottom += 1
            if grid[i][x] >= tree:
                break

        score = left * right * top * bottom
        if score > best_score:
            best_score = score

print("Best score possible:", best_score)
