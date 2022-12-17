from itertools import chain
import json


def check_values(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None
        return left < right
    elif isinstance(left, list) and isinstance(right, list):
        for a, b in zip(left, right):
            result = check_values(a, b)
            if result != None:
                return result

        if len(left) == len(right):
            return None
        return len(left) < len(right)

    else:
        left = [left] if isinstance(left, int) else left
        right = [right] if isinstance(right, int) else right
        return check_values(left, right)


def merge_sort(m: list):
    if len(m) <= 1:
        return m

    slicing = int(len(m) / 2)

    left = merge_sort(m[:slicing])
    right = merge_sort(m[slicing:])

    return merge(left, right)


def merge(left, right):
    result = []

    while left and right:
        if check_values(left[0], right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result += left + right

    return result


if __name__ == '__main__':
    with open('input.txt') as file:
        pairs = [[json.loads(l) for l in line.split('\n')]
                 for line in file.read().split('\n\n')]

    part1 = [num + 1 for num, (a, b) in enumerate(pairs) if check_values(a, b)]

    print("Part 1:", sum(part1))

    ordering = merge_sort(list(chain(*pairs, [[[2]], [[6]]])))

    print("Part 2:", (ordering.index([[2]]) + 1) * (ordering.index([[6]]) + 1))
