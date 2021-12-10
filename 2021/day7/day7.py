import time
start_time = time.time()

# f = open("crabs_small.txt", "r")
f = open("crabs.txt", "r")
if f:
    print("Successfully opened data...")

gang = []
gang_str = f.read().split(",")
max_crab = 0
for crab in gang_str:
    gang.append(int(crab))
    if int(crab) > max_crab:
        max_crab = int(crab)
    
# cost_list = []
# min_cost = 100000000000000000000000000000000000000000000000000000000000
# for ii in range(max_crab + 1):
#     cost = 0
#     for crab in gang:
#         cost += abs(ii - crab)
#     if min_cost > cost:
#         min_cost = cost
cost_list = [1]
for ii in range(2, max_crab + 1):
    cost_list.append(cost_list[ii - 2] + ii)
min_cost = 100000000000000000000000000000000000000000000000000000000000

for ii in range(max_crab + 1):
    cost = 0
    for crab in gang:
        cost += cost_list[abs(crab - ii) - 1]
    if min_cost > cost:
        min_cost = cost
    

print(min_cost)


print("--- %s seconds ---" % (time.time() - start_time))


