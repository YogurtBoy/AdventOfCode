import time
start_time = time.time()

# f = open('2022/day8/treemap_small.txt', 'r')
f = open('2022/day8/treemap.txt', 'r')

if f:
    print("Successfully opened data...")

# Generate map
map = []
for line in f:
    map.append([])
    for height in line.strip():
        map[-1].append(int(height))
        
map_size = len(map[0])

# Return 1 if the tree is visible, 0 if not
def check_visibility(row, col):
    # print(str(row) + ', ' + str(col))
    height_here = map[row][col]
    is_visible = 0
    score = 1

    # Check visibility from left
    view_distance_from_left = col
    visible_from_left = 1
    for mm in range(col - 1, -1, -1):
        if map[row][mm] >= height_here:
            visible_from_left = 0
            view_distance_from_left = col - mm
            break
    score = score * view_distance_from_left
    is_visible = is_visible or visible_from_left

    view_distance_from_right = map_size - col - 1
    visible_from_right = 1
    for mm in range(col + 1, map_size):
        if map[row][mm] >= height_here:
            visible_from_right = 0
            view_distance_from_right = (mm - col)
            break
    score = score * view_distance_from_right
    is_visible = is_visible or visible_from_right

    view_distance_from_top = row
    visible_from_top = 1
    for mm in range(row - 1, -1, -1):
        if map[mm][col] >= height_here:
            visible_from_top = 0
            view_distance_from_top = (row - mm)
            break
    score = score * view_distance_from_top
    is_visible = is_visible or visible_from_top

    view_distance_from_bottom = map_size - row - 1
    visible_from_bottom = 1
    for mm in range(row + 1, map_size):
        if map[mm][col] >= height_here:
            visible_from_bottom = 0
            view_distance_from_bottom = (mm - row)
            break
    score = score * view_distance_from_bottom
    is_visible = is_visible or visible_from_bottom

    return is_visible, score

max_tree_score = 0
num_visible_trees = 0
for ii in range(1, map_size - 1):
    for jj in range(1, map_size - 1):
        (this_tree_is_visible, this_tree_score) = check_visibility(ii, jj)
        num_visible_trees += this_tree_is_visible
        if this_tree_score > max_tree_score:
            max_tree_score = this_tree_score

num_visible_trees += map_size * 4 - 4

print(num_visible_trees)
print(max_tree_score)



print("--- %s seconds ---" % (time.time() - start_time))