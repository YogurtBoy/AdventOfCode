import time
start_time = time.time()

# f = open("risk_small.txt", "r")
f = open("risk.txt", "r")
if f:
    print("Successfully opened data...")

map = []
for line in f:
    width = []
    line = line.strip()
    for ii in range(len(line)):
        width.append(int(line[ii]))
    map.append(width)

def findLowest(paths: list):
    lowestCost = 10000
    # Might be a problem if two paths have the same cost
    for item in paths: 
        if item[2] < lowestCost:
            lowestCost = cost
            (lX, lY) = (item[0], item[1])
    return (lX, lY)

def findCost(xy, paths):
    for ii, item in enumerate(paths):
        if item[0] == xy[0] and item[1] == xy[1]:
            return (ii, item[2])
    return (-1, 0)


# Start by assuming the lowest-risk path is also the shortest
# AKA movement can only happen to the right or down
width = len(map[0])
height = len(map)

# I think this is just Dijksta's algorithm
x = y = cost = lastCost = 0
paths = [(x, y, cost)]
# while x != width - 1 or y != height - 1:
while findLowest(paths) != (width - 1, height - 1):
    (x, y) = findLowest(paths)
    (iDx, cost) = findCost((x, y), paths)
    # print(cost)
    # print(x, y)
    paths.pop(iDx)
    if x < width - 1:
        costX = cost + map[y][x + 1]
        paths.append((x + 1, y, costX))
    if y < height - 1:
        costY = cost + map[y + 1][x]
        paths.append((x, y + 1, costY))
    if cost > lastCost:
        print(cost)
        lastCost = cost
    
print(cost)


# testPaths = {}
# testPaths[1] = (0, 1)
# testPaths[2] = (1, 2)
# testPaths[3] = (3, 6)
# testPaths[4] = (2, 4)
# print(findLowest(testPaths))
# print(testPaths.get(findLowest(testPaths)))



print(time.time() - start_time)
