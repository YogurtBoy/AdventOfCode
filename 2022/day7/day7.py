# f = open('2022/day7/directory_small.txt', 'r')
from http.client import REQUEST_TIMEOUT


f = open('2022/day7/directory.txt', 'r')

if f:
    print("Successfully opened data...")

dir_sizes = {'/': 0}  # dir_sizes holds the total size of each directory as values, with dir name as keys
for line in f:
    # This isn't totally necessary, but if we go to the top level folder that means we aren't in the contenst of any other folder
    if line[0:6] == '$ cd /':
        curr_dir = ['/']  # curr_dir is the list of all of the folders we are inside; if we did 'cd A' and then 'cd B', it would contain A and B
    
    # If we go up a folder on the tree, it means that any following data won't be counted as inside of the folder
    elif line[0:7] == '$ cd ..':
        removed_dir = curr_dir.pop()

    # Moving down into a folder should add it to the list of folders we are inside
    elif line[0:4] == '$ cd':
        # Extract the folder from the line
        parts = line.split(' ')
        dir_name = parts[-1].strip()

        # Check if a different directory of the same name has already been counted
        while dir_name in dir_sizes:
            dir_name = dir_name + '1'

        dir_sizes[dir_name] = 0   
        curr_dir.append(dir_name)
    
    # # Nothing happens to the folder here except that a new folder is added to the dictionary of directories and their sizes
    # elif line[0:3] == 'dir':
    #     parts = line.split(' ')
    #     dir_name = parts[1].strip()
    #     # Make sure the directory isn't already known
    #     while dir_name in list(dir_sizes):
    #         dir_name = dir_name + '1'
            
    #     dir_sizes[dir_name] = 0
    
    # This section adds a file's size to every containint folder's score
    elif ord(line[0]) >= 48 and ord(line[0]) <= 57:
        parts = line.split(' ')
        for ii in range(len(curr_dir)):
            dir_sizes[curr_dir[ii]] += int(parts[0])



lil_sizes = 0
all_dirs = list(dir_sizes)
all_sizes = []
for jj in range(len(all_dirs)):
    if dir_sizes[all_dirs[jj]] <= 100000:
        lil_sizes += dir_sizes[all_dirs[jj]]

    all_sizes.append(dir_sizes[all_dirs[jj]])

required_space = dir_sizes['/'] - 40000000
all_sizes.sort()
for mm in range(len(all_sizes)):
    if all_sizes[mm] >= required_space:
        print(all_sizes[mm])
        break


        

print(lil_sizes)


