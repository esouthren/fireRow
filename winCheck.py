

def winCheck(board, height, width, row, col, player):


    def checkH():

        # Check Horizontal
        for h in range(0,width - 3):
            testSet = [board[row][h],board[row][h + 1],board[row][h + 2],board[row][h + 3]]
            if testSet == set:
                return True
                break
    # Check Vertical
    def checkV():
        for v in range(0, height - 3):
            testSet = [board[v][col], board[v + 1][col], board[v + 2][col], board[v + 3][col]]
            if testSet == set:
                return True
                break


    # Check diagonal: / by testing all sets of 4 in the most recently placed counters' diagonal

    def checkD1():
        # Where does the north-east diagonal row begin?
        baseRow = row
        baseCol = col
        # find left-base
        while baseCol > 0 and baseRow < height - 1:
            baseCol -= 1
            baseRow += 1

        # get full diagonal array
        diagNorthEast = []
        while baseCol < width and baseRow > 0:
            newEl = board[baseRow][baseCol]

            diagNorthEast.append(newEl)
            baseCol += 1
            baseRow -= 1
        # iterate through diagonal in sets of 4

        if len(diagNorthEast) > 3:
            for x in range(0, len(diagNorthEast) - 3):
                testSet = [diagNorthEast[x], diagNorthEast[x + 1], diagNorthEast[x + 2], diagNorthEast[x + 3]]
                if testSet == set:
                    return True
                    break

    def checkD2():
        baseRow2 = row
        baseCol2 = col
        # find right-base of diagonal
        while baseCol2 < width-1 and baseRow2 < height-1:
            baseCol2 += 1
            baseRow2 += 1

        # get full diagonal array
        diagNorthWest = []
        while baseCol2 < width and baseRow2 > 0:
            newEl = board[baseRow2][baseCol2]

            diagNorthWest.append(newEl)
            baseCol2 -= 1
            baseRow2 -= 1
        # iterate through diagonal in sets of 4

        if len(diagNorthWest) > 3:
            for x in range(0, len(diagNorthWest) - 3):
                testSet = [diagNorthWest[x], diagNorthWest[x + 1], diagNorthWest[x + 2], diagNorthWest[x + 3]]
                if testSet == set:
                    return True
                    break


    set = [player, player, player, player]

    if checkH() or checkV() or checkD1() or checkD2():
        return True
    else:
        return False

