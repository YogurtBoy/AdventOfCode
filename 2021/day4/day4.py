# f = open("boards_small.txt", "r")
f = open("boards.txt", "r")
if f:
    print("Successfully opened data...")

def checkForBingo(board: list, jj: int):
    if board[jj - (jj%5)] < 0 and board[jj - (jj%5) + 1] < 0 and board[jj - (jj%5) + 2] < 0 and board[jj - (jj%5) + 3] < 0 and board[jj - (jj%5) + 4] < 0:
        return True, ii
    elif board[jj] < 0 and board[(jj + 5)%25] < 0 and board[(jj + 10)%25] < 0 and board[(jj + 15)%25] < 0 and board[(jj + 20)%25] < 0:
            return True, ii
    else:
        return False, 0 
                
def makeDraws(boards: list):
    ind = 0
    for draw in draws:
        print("\nNext number is " + str(draw) + "!")
        for ii, board in enumerate(boards):
            for jj, space in enumerate(board):
                if space == draw:
                    boards[ii][jj] = -1
                    print(board)
                    bingo, ind = checkForBingo(board, jj)
                    if bingo:
                        return board, draw

def makeDrawsLoser(boards:list):
    ind = 0
    bingo = False
    numBoards = len(boards)
    wins = [0]*numBoards
    for draw in draws:
        print("\nNext number is " + str(draw) + "!")
        for ii, board in enumerate(boards):
            for jj, space in enumerate(board):
                if space == draw:
                    boards[ii][jj] = -1
                    print(board)
                    bingo, ind = checkForBingo(board, jj)
                    if bingo:
                        wins[ii] = 1
                        if sum(wins) == numBoards:
                            return boards[ii], draw

def scoreBoard(board: list, finalDraw: int):
    score = 0
    for space in board:
        if space > -1:
            score += space
    score *= finalDraw
    return score

boardLine = []
boards = []
numBoards = 0
draws = []
for line in f:
    if len(line) > 20: # Random number draws
        for ii in line.split(','):
            draws.append(int(ii))
    elif len(line) < 5: # lines between boards
        boards.append([])
        numBoards += 1
    else:
        boardLine = line.split()
        for ii in range(len(boardLine)):
            boards[numBoards - 1].append(int(boardLine[ii]))

winningBoard, finalDraw = makeDraws(boards)
score = scoreBoard(winningBoard, finalDraw)
print(score)

losingBoard, finalDraw = makeDrawsLoser(boards)
losingScore = scoreBoard(losingBoard, finalDraw)
print(losingScore)