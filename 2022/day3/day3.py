# f = open('2022/day3/rucksacks_small.txt', 'r')
f = open('2022/day3/rucksacks.txt', 'r')

if f:
    print("Successfully opened data...")

def convert_to_set(sack):
    str_set = set()
    for ii in range(len(sack)):
        str_set.add(sack[ii])
    return str_set

def score_list(misplaced):
    score = 0
    for jj in range(len(misplaced)):
        priority = ord(misplaced[jj]) - 38 # 38 is 65 (the ascii value of 'A') - 27 (value of 'A' from the problem)
        if priority > 54:
            priority -= 58
        score += priority
    return score

score = 0
badges = []
mishaps = []
rucksacks = []
for line in f:
    rucksacks.append(line.strip())
    comp_size = int(len(line.strip()) / 2)
    comp_1 = set()
    comp_2 = set()
    for ii in range(comp_size):
        comp_1.add(line[ii])
        comp_2.add(line[ii + comp_size])
    onion = comp_1.intersection(comp_2)
    mishaps.append(onion.pop())

for kk in range(int(len(rucksacks)/3)):
    lin1 = convert_to_set(rucksacks[kk * 3])
    lin2 = convert_to_set(rucksacks[kk * 3 + 1])
    lin3 = convert_to_set(rucksacks[kk * 3 + 2])
    badge_onion = lin1.intersection(lin2, lin3).pop()
    print(badge_onion)
    badges.append(badge_onion)

p1_score = score_list(mishaps)
p2_score = score_list(badges)

print(p2_score)