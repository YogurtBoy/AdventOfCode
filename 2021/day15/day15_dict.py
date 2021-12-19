import time
start_time = time.time()

# f = open("risk_small.txt", "r")
f = open("risk_small_p2.txt", "r")
# f = open("risk.txt", "r")
if f:
    print("Successfully opened data...")

map = []
# paths = {}
for line in f:
    width = []
    line = line.strip()
    for ii in range(len(line)):
        width.append(int(line[ii]))
    map.append(width)

def findLowest(paths: list):
    lowestCost = 10000
    # Might be a problem if two paths have the same cost
    for (x, y), cost in paths.items(): 
        if cost < lowestCost:
            lowestCost = cost
            (lX, lY) = (x, y)
    return (lX, lY)

# def findCost(xy, paths):
#     for ii, item in enumerate(paths):
#         if item[0] == xy[0] and item[1] == xy[1]:
#             return (ii, item[2])
#     return (-1, 0)


# Start by assuming the lowest-risk path is also the shortest
# AKA movement can only happen to the right or down
width = len(map[0])
height = len(map)

# I think this is just Dijksta's algorithm
x = y = cost = lastCost = 0
paths = {(x, y): cost}
# while x != width - 1 or y != height - 1:
(x, y) = findLowest(paths)
while (x, y) != (width - 1, height - 1):
    cost = paths.get((x, y))
    paths.pop((x, y))
    if x < width - 1:
        costX = cost + map[y][x + 1]
        inCost = int(paths.get((x + 1, y)) or 0)
        if inCost > costX or not inCost:
            paths[(x + 1, y)] = costX
    if y < height - 1:
        costY = cost + map[y + 1][x]
        inCost = int(paths.get((x, y + 1)) or 0)
        if inCost > costY or not inCost:
            paths[(x, y + 1)] = costY
    if cost > lastCost:
        print(cost)
        lastCost = cost
    
    (x, y) = findLowest(paths)
    
print(cost)


# testPaths = {}
# testPaths[(0, 1)] = 1
# testPaths[(1, 2)] = 2
# testPaths[(3, 6)] = 3
# testPaths[(2, 4)] = 4
# # print(findLowest(testPaths))
# # print(testPaths.get(findLowest(testPaths)))
# print(testPaths.get((5, 10)))
# print(int(testPaths.get((2, 4)) or 0))


print(time.time() - start_time)
