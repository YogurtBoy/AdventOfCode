# f = open('2022/day4/assignments_small.txt', 'r')
f = open('2022/day4/assignments.txt', 'r')

if f:
    print("Successfully opened data...")

def give_me_section_ids(sections_code):
    ids = []

    sections_list = line.strip().split(',')
    ids[:1] = sections_list[0].split('-')
    ids[2:] = sections_list[1].split('-')

    return ids

num_subsets = 0
num_intersections = 0
for line in f:
    section_ids = give_me_section_ids(line)
    id1 = set(range(int(section_ids[0]), int(section_ids[1]) + 1))
    id2 = set(range(int(section_ids[2]), int(section_ids[3]) + 1))
    if id1 >= id2:
        num_subsets += 1
    elif id2 >= id1:
        num_subsets += 1
    
    if len(id1.intersection(id2)) > 0:
        num_intersections += 1

    


print(num_subsets)
print(num_intersections)
    
