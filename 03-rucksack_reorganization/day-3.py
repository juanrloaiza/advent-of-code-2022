import string


def find_items_in_common(rucksack: str):
    items_per_compartment = int(len(rucksack) / 2)
    compartment_one = set(rucksack[:items_per_compartment])
    compartment_two = set(rucksack[items_per_compartment:])

    return compartment_one.intersection(compartment_two)


def find_priority(item: str):
    return string.ascii_letters.index(item) + 1


if __name__ == "__main__":

    # Part one

    with open('input.txt') as file:
        rucksacks = file.read().split()

    score = 0
    for rucksack in rucksacks:
        priorities = [find_priority(item)
                      for item in find_items_in_common(rucksack)]
        score += sum(priorities)

    print(f"The sum of priorities is: {score}.")

    # Part two

    groups = [rucksacks[x:x+3] for x in range(0, len(rucksacks), 3)]

    score = 0
    for group in groups:
        rucksack_types = [set(rucksack) for rucksack in group]
        badge = rucksack_types[0].intersection(*rucksack_types[1:])
        score += sum([find_priority(item) for item in badge])

    print(f"The sum of priorities in elves' badges is: {score}.")
