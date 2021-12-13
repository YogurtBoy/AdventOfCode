import time
start_time = time.time()

f = open("dotMatrix_small.txt", "r")
# f = open("dotMatrix.txt", "r")
if f:
    print("Successfully opened data...")

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
        paper.add([int(coords[0]), int(coords[1])])

for fold in folds:
    newDot = [0, 0]
    if fold > 0:
        for dot in paper:
            newDot[0] = dot[0]
            if dot[1] > fold:
                newDot[1] = 2*fold - dot[1]
                paper.add(newDot)
                paper.remove(dot)
