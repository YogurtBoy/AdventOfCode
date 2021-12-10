# f = open("trajectory_small.txt", "r")
f = open("trajectory.txt", "r")
if f:
    print("Successfully opened data... \n")

x_pos = 0
y_pos = 0
nums = []
words = []
aim = 0
dep2 = 0
for line in f:
    structions = line.split()
    words.append(structions[0])
    nums.append(int(structions[1]))
    if structions[0][0] == 'f':
        x_pos += int(structions[1]) # part 1
        dep2 += aim * int(structions[1]) # part 2
    elif structions[0][0] == 'u':
        y_pos -= int(structions[1]) # part 1
        aim -= int(structions[1]) # part 2
    elif structions[0][0] == 'd':
        y_pos += int(structions[1]) # part 1
        aim += int(structions[1]) # part 2
    print("X: " + str(x_pos) + "    Y: " + str(y_pos) + "\n")

print(y_pos*x_pos) # part 1

print(x_pos * dep2) # part 2

