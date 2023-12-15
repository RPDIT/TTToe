from player import Player

def p2Marker(selected):
    if (selected != "O"):
        player2 = Player("O")
    else: 
        player2 = Player("X")
    return player2

def main(): 
    board = [["","",""],["","",""],["","",""]]
    turn = 1
    won = 0

    while True:
        marker_selection = input("Input the single character you would like to use as a marker. ")
        if len(marker_selection) == 1:
            break
        else: 
            print("Marker Is too long.")
            continue
            
    player1 =  Player(marker_selection)
    player2 = p2Marker(marker_selection)
    player1.showBoard(board)

    while (won == 0):
        status = player1.takeTurn(board, turn)
        if (status == True):
            won = 1
            print("Player 1 wins!")
            break
        status = player2.takeTurn(board, turn)
        if (status == True):
            won = 1
            print("Player 2 wins!")
            break
    return


main()



    

