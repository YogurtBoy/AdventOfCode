
numStrings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numWords = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dig1 = 'a'
sum = 0
with open('2023/day1/calibration.txt', 'r') as f:
    for line in f:
        for idx, char in enumerate(line):
            for numIdx, word in enumerate(numWords):
                if word in line[idx:(idx + len(word))]:
                    if dig1 == 'a':
                        dig1 = numStrings[numIdx]
                    dig2 = numStrings[numIdx]
            if char in numStrings and dig1 == 'a':
                dig1 = char
            if char in numStrings:
                dig2 = char
        sum = sum + int(dig1 + dig2) # Combine the digits while they're strings, then convert to a number and add to total
        dig1 = 'a'

print(sum)
            