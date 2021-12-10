import time
start_time = time.time()

# f = open("navigation_small.txt", "r")
f = open("navigation.txt", "r")
if f:
    print("Successfully opened data...")

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
illegal = [3, 57, 1197, 25137]

syntaxScore = 0
autoScore = []
for line in f:
    illegalFlag = False
    record = []
    for char in line:
        # Keep an ordered record of pending open brackets
        if char in openers:
            place = openers.index(char)
            record.append(place)
        elif char in closers:
            place = closers.index(char)
            # If a closing bracket doesn't match the outstanding open bracket, trip the loop
            if place != record[-1]:
                syntaxScore += illegal[place]
                illegalFlag = True
                break
            # Else remove the outstanding open bracket
            else:
                record.pop()
    # Find unfinished records that aren't illegal
    if len(record) and not illegalFlag:
        autoScoreT = 0
        # Scroll backwards through the remaining list record?
        for ii in range(len(record) - 1, -1, -1): 
            autoScoreT = 5 * autoScoreT + record[ii] + 1
        autoScore.append(autoScoreT)

# Find and save median
autoScore.sort()
autoScoreFinal = autoScore[int(len(autoScore)/2)]

# Part one 
print(syntaxScore)

# Part 2
print(autoScoreFinal)

print("--- %s seconds ---" % (time.time() - start_time))


