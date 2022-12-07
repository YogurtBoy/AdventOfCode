# f = open('2022/day5/manifest_small.txt', 'r')
f = open('2022/day5/manifest.txt', 'r')

if f:
    print("Successfully opened data...")

manifest = []

def shift_cargo_p1(cnt, src, dest):
    for mm in range(cnt):
        crate = manifest[src].pop()
        manifest[dest].append(crate)
    return

def shift_cargo_p2(cnt, src, dest):
    orig_len = len(manifest[src])
    move_stack = manifest[src][orig_len - cnt:orig_len]
    manifest[dest].extend(move_stack)
    del manifest[src][orig_len - cnt:orig_len]
    
    return

for line in f:
    if line[0] == 'm':
        instr = line.split(' ')
        n_move = int(instr[1])
        source_stack = int(instr[3]) - 1
        dest_stack = int(instr[5]) - 1
        shift_cargo_p2(n_move, source_stack, dest_stack)

    elif '[' in line:
        for ii in range(int(len(line)/4)):
            if len(manifest) < ii + 1:
                manifest.append([])
            crate_ind = ii * 4 + 1 
            if line[crate_ind] != ' ':
                manifest[ii].insert(0, line[crate_ind])

print(manifest)

cream = ''
for nn in range(len(manifest)):
    cream = cream + manifest[nn][-1]

print(cream)