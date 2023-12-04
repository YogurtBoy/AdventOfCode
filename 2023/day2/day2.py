f = open('2023/day2/games.txt', 'r')

print("OPENED!")

colors = ['red', 'blue', 'green']
gameString = 'Game '
for line in f:
    idx = line.find(':')
    gameNum = line[len(gameString):idx]


    for char in line:
        for color in colors:
    colorIdx = line[idx:].find(color)

    print(gameNum)

