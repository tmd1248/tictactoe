#Tic Tac Toe - Tyler Day


def gameSetup():
    gameSpace = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return gameSpace

def main():
    thisGameBoard = gameSetup()
    for column in thisGameBoard: (print(column))
    turnCounter = 0
    previousMoves = []
    while turnCounter < 9:
        turnCounter = turnCounter + 1 
        if turnCounter % 2 == 1:
            currentMove = int(input("player X's move "))
            if currentMove > 9 or currentMove < 1:
                currentMove = int(input("Pick a number between 1 and 9 "))
            for move in previousMoves:
                if currentMove == move:
                    while currentMove == move: 
                        currentMove = int(input("Pick a spot that has not been taken "))
            previousMoves.append(currentMove)
            for i in range(3):
                 for n in range(3):
                     if i == 0:
                        if currentMove - 1 == (i + n):
                            thisGameBoard[i][n] = 'x'
                     else:
                         if i == 1:
                             if currentMove - 1 == (3 * i + n):
                                 thisGameBoard[i][n] = 'x'
                         else:
                             if currentMove - 1 == (3 * i + n):
                                 thisGameBoard[i][n] = 'x'  
            for column in thisGameBoard: (print(column))    
        else:
            currentMove = int(input("player O's move "))
            if currentMove > 9 or currentMove < 1:
                currentMove = int(input("Pick a number between 1 and 9 "))
            for move in previousMoves:
                if currentMove == move:
                    while currentMove == move:
                        currentMove = int(input("Pick a spot that has not been taken "))
            previousMoves.append(currentMove)
            for i in range(3):
                 for n in range(3):
                     if i == 0:
                        if currentMove - 1 == (i + n):
                            thisGameBoard[i][n] = 'o'
                     else:
                         if i == 1:
                             if currentMove - 1 == (3 * i + n):
                                 thisGameBoard[i][n] = 'o'
                         else:
                             if currentMove - 1 == (3 * i + n):
                                 thisGameBoard[i][n] = 'o'  
            for column in thisGameBoard: (print(column))
        firstColumnOPoint = 0
        firstColumnXPoint = 0
        secondColumnOPoint = 0
        secondColumnXPoint = 0
        thirdColumnOPoint = 0
        thirdColumnXPoint = 0
        firstRowOPoint = 0
        firstRowXPoint = 0
        secondRowOPoint = 0
        secondRowXPoint = 0
        thirdRowOPoint = 0
        thirdRowXPoint = 0
        firstDiagonalXPoint = 0
        firstDiagonalOPoint = 0
        secondDiagonalXPoint = 0
        secondDiagonalOPoint = 0
        xWin = False
        oWin = False
        evili = 2
        eviln = 0
        n = 0
        for i in range(3):
                if thisGameBoard[0][n] == 'x':
                    firstColumnXPoint = firstColumnXPoint + 1
                else: 
                    if thisGameBoard[0][n] == 'o':
                        firstColumnOPoint = firstColumnOPoint + 1
                if firstColumnXPoint == 3: 
                    xWin = True
                else: 
                    if firstColumnOPoint == 3:
                        oWin = True
                if thisGameBoard[1][n] == 'x':
                    secondColumnXPoint = secondColumnXPoint + 1
                else: 
                    if thisGameBoard[1][n] == 'o':
                        secondColumnOPoint = secondColumnOPoint + 1
                if secondColumnXPoint == 3: 
                    xWin = True
                else: 
                    if secondColumnOPoint == 3:
                        oWin = True
                if thisGameBoard[2][n] == 'x':
                    thirdColumnXPoint = thirdColumnXPoint + 1
                else: 
                    if thisGameBoard[2][n] == 'o':
                        thirdColumnOPoint = thirdColumnOPoint + 1
                if thirdColumnXPoint == 3: 
                    xWin = True
                else: 
                    if thirdColumnOPoint == 3:
                        oWin = True
                if thisGameBoard[i][0] == 'x':
                    firstRowXPoint = firstRowXPoint + 1
                else: 
                    if thisGameBoard[i][0] == 'o':
                        firstRowOPoint = firstRowOPoint + 1
                if firstRowXPoint == 3: 
                    xWin = True
                else: 
                    if firstRowOPoint == 3:
                        oWin = True
                if thisGameBoard[i][1] == 'x':
                    secondRowXPoint = secondRowXPoint + 1
                else: 
                    if thisGameBoard[i][1] == 'o':
                        secondRowOPoint = secondRowOPoint + 1
                if secondRowXPoint == 3: 
                    xWin = True
                else: 
                    if secondRowOPoint == 3:
                        oWin = True
                if thisGameBoard[i][2] == 'x':
                    thirdRowXPoint = thirdRowXPoint + 1
                else: 
                    if thisGameBoard[i][2] == 'o':
                        thirdRowOPoint = thirdRowOPoint + 1
                if thirdRowXPoint == 3: 
                    xWin = True
                else: 
                    if thirdRowOPoint == 3:
                        oWin = True
                if thisGameBoard[i][i] == 'x':
                    firstDiagonalXPoint = firstDiagonalXPoint + 1
                else: 
                    if thisGameBoard[i][i] == 'o':
                        firstDiagonalOPoint = firstDiagonalOPoint + 1
                if firstDiagonalXPoint == 3: 
                    xWin = True
                else: 
                    if firstDiagonalOPoint == 3:
                        oWin = True
                n = n + 1
        while evili > -1:
                if thisGameBoard[evili][eviln] == 'x':
                    secondDiagonalXPoint = secondDiagonalXPoint + 1
                else: 
                    if thisGameBoard[evili][eviln] == 'o':
                        secondDiagonalOPoint = secondDiagonalOPoint + 1
                if secondDiagonalXPoint == 3: 
                    xWin = True
                else: 
                    if secondDiagonalOPoint == 3:
                        oWin = True
                eviln = eviln + 1
                evili = evili - 1
        if xWin == True:
            print("Player X wins!")
            break
        else: 
            if oWin == True:
                print("Player O Wins")
                break


    
main()
