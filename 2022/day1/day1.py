# f = open('2022/day1/calorie_list_small.txt', 'r')
f = open('2022/day1/calorie_list.txt', 'r')

if f:
    print("Successfully opened data...")

stronkest = [0]*3
max_cals = 0
carried_cals = 0
# for line in f:
#     if line[0] == '\n':
#         for ii in range(len(stronkest)):
#             if carried_cals > stronkest[ii]:
#                 print("FOUND ONE BIGGER!")
#                 jj = len(stronkest) - 1
#                 while jj > ii:
#                     stronkest[jj] = stronkest[jj - 1]
#                     jj = jj - 1
#                 stronkest[ii] = carried_cals
#                 print(stronkest)
#                 break
        
#         carried_cals = 0
#     else:
#         carried_cals = int(line) + carried_cals
# print(stronkest)
# print(stronkest[0] + stronkest[1] + stronkest[2])

elfbags = [0]
for line in f:
    if line[0] != '\n':
        elfbags[-1] += int(line)
    else:
        elfbags.append(0)

elfbags.sort(reverse=True)

print(sum(elfbags[0:3]))