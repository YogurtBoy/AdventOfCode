# f = open("lines_small.txt", "r")
# f = open("lines_medium.txt", "r")
f = open("lines.txt", "r")
if f:
    print("Successfully opened data...")

def makeListOfPoints(f):
    segments = []
    for line in f:
        points = line.split(',')
        x1 = int(points[0])
        y1 = int(points[1].split(' -> ')[0])
        x2 = int(points[1].split(' -> ')[1])
        y2 = int(points[2])
        segments.append([x1, y1, x2, y2])
    return segments

# def checkIntersection(tx, ty, seg) -> int:
#     pointIsOnLine = 0
#     x1, y1, x2, y2 = seg
#     dxSeg = x2 - x1
#     dySeg = y2 - y1
#     dxP = tx - x1
#     dyP = ty - y1
#     if dxSeg * dyP == dySeg*dxP:
#         if ((x1 >= x2 and x2 - tx >= x2 - x1) or (x1 <= x2 and x2 - tx <= x2 - x1)) \
#             and ((y1 >= y2 and y2 - ty >= y2 - y1) or (y1 <= y2 and y2 - ty <= y2 - y1)):
#             pointIsOnLine += 1
#     return pointIsOnLine

def daRealRange(n1, n2):
    if n1 == n2:
        return []
    rangeOut = []
    tn = n1
    dir = -1 if n1 > n2 else 1
    while not tn == n2:
        rangeOut.append(tn)
        tn += dir
    rangeOut.append(n2)
    return rangeOut

def findSizeOfMap(segments):
    sizeOfMap = 0
    for seg in segments:
        maxIdx = max(seg)
        if maxIdx > sizeOfMap:
            sizeOfMap = maxIdx
    sizeOfMap += 1
    return sizeOfMap

def countDoubleLaps(laps, sizeOfMap):
    doubles = 0
    for ii in range(sizeOfMap):
        for jj in range(sizeOfMap):
            if laps[ii][jj] > 1:
                doubles += 1
    return doubles

segments = makeListOfPoints(f)
sizeOfMap = findSizeOfMap(segments)
empty = [0]*sizeOfMap
laps = []
for ii in range(sizeOfMap):
    laps.append(empty[:])

# print(laps)
doubleLaps = 0
counter = 0
    
intersections = 0
# Part 1
for seg in segments:
    # Check if line is vertical or horizontal
    if seg[0] == seg[2] or seg[1] == seg[3]:
        xRange = daRealRange(seg[0], seg[2])
        yRange = daRealRange(seg[1], seg[3])
        for ii in range(max(len(xRange), len(yRange))):
            if len(xRange):
                laps[seg[1]][xRange[ii]] += 1
                if laps[seg[1]][xRange[ii]] > 1:
                    intersections += 1
            if len(yRange):
                laps[yRange[ii]][seg[0]] += 1
                if laps[yRange[ii]][seg[0]] == 2:
                    intersections += 1
                    
    counter += 1

# if sizeOfMap < 30:
#     for ii in range(len(laps)):
#         print(laps[ii])

print(intersections)
print(countDoubleLaps(laps, sizeOfMap))

print("\nPART 2")
if intersections:
    intersections = 0
laps2 = []
for ii in range(sizeOfMap):
    laps2.append(empty[:])

for seg in segments:
    xRange = daRealRange(seg[0], seg[2])
    yRange = daRealRange(seg[1], seg[3])
    for ii in range(max(len(xRange), len(yRange))):
        if len(xRange):
            tx = xRange[ii]
        else:
            tx = seg[0]
        if len(yRange):
            ty = yRange[ii]
        else:
            ty = seg[1]
        laps2[ty][tx] += 1
        if laps2[ty][tx] == 2:
            intersections += 1

print(intersections)
print(countDoubleLaps(laps2, sizeOfMap))
