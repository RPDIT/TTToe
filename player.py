class Player (): 
   
    def __init__( self, marker): 
        self.marker = marker
   
    def placeMarker(self, cords, board): # takes x,y values as a list of ints as cords
        board[cords[0]][cords[1]] = self.marker
        return self.checkWin(board)

    def showBoard(self, displayBoard):
        print(f" {displayBoard[2][0]}  |  {displayBoard[2][1]}  |  {displayBoard[2][2]} ")
        print(f" {displayBoard[1][0]}  |  {displayBoard[1][1]}  |  {displayBoard[1][2]} ")
        print(f" {displayBoard[0][0]}  |  {displayBoard[0][1]}  |  {displayBoard[0][2]} ")
    
    def checkPosition(self, cords, board):
        if board[cords[0]][cords[1]] != "":
            print("That position is taken")
            return False
        else: 
            return True  

    def getInput(self):
        while True:
            cords = input(f" Player {self.marker}: Enter the x,y values ")
            cordStr = str(cords)
            try: 
                cordArray = cordStr.split(" , ")
                cords = [int(d) for d in cordArray[0].split(',')]
                return cords
            except:
                print("Please re-enter your input with only an X and Y value separated by a comma within the ranges 0-2. IE: 0,1 0,0 2,2")
                continue
    
    def checkWin(self, boardInput):
        matrix = self.genMatrix(boardInput)
        for m in matrix:
            status = m.count(self.marker) == 3
            if (status == True):
                return 1
        return 0

    def genMatrix(self, inputBoard):
        return [
            inputBoard[0],
            inputBoard[1],
            inputBoard[2],
            [inputBoard[0][0], inputBoard[1][0], inputBoard[2][0]], 
            [inputBoard[0][1], inputBoard[1][1], inputBoard[2][1]],
            [inputBoard[0][2], inputBoard[1][2], inputBoard[2][2]],
            [inputBoard[0][0], inputBoard[1][1], inputBoard[2][2]],
            [inputBoard[0][2], inputBoard[1][1], inputBoard[2][0]] 
        ]
    def validateInput(self, move):
        for x in move: 
            if x > 2:
                print("Your input is larger than the 0-2 range of the board")
                return False
            if 0 > x: 
                print("Your input must be positive")
                return False
        return True

    def takeTurn(self, inputBoard, turnCounter):
        while True:
            move1 = self.getInput()
            if self.validateInput(move1):
                if self.checkPosition(move1, inputBoard):
                    play = self.placeMarker(move1, inputBoard)
                    break
        self.showBoard(inputBoard)
        if (play == True):
            return 1
        turnCounter = turnCounter * -1
        return 0
