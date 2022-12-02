# f = open('2022/day2/guide_small.txt', 'r')
f = open('2022/day2/guide.txt', 'r')

if f:
    print("Successfully opened data...")

score = 0
for line in f:
    opp, me = line.split(' ')

    # Ascii for 'A' is 65, 'X' is 88
    me_num = ord(me.strip()) - 88
    opp_num = ord(opp) - 65
    score += me_num * 3
    pick = (opp_num + me_num - 1) % 3
    score += pick + 1

print(score)