# f = open("pulses.txt", "r")
f = open("pulses_small.txt", "r")
# f = open("bag_rules_d7_2020_small.txt", "r")
# f = open("bag_rules_d7_2020_small_2.txt", "r")
if f:
    print("Successfully opened data... \n")

lastestLine = 0
lastLine = 0
increases = 0
lineNum = 0
rolling = 0
lastRolling = 0
rollIncreases = 0
for line in f:
    lineNum = int(line)
    rolling = lastestLine + lastLine + lineNum
    # if int(line) > lastLine:
    #     increases = increases + 1
    if rolling > lastRolling:
        rollIncreases = rollIncreases + 1
    lastestLine = lastLine
    lastLine = int(line)
    lastRolling = rolling
    
print(increases)
print(rollIncreases)