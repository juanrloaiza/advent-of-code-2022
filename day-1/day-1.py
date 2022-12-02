# Part 1

with open('input.txt') as file:
    elves = file.read().split('\n\n')

elves = [elf.split('\n') for elf in elves]
calories = [sum([int(meal) for meal in elf if meal]) for elf in elves]

print(f"The elf carrying the most calories is: {max(calories)}")

# Part 2

top_3 = sorted(calories, reverse=True)[:3]

print(f"The top 3 elves are carrying {sum(top_3)} calories.")
