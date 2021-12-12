import time
start_time = time.time()

# f = open("puses_example.txt", "r")
f = open("puses.txt", "r")
if f:
    print("Successfully opened data...")

def energizePuses(octos: list, y: int, x: int):
    itin = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for ii in range(len(itin)):
        yT = itin[ii][0] + y
        xT = itin[ii][1] + x
        if not yT or not xT or yT == (len(octos) - 1) or xT == (len(octos[0]) - 1):
            continue
        else:
            octos[yT][xT] += 1
            if octos[yT][xT] == 10:
                octos = energizePuses(octos, yT, xT)

    return octos

def tallyFlashes(octos: list):
    flashes = 0
    for ii in range(len(octos)):
        for jj in range(len(octos[0])):
            if not ii or not jj or ii == (len(octosPlus) - 1) or jj == (len(octosPlus[0]) - 1):
                continue
            else:
                if octos[ii][jj] > 9:
                    flashes += 1
                    octos[ii][jj] = 0

    return flashes



octosLame = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
octos = []
octosPlus = []
octosPlus.append(octosLame[:])
for line in f:
    line = line.strip()
    width = []
    for ii, num in enumerate(line):
        width.append(int(num))
    octos.append(width[:])
    width.insert(0, 0)
    width.append(0)
    octosPlus.append(width)
octosPlus.append(octosLame[:])

# print(octos)
# print(octosPlus)
totalFlashes = 0
transit = 0
totSum = 1
# while transit < 100: # For part 1
while totSum:
    totSum = 0
    print("TRANSIT NUMBER: " + str(transit))
    for ii in range(len(octosPlus)):
        for jj in range(len(octosPlus[0])):
            if not ii or not jj or ii == (len(octosPlus) - 1) or jj == (len(octosPlus[0]) - 1):
                continue
            else:
                octosPlus[ii][jj] += 1
                if octosPlus[ii][jj] == 10:
                    octosPlus = energizePuses(octosPlus, ii, jj)
    totalFlashes += tallyFlashes(octosPlus)
    # print(totalFlashes)
    for kk in range(12):
        print(octosPlus[kk])
    transit += 1


    for kk in range(10):
        totSum += sum(octosPlus[kk + 1])

print(totalFlashes)

print("--- %s seconds ---" % (time.time() - start_time))


