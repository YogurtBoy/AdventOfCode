import time
start_time = time.time()

# f = open("dotMatrix_small.txt", "r")
f = open("dotMatrix.txt", "r")
if f:
    print("Successfully opened data...")

def findMax(paper):
    maxX = maxY = 0
    for dot in paper:
        if dot[0] > maxX:
            maxX = dot[0]
        if dot[1] > maxY:
            maxY = dot[1]
    return maxX, maxY

maxX = maxY = 0
folds = []
paper = set()
for line in f:
    if len(line) > 10: # Lines that have folds
        print(line[13:-1])
        along = int(line[13:-1])
        if line[11] == 'x':
            folds.append(along)
        else:
            folds.append(-1*along)
    elif len(line) > 2: # Lines that aren't just a \n
        coords = line.strip().split(',')
        paper.add((int(coords[0]), int(coords[1])))


print(paper)
for fold in folds:
    paperT = set()
    # Check if fold is x (positive) or y (negative)
    if fold < 0:
        fold *= -1
        for dot in paper:
            # Only reflect dots that are on the opposite side of the fold
            if dot[1] > fold:
                newDot = (dot[0], 2*fold - dot[1])
                paperT.add(newDot)
            else:
                paperT.add(dot)
    else:
        for dot in paper:
            # Only reflect dots that are on the opposite side of the fold
            if dot[0] > fold:
                newDot = (2*fold - dot[0], dot[1])
                paperT.add(newDot)
            else:
                paperT.add(dot)
    paper = paperT
    print(len(paperT))

# print(paper)
(maxX, maxY) = findMax(paper)
zeros = ['.']*(maxX + 1)
origami = []
for ii in range(maxY + 1):
    origami.append(zeros[:])

for dot in paper:
    origami[dot[1]][dot[0]] = '0'

for ii in range(maxY + 1):
    print(origami[ii])

