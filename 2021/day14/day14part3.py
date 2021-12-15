import time
start_time = time.time()

# f = open("chemicals_small.txt", "r")
f = open("chemicals.txt", "r")
if f:
    print("Successfully opened data...")

def updateAlphabet(albet: list, chunk: str) -> list:
    for ii in range(len(chunk) - 1):
        albet[ord(chunk[ii]) - 65] += 1
    return albet

goalSteps = 18
def eatChunk(abc: list, first, next, depth: int):
    chunk = first + next
    for reaction in rules:
        if reaction.find(chunk) == 0:
            insertC = reaction[-1]
            abc[]
            break
    depth += 1
    if depth < goalSteps:
        abc = eatChunk(abc, chunk[0] + chunk[1], depth)
    #     abc = eatChunk(abc, chunk[1] + chunk[2], depth)
    # else:
    #     # print(time.time() - start_time)
    #     # print(chunk)
    #     abc = updateAlphabet(abc, chunk)
    # return abc

template = ''
product = []
rules = []
for line in f:
    if not len(template):
        template = line.strip()
    elif len(line) > 2:
        product = line.strip().split(' -> ')
        rules.append(product[0] + product[1])


abc = [0]*26
alb2 = abc[:]
steps = 0
while len(template) > 1:
    print(template)
    elementChunk = template[0] + template[1] # Take the first two elements in the template
    template = template[1:] # Remove the first element from the template
    abc = eatChunk(abc, elementChunk[0], elementChunk[1], 0)
    print(time.time() - start_time)


abc[ord(template) - 65] += 1
print(abc)
minBin = 100000000
# min() just returns 0, so find my own min
for bin in abc:
    if bin < minBin and bin > 0:
        minBin = bin
score = max(abc) - minBin
print(score)


    
