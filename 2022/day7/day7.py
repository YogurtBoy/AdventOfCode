# f = open('2022/day7/directory_small.txt', 'r')
f = open('2022/day7/directory.txt', 'r')

if f:
    print("Successfully opened data...")

dir_sizes = {}
for line in f:
    if line[0:6] == '$ cd /':
        curr_dir = []
    elif line[0:7] == '$ cd ..':
        curr_dir.pop()
    elif line[0:4] == '$ cd':
        parts = line.split(' ')
        dir_name = parts[-1].strip()
        curr_dir.append(dir_name)
    elif line[0:3] == 'dir':
        parts = line.split(' ')
        dir_name = parts[-1].strip()
        dir_sizes[dir_name] = 0
    elif ord(line[0]) >= 48 and ord(line[0]) <= 57:
        parts = line.split(' ')
        for ii in range(len(curr_dir)):
            dir_sizes[curr_dir[ii]] += int(parts[0])

print(dir_sizes)

lil_sizes = 0
all_dirs = list(dir_sizes)
for jj in range(len(all_dirs)):
    if dir_sizes[all_dirs[jj]] <= 100000:
        lil_sizes += dir_sizes[all_dirs[jj]]
    else: 
        print(dir_sizes[all_dirs[jj]])
        

print(lil_sizes)


