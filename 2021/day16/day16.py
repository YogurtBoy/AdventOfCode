import time
from typing import NoReturn
start_time = time.time()

# f = open("packets_p2_e.txt", "r")
# f = open("packets_tiny.txt", "r")
# f = open("packets_small_c.txt", "r")
f = open("packets.txt", "r")
if f:
    print("Successfully opened data...")

# binary = 0b010
# print("{0:b}".format(binary))
# print(binary)

# hexo = '3b'
# print(int(hexo, 16))
# print(bin(int(hexo, 16)))

input = f.readline()
input = input.strip()

global TOTAL_VERSION
TOTAL_VERSION = 0

def trimQueue(queue, numBits):
    # Create a mask by shifting the 1 left up until the original number of bits, then flipping
    mask = (1 << numBits) - 1
    queue = queue & mask
    return queue

def parsePackets(queue, numBits):
    (version, queue, numBits) = getVersionOrType(queue, numBits)
    (typeID, queue, numBits) = getVersionOrType(queue, numBits)
    global TOTAL_VERSION
    TOTAL_VERSION += version
    if typeID == 4:
        (value, queue, numBits) = getLiteralValue(queue, numBits)
        print("LITERAL: " + str(value))
    else:
        (value, queue, numBits) = procOperator(queue, numBits, typeID)

    return (value, queue, numBits)

def getVersionOrType(queue, numBits):
    # Change numbits to the number of bits after the version/type has been stripped out
    numBits = numBits - 3

    # Get version/type by shifting the queue to the right until only relevant bits remain
    version = queue >> numBits

    queue = trimQueue(queue, numBits)
    return version, queue, numBits

def getLiteralValue(queue, numBits):
    keepCounting = 1
    value = 0
    while keepCounting:
        pQueue = bin(queue)
        numBits -= 1
        keepCounting = queue >> numBits
        queue = trimQueue(queue, numBits)
        numBits -= 4
        value = value << 4
        value = value | queue >> numBits
        queue = trimQueue(queue, numBits)
    
    return (value, queue, numBits)

def calcValue (subValue, value, typeID):
    if typeID == 0:
        value = value + subValue
    elif typeID == 1:
        value = value * subValue
    elif typeID == 2:
        value = min(value, subValue)
    elif typeID == 3:
        value = max(value, subValue)
    elif typeID == 5:
        if value > subValue: 
            value = 1
        else: 
            value = 0
    elif typeID == 6:
        if value < subValue: 
            value = 1
        else: 
            value = 0
    elif typeID == 7:
        if value == 0:
            value = subValue
        else: 
            if value == subValue: 
                value = 1
            else: 
                value = 0
    else: 
        print("Fucked up the typeID :(")
    return value

def procOperator(queue, numBits, typeID):
    numBits -= 1
    lengthID = queue >> numBits
    queue = trimQueue(queue, numBits)
    print("Operator: type " + str(lengthID))
    if lengthID:
        numBits -= 11
        numSubPackets = queue >> numBits
        queue = trimQueue(queue, numBits)
        while numSubPackets:
            (subValue, queue, numBits) = parsePackets(queue, numBits)
            if not 'value' in locals():
                value = subValue
            else:
                value = calcValue(subValue, value, typeID)
            numSubPackets -= 1
    elif not lengthID:
        numBits -= 15
        numSubBits = queue >> numBits
        queue = trimQueue(queue, numBits)
        while numSubBits > 1:
            tempBits = numBits
            (subValue, queue, numBits) = parsePackets(queue, numBits)
            if not 'value' in locals():
                value = subValue
            else:
                value = calcValue(subValue, value, typeID)
            numSubBits = numSubBits - (tempBits - numBits)
        
    return (value, queue, numBits)

numBits = 0
queue = 0
for ii in range(len(input)):
    queue = queue << 4
    queue = queue | int(input[ii], 16)
    numBits += 4

print("Original queue: ")
print(bin(queue))

(value, queue, numBits) = parsePackets(queue, numBits)

print("TOTAL_VERSION: " + str(TOTAL_VERSION))
print("TOTAL VALUE: " + str(value))
