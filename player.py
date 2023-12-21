class Player (): 
   
    def __init__( self, marker, name): 
        self.marker = marker
        self.display_board = [["","",""],["","",""],["","",""]]
        self.name = name
    
    def takeTurn(self, inputBoard, move1): # returns 0 or 1 value to check if the current player has won
        if self.checkPosition(move1, inputBoard):
            return self.placeMarker(move1, inputBoard) 
        else:
            return 0

    def checkPosition(self, cords, board):
        if board[cords[0]][cords[1]] != "":
            print("That position is taken")
            return False
        else: 
            return True  
   
    def placeMarker(self, cords, board): # takes x,y values as a list of ints as cords
        board[cords[0]][cords[1]] = self.marker
        self.board = board
        return self.checkWin(board)
    
    def checkWin(self, boardInput):
        matrix = self.genMatrix(boardInput)
        for m in matrix:
            status = m.count(self.marker) == 3
            if (status == True):
                return 1
        if self.checkStalemate(boardInput):
            return 2
        else:
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
    
    def checkStalemate(self, boardInput):
        for row in boardInput:
            for entry in row:
                if entry == "":
                    return False
        return True



