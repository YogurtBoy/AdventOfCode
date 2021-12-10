# f = open("diag_small.txt", "r")
f = open("diag.txt", "r")
if f:
    print("Successfully opened data...")
# width = 5
width = 12
ii = mcbD = lcbD = 0
diagRemain = []
# desc = [4, 3, 2, 1, 0]
desc = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# mcb = [0, 0, 0, 0, 0]
mcb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for line in f:
    diagRemain.append(line) # Part 2
    for jj in range(width):
        mcb[jj] += int(line[jj])
    ii += 1

for jj in range(width - 1, -1, -1):
    if mcb[jj] > ii/2:
        mcb[jj] = 1
    else:
        mcb[jj] = 0
    mcbD += mcb[jj]*(2**((width - 1) - jj))
lcbD = ((2**width) - 1) - mcbD 

print("Part 1: " + str(mcbD*lcbD) + "\n")

diagRemainMT = diagRemain[:]
diagRemainM = diagRemain[:]
diagRemainLT = diagRemain[:]
diagRemainL = diagRemain[:]

for ii in range(width):
    mcb2 = 0
    lcb2 = 0
    for jj in diagRemainM:
        mcb2 += int(jj[ii])
    if mcb2 < len(diagRemainMT)/2:
        mcb2 = 0
    else:
        mcb2 = 1

    for kk in diagRemainM:
        if(len(diagRemainM) <= 1):
            break

        # print("Comparing index " + str(ii) + " of " + kk + " against mcb " + str(mcb2))

        if not int(kk[ii]) == mcb2:
            # print("Removing...")
            diagRemainMT.remove(kk)
    
    diagRemainM = diagRemainMT[:]

    for jj in diagRemainL:
        lcb2 += int(jj[ii])
    if lcb2 < len(diagRemainLT)/2:
        lcb2 = 1
    else:
        lcb2 = 0

    for kk in diagRemainL:
        if(len(diagRemainL) <= 1):
            break

        if not int(kk[ii]) == lcb2:
            diagRemainLT.remove(kk)
    
    diagRemainL = diagRemainLT[:]

    print(diagRemainL)

oxygen = 0
carbon = 0
for decNum in desc:
    oxygen += int(diagRemainM[0][decNum])*(2**((width - 1) - decNum))
    carbon += int(diagRemainL[0][decNum])*(2**((width - 1) - decNum))
print(oxygen)
print(carbon)
print(oxygen*carbon)
    
        
    
    # print("mcb2: " + str(mcb2))

