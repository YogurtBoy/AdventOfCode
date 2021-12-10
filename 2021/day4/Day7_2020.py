from dataclasses import dataclass

@dataclass
class Bag:
    mycolor: str = ''
    contains: str = ''

f = open("bag_rules_d7_2020.txt", "r")
# f = open("bag_rules_d7_2020_small.txt", "r")
# f = open("bag_rules_d7_2020_small_2.txt", "r")
if f:
    print("Successfully opened data... \n")

bagList = []

shinyGoldBag = Bag('shiny gold')

ii = 0

for line in f:
    tempBag = Bag()
    data = line.split()
    for index, word in enumerate(data):
        if "bag" in word:
            bag_name = ' '.join([data[index - 2], data[index-1]])
            if index < 3:
                tempBag.mycolor = bag_name
            else: 
                bag_name = ' '.join([data[index - 3], bag_name])
                tempBag.contains = tempBag.contains + ' ' + bag_name

    bagList.append(tempBag)
    ii += 1
    # if ii > 1:
    #     break

print(bagList)

# Part 1
bagSet = set()
def innardBagTypes(Bag):
    for parent in bagList:
        mycolor = parent.mycolor
        contains = parent.contains
        if Bag.mycolor in contains:
            innardBagTypes(parent)
            bagSet.add(mycolor)
    return

innardBagTypes(shinyGoldBag)
print("Length of bagSet: " + str(len(bagSet)) + "\n")

# print(bagSet)

# Part 2
def numInsideBags(Bag):
    numContains = 1
    for child in bagList:
        bagColor = Bag.mycolor
        bagContains = Bag.contains
        print("Looking for " + child.mycolor + " in " + bagContains)
        foundColor = bagContains.find(child.mycolor)
        
        print("Found number " + bagContains[foundColor - 2] + " at " + str(foundColor) + "... \n")
        
        if foundColor > 0:
            foundNumber = int(bagContains[foundColor - 2])
            numContains += foundNumber * numInsideBags(child)

    print(Bag.mycolor + " bags contain " + str(numContains) + " other bags! \n")
    return numContains

numBags = 0
for bag in bagList:
    if bag.mycolor == shinyGoldBag.mycolor:
        numBags += numInsideBags(bag)
print("Number of contained bags: " + str(numBags) + "\n")

f.close()