import time
start_time = time.time()

# f = open("landing_small.txt", "r")
f = open("landing.txt", "r")
if f:
    print("Successfully opened data...")

splitted = f.readline().split(' ')
splittedx = splitted[2].split('..')
splittedy = splitted[3].split('..')
xZ = [int(splittedx[0].strip('x=')), int(splittedx[1].strip(','))]
yZ = [int(splittedy[0].strip('y=')), int(splittedy[1].strip(','))]
# I think I can assue that xZ[0] < xZ[1], as in you're always firing to the right

def isInZone(xpos, ypos):
    if (xZ[0] <= xpos and xpos <= xZ[1]
        and yZ[0] <= ypos and ypos <= yZ[1]):
        return True
    else:
        return False

def findLeastXInit(lastInit):
    condition = 1
    vxi = lastInit
    while condition:
        px = 0
        vxi += 1
        vx = vxi
        while vx > 0:
            px += vx
            vx -= 1
            if isInZone(px, yZ[0]):
                condition = 0
                break
            elif px > xZ[1]:
                break
    return vxi

def findMostYInit(initX, initY):
    vyi = initY
    while vyi >= yZ[0]:
        vx = initX
        px = 0
        py = 0
        vyi -= 1
        vy = vyi
        while px <= xZ[1]:
            py += vy
            vy -= 1
            px += vx
            if vx > 0:
                vx -= 1
            if isInZone(px, py):
                return True, vyi
            elif py < yZ[0] or px > xZ[1]:
                break
    return False, 0
            

vxi = vyi = 0
found = False
while not found:
    vxi = findLeastXInit(vxi)
    (found, vyi) = findMostYInit(vxi, 1000)

zenith = 1
py = 0
while zenith - py:
    zenith = py
    py += vyi
    vyi -= 1

print(zenith) # Part 1

numICs = 0
vxi = 0
while vxi < xZ[1]:
    vxi = findLeastXInit(vxi)
    vyi = 1000
    found = True
    while found:
        (found, vyi) = findMostYInit(vxi, vyi)
        if found:
            numICs += 1
            print("vxi: " + str(vxi) + "  vyi: " + str(vyi))

print(numICs)



        

print("--- %s seconds ---" % (time.time() - start_time))
