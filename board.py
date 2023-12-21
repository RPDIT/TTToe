from player import Player

class Engine:
    def __init__(self):
        self.board = [["","",""],["","",""],["","",""]]
        self.turn = 1
        self.won = 0
        self.getInput()
    
    def getInput(self):
        while True:
            self.marker_selection = input("Input the single character you would like to use as a marker. ")
            if len(self.marker_selection) == 1:
                break
            else: 
                print("Marker Is too long.")
                continue
                
        self.player1 =  Player(self.marker_selection, "Player 1")
        self.player2 = self.p2Marker()
        self.player1.showBoard(self.board)
        self.gameState()

    def p2Marker(self):
        if (self.marker_selection != "O"):
            player2 = Player("O", "Player 2")
        else: 
            player2 = Player("X", "Player 2")
        return player2
    
    def handleGameState(self):
        if self.won == 1: 
            print(f"{self.current_player.name} has Won!")
            return
        elif self.won == 2: 
            print(f"It's a stalemate, nobody wins.")
            return
    
    def gameState(self):
        self.current_player = self.whichPlayer()
        self.won = self.current_player.takeTurn(self.board)
        self.turn = self.turn * -1
        
    def whichPlayer(self):
        if self.turn == 1: 
            return self.player1
        else: 
            return self.player2

if __name__ == '__main__':
    main = Engine()
    while main.won == 0: 
        main.gameState()
        continue
    main.handleGameState()
    





    

