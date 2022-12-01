import time
start_time = time.time()

# f = open("risk_small.txt", "r")
# f = open("risk_small_p2.txt", "r")
f = open("risk.txt", "r")
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
    lowestCost = 100000
    # Might be a problem if two paths have the same cost
    for (x, y), cost in paths.items(): 
        if cost < lowestCost:
            lowestCost = cost
            (lX, lY) = (x, y)
    return (lX, lY)

def getRisk(x, y):
    ogRisk = map[y%len(map)][x%len(map[0])]
    bigRisk = ogRisk + int(y/len(map)) + int(x/len(map[0]))
    risk = (bigRisk - 1)%9 + 1
    return risk

# Start by assuming the lowest-risk path is also the shortest
# AKA movement can only happen to the right or down
# PART 2 - Alter map so it's a tile
width = len(map[0])*5
height = len(map)*5
bigLowest = [100000]*width
lowestMap = []
for ii in range(height):
    lowestMap.append(bigLowest[:])
    

# I think this is just Dijksta's algorithm
x = y = cost = lastCost = 0
paths = {(x, y): cost}
(x, y) = findLowest(paths)
while (x, y) != (width - 1, height - 1):
    cost = paths.get((x, y))
    paths.pop((x, y))
    if x < width - 1:
        costX = cost + getRisk(x + 1, y)
        inCost = int(paths.get((x + 1, y)) or 0)
        if inCost > costX or not inCost:
            paths[(x + 1, y)] = costX
    if y < height - 1:
        costY = cost + getRisk(x, y + 1)
        inCost = int(paths.get((x, y + 1)) or 0)
        if inCost > costY or not inCost:
            paths[(x, y + 1)] = costY
    # if cost > lastCost:
    #     print(cost)
    #     lastCost = cost
    print(len(paths))
    
    (x, y) = findLowest(paths)
    
print(cost)



print(time.time() - start_time)
