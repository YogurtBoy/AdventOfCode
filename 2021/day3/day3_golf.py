f = open("trajectory.txt", "r")

x = y = a = d = 0
for l in f:
    x += (not (ord(l[0]) - 102)) * int(l[-2])
    y += (ord(l[0]) - 102 < 0) * int(l[-2]) - ((ord(l[0]) - 102) > 0) * int(l[-2])
    d += (not (ord(l[0]) - 102)) * a * int(l[-2])
    a += (ord(l[0]) - 102 < 0) * int(l[-2]) - ((ord(l[0]) - 102) > 0) * int(l[-2])

print("Part 1: " + str(x*y))
print("Part 2: " + str(x * d))