import time
start_time = time.time()

# f = open("map_small.txt", "r")
f = open("map.txt", "r")
if f:
    print("Successfully opened data...")

# (Recursive) Returns a set that contains all the points in a point's basin
def findBasinSize(ii: int, jj: int, map: list, pointSet: set) -> set:
    pointSetLen0 = len(pointSet)
    pointSet.add((ii, jj))
    if len(pointSet) == pointSetLen0:
        return pointSet
    if map[ii][jj + 1] < 9:
        pointSet = findBasinSize(ii, jj + 1, map, pointSet)
    if map[ii + 1][jj] < 9:
        pointSet = findBasinSize(ii + 1, jj, map, pointSet)
    if map[ii][jj - 1] < 9:
        pointSet = findBasinSize(ii, jj - 1, map, pointSet)
    if map[ii - 1][jj] < 9:
        pointSet = findBasinSize(ii - 1, jj, map, pointSet)
    return pointSet

# Returns the product of all elements in list
def productL(listIn):
    product = 1
    for ii in range(len(listIn)):
        product *= listIn[ii]
    return product

# Convert map to 2D list
map = []
for line in f:
    horiz = []
    line = line.strip()
    for hae in line:
        horiz.append(int(hae))
    map.append(horiz)
    

map_width = len(horiz)
map_height = len(map)

# Make copy of map with edges of 9s
fringey = [row[:] for row in map] # fringey = map[:] does not work (because map is nested list)
for width in fringey:
    width.insert(0, 9)
    width.append(9)
manys = [9] * (map_width + 2)
fringey.insert(0, manys)
fringey.append(manys)

# Go through each point on the map and check if each adjacent point is higher
pointSet = set()  # Empty set (does python deallocate variables out of for loop scope?)
topBasinSizes = [0, 0, 0]
total_risk = 0 # Part 1 answer
# Iterate through all points on the map
for ii, width in enumerate(map):
    for jj, height in enumerate(width):
        # Check if the given point is surrounded by only points of greater height
        if (fringey[ii][jj + 1] > map[ii][jj]
        and fringey[ii + 1][jj] > map[ii][jj]
        and fringey[ii + 2][jj + 1] > map[ii][jj]
        and fringey[ii + 1][jj + 2] > map[ii][jj]):
            pointSet = set() # Empty set
            total_risk += map[ii][jj] + 1 # If minimum, add risk level of minimum to total
            pointSet = findBasinSize(ii + 1, jj + 1, fringey, pointSet)
            # Each time, check to see if the size of the basin is in the top three basin sizes
            for tres in range(3):
                if topBasinSizes[tres] <= len(pointSet):
                    topBasinSizes.insert(tres, len(pointSet))
                    topBasinSizes.pop(3)
                    break

print(total_risk) # Part 1 answer
print(productL(topBasinSizes)) # Part 2 answer

print("--- %s seconds ---" % (time.time() - start_time))


