import time
start_time = time.time()

f = open("chemicals_small.txt", "r")
# f = open("chemicals.txt", "r")
if f:
    print("Successfully opened data...")

def calculateScore(chemical: list) -> int:
    abc = [0]*26
    for element in chemical:
        abc[ord(element) - 65] += 1
    minBin = 100000
    # min() just returns 0, so find my own min
    for bin in abc:
        if bin < minBin and bin > 0:
            minBin = bin
    score = max(abc) - minBin
    return score


template = ''
product = []
rules = []
for line in f:
    if not len(template):
        template = line.strip()
    elif len(line) > 2:
        product = line.strip().split(' -> ')
        rules.append(product[0] + product[1])

steps = 0
while steps < 10:
    scroll = len(template)
    for ii in range(scroll - 1):
        ii = scroll - ii - 2
        elementPair = template[ii] + template[ii + 1]
        for reaction in rules:
            if reaction.find(elementPair) == 0:
                # str[:midPoint] + '-' + str[midPoint:]
                template = template[:(ii + 1)] + reaction[-1] + template[(ii + 1):]
                break
    
    print(len(template))
    steps += 1

print(calculateScore(template))
