f = open("day8/antennae.txt", "r")

def get_antinodes(p1, p2):
    rise = p1[1] - p2[1]
    run = p1[0] - p2[0]
    a1 = [p1[0] + run, p1[1] + rise]
    a2 = [p2[0] - run, p2[1] - rise]
    return (a1, a2)

def check_antenna(locations):
    print()

    node_list = []
    for ii, p in enumerate(locations):
        print(p)
        for jj in range(ii + 1, len(locations)):
            (a1, a2) = get_antinodes(p, locations[jj])
            print(a1, a2)
            node_list.append(a1)
            node_list.append(a2)

    return node_list

antennae = {}
for ii, line in enumerate(f):
    for jj, letter in enumerate(line.strip()):
        if letter != '.':
            if letter in antennae:
                antennae[letter].append([jj, ii])
            else:
                antennae[letter] = [[jj, ii]]

width = len(line.strip())
length = ii + 1

unique_antinodes = []
for antenna in antennae.keys():
    an_l = check_antenna(antennae[antenna])
    for node in an_l: 
        if node not in unique_antinodes:
            if node[0] >= 0 and node[1] >= 0 and node[0] < width and node[1] < length:
                unique_antinodes.append(node)

print(unique_antinodes)
print(len(unique_antinodes))


f.close()