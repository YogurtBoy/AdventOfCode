# f = open("diag_small.txt", "r")
f = open("diag.txt", "r")
if f:
    print("Successfully opened data...")

def mcb(nums: list) -> str:
    mcbStr = [0] * (len(nums[0]) - 1) # declare list the same width as the input
    for word in nums:
        for jj in range(len(mcbStr) - 1):
            mcbStr[jj] += int(word[jj])
    for jj in range(len(mcbStr)):
            if mcbStr[jj] < len(nums)/2:
                mcbStr[jj] = '0'
            else: 
                mcbStr[jj] = '1'
    return ''.join(mcbStr)

    


diags = []
diagsStr = []
for line in f:
    diagsStr.append(line)
# diags = zip(*diagsStr)
width = len(diagsStr[0]) - 1

mSOBNGAOEUGB = mcb(diagsStr)
print(mSOBNGAOEUGB)
gamma = int(mSOBNGAOEUGB, 2)
epsilon = (2**width - 1) - gamma
gamep = gamma*epsilon
print(gamep)



