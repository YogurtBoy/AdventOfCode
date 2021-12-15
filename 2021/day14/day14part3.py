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
for ii in range(len(template)):
    abc[ord(template[ii]) - 65] += 1
# print(abc)

histo = [0]*len(rules)
for ii in range(len(template) - 1):
    for jj, reaction in enumerate(rules):
        if reaction.find(template[ii] + template[ii + 1]) == 0:
            histo[jj] += 1
            break

print(histo)

steps = 0
goalSteps = 10
while steps < goalSteps:
    histoT = [0]*len(rules)
    for ii in range(len(rules)):
        letternum = ord(rules[ii][-1]) - 65
        abc[letternum] += histo[ii]
        for jj, rule in enumerate(rules):
            if rule.find(rules[ii][0] + rules[ii][-1]) == 0:
                histoT[jj] += histo[ii]
            elif rule.find(rules[ii][1] + rules[ii][-1]) == 0:
                histoT[jj] += histo[ii]
    histo = histoT[:]
    steps += 1
    print(histo)
print(abc)
                

# Template:     NNCB
# After step 1: NCNBCHB
# After step 2: NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

# print(abc)
minBin = 100000000
# min() just returns 0, so find my own min
for bin in abc:
    if bin < minBin and bin > 0:
        minBin = bin
score = max(abc) - minBin
print(score)







    
