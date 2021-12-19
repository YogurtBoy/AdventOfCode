import time
start_time = time.time()

f = open("packets_tiny.txt", "r")
# f = open("packets_small.txt", "r")
# f = open("packets.txt", "r")
if f:
    print("Successfully opened data...")

binary = 0b010
print("{0:b}".format(binary))
print(binary)

hexo = '3b'
print(int(hexo, 16))
print(bin(int(hexo, 16)))

input = f.readline()

queue = 0b0
for ii in range(len(input)):
    stage = input[ii]
    # print(stage)
    # queue << 4
    # queue = queue | bin(int(stage, 16))
    print(type(bin(int(stage, 16))))