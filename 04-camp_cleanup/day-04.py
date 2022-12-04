with open('input.txt') as file:
    ranges = file.read().split('\n')

assignments = [assignment.split(',') for assignment in ranges]

full_overlap = 0
partial_overlap = 0
for assignment in assignments:
    assignment_list = [range.split('-') for range in assignment]
    assignment_list = [set(range(int(assignment[0]), int(
        assignment[1]) + 1)) for assignment in assignment_list]

    # Part 1
    if assignment_list[0] <= assignment_list[1] or assignment_list[0] >= assignment_list[1]:
        full_overlap += 1

    # Part 2
    if assignment_list[0] & assignment_list[1]:
        partial_overlap += 1

print(f"Fully overlapping sets: {full_overlap}")
print(f"Partially overlapping sets: {partial_overlap}")
