from collections import defaultdict
import re


def parse_crates() -> dict[int, list]:
    crates_dict = defaultdict(list)
    with open('input.txt') as file:
        crates_lines = file.readlines()

    for line in crates_lines[:10]:
        crates = line.replace('     ', ' XXX ').split(' ')

        for num, crate in enumerate(crates):
            if '[' not in crate:
                continue
            crates_dict[num + 1].insert(0, crate.strip())
    return crates_dict


def print_crates(crates_dict: dict):
    for num in sorted(crates_dict):
        print(num, crates_dict[num])

    print('---------------------')


def get_top_of_stacks(crates_dict: dict):
    tops = []

    for num in sorted(crates_dict):
        # If there's a crate on top, add it to the top list.
        if crates_dict[num]:
            tops.append(crates_dict[num][-1])

    print(f"Top of the stacks: {tops}")
    print('Code:', ''.join([re.findall(r'\w', s)[0] for s in tops]))


if __name__ == '__main__':
    stacks = parse_crates()

    with open('input.txt') as file:
        moves = file.readlines()

    for move in moves[10:]:
        this_many_crates, from_stack, to_stack = [
            int(x) for x in re.findall('\d+', move)]

        # Part 1
        # for _ in range(this_many_crates):
        #    crates_dict[to_stack].append(crates_dict[from_stack].pop())

        # Part 2
        stacks[to_stack] += stacks[from_stack][-this_many_crates:]
        stacks[from_stack] = stacks[from_stack][:-this_many_crates]

        # print_crates(crates_dict)

    get_top_of_stacks(stacks)
