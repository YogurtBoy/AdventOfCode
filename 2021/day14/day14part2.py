import time
start_time = time.time()

f = open("chemicals_small.txt", "r")
# f = open("chemicals.txt", "r")
if f:
    print("Successfully opened data...")

def updateAlphabet(albet: list, chunk: str) -> list:
    for ii in range(len(chunk) - 1):
        albet[ord(chunk[ii]) - 65] += 1
    return albet

goalSteps = 4
def eatChunk(abc: list, chunk: str, depth: int):
    for reaction in rules:
        if reaction.find(chunk) == 0:
            chunk = chunk[0] + reaction[-1] + chunk[1]
            break
    depth += 1
    if depth < goalSteps:
        abc = eatChunk(abc, chunk[0] + chunk[1], depth)
        abc = eatChunk(abc, chunk[1] + chunk[2], depth)
    else:
        print(chunk)

    abc = updateAlphabet(abc, chunk)
    return abc

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
    elementChunk = template[0] + template[1] # Take the first two elements in the template
    template = template[1:] # Remove the first element from the template
    abc = eatChunk(abc, elementChunk, 0)
    # for reaction in rules:
    #     if reaction.find(elementChunk) == 0:
    #         elementChunk = elementChunk[0] + reaction[-1] + elementChunk[1]
    #         break
    # abc = updateAlphabet(abc, elementChunk)

abc[ord(template) - 65] += 1
print(updateAlphabet(alb2, 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'))
print(abc)
minBin = 100000000
# min() just returns 0, so find my own min
for bin in abc:
    if bin < minBin and bin > 0:
        minBin = bin
score = max(abc) - minBin
print(score)


    
