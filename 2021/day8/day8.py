import time
start_time = time.time()

# f = open("notes_tiny.txt", "r")
# f = open("notes_small.txt", "r")
f = open("notes.txt", "r")
if f:
    print("Successfully opened data...")

# after = 0
# numnums = 0
# for line in f:
#     after = 0
#     display = line.split()
#     for note in display:
#         if note == "|":
#             print("After!")
#             after = 1
#             continue
#         if after:
#             print(note)
#             if (len(note) == 2 or 
#                 len(note) == 3 or
#                 len(note) == 4 or
#                 len(note) == 7):
#                 numnums += 1
#         else:
#             continue


#   a b c d e f g
# m 0 0 0 0 0 0 0
# n 0 0 0 0 0 0 0
# o 0 0 0 0 0 0 0
# p 0 0 0 0 0 0 0
# q 0 0 0 0 0 0 0
# r 0 0 0 0 0 0 0
# s 0 0 0 0 0 0 0

#   aaaa     mmmm 
#  b    c   n    o
#  b    c   n    o
#   dddd     pppp 
#  e    f   q    r
#  e    f   q    r
#   gggg     ssss 


# print(numnums)
# print("--- %s seconds ---" % (time.time() - start_time))

def checkStringForChars(chars, str):
    for c in chars:
        isIn = False
        for s in str:
            if c == s:
                isIn = True
        if not isIn:
            return False
    return True

total_report = 0
for line in f:
    key = []
    output = []
    map = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    outputStr = ''
    after = 0
    display = line.split()
    for note in display:
        if note == "|":
            after = 1
            continue
        if after:
            output.append(note)
        else:
            key.append(note)

    # print(key)
    # print(output)

    unfilled = 1
    oneChars = 'z'
    sixChars = 'z'
    fourChars = 'z'
    sevenChars = 'z'
    while unfilled:
        for ii, dig in enumerate(key):
            if len(dig) == 2:
                map[ii] = 1
                oneChars = dig
                # oneChars = set(dig)
            if len(dig) == 4:
                map[ii] = 4
                # fourChars = set(dig)
                fourChars = dig
            if len(dig) == 3:
                map[ii] = 7
                sevenChars = dig
            if len(dig) == 7:
                map[ii] = 8
                sevenChars = dig
            if len(dig) == 6:
                if checkStringForChars(fourChars, dig):
                    map[ii] = 9
                elif checkStringForChars(oneChars, dig):
                    map[ii] = 0
                elif len(fourChars) > 1 and len(oneChars) > 1:
                    map[ii] = 6
                    sixChars = dig
                    # sixChars = set(dig)
            if len(dig) == 5:
                # elif all(c in sixChars for c in dig): Y no work?
                if checkStringForChars(dig, sixChars):
                    map[ii] = 5
                # elif all((c in oneChars) for c in dig):
                elif checkStringForChars(oneChars, dig):
                    map[ii] = 3
                else:
                    map[ii] = 2
            # print(map)
            
        if sum(map) == 45:
            unfilled = 0
    
    for digit in output:
        for number in key:
            if checkStringForChars(digit, number) and len(digit) == len(number):
                outputStr += str(map[key.index(number)])
                break
        # outputStr += str(map[(checkStringForChars(number, digit) for number in key)])
        # outputStr += str(map[key.index(digit)])
    print('')
    print(output)
    print(map)
    print(outputStr)
    total_report += int(outputStr)



print(total_report)
