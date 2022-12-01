import time
start_time = time.time()

f = open("homework_small.txt", "r")
# f = open("homework.txt", "r")
if f:
    print("Successfully opened data...")




print("--- %s seconds ---" % (time.time() - start_time))
