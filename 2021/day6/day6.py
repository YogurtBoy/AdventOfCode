import time
start_time = time.time()
# f = open("fish_small.txt", "r")
# f = open("fish_kellen.txt", "r")
f = open("fish.txt", "r")
# if f:
#     print("Successfully opened data...")

family = []
family_str = f.read().split(",")
for fish in family_str:
    family.append(int(fish))

t = 0
# t_end = 18
t_end = 256
# print(family)

# PART ONE
# while t < t_end:
#     for ii in range(len(family)):
#         if not family[ii]:
#             family[ii] = 6
#             family.append(8)
#         else: 
#             family[ii] -= 1
#     print(t)
#     print(len(family))
#     print("")
#     t += 1

histo = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for ii in family:
    histo[ii] += 1
# print(histo)

# while t < t_end: 
#     histoTemp = histo[:]
#     histo[0] = histoTemp[1]
#     histo[1] = histoTemp[2]
#     histo[2] = histoTemp[3]
#     histo[3] = histoTemp[4]
#     histo[4] = histoTemp[5]
#     histo[5] = histoTemp[6]
#     histo[6] = histoTemp[0] + histoTemp[7]
#     histo[7] = histoTemp[8]
#     histo[8] = histoTemp[0]
#     # print(histo)
#     t += 1
babymakers = 0
while t < t_end: 
    babymakers = histo[0]
    histo[0] = histo[1]
    histo[1] = histo[2]
    histo[2] = histo[3]
    histo[3] = histo[4]
    histo[4] = histo[5]
    histo[5] = histo[6]
    histo[6] = histo[7] + babymakers
    histo[7] = histo[8]
    histo[8] = babymakers
    # print(histo)
    t += 1


total = 0
for bin in histo:
    total += bin

print(total)



# print("--- %s seconds ---" % (time.time() - start_time))
print(time.time())
print(start_time)
