import tkinter as tk
from player import Player
from functools import partial

class Gooey: 
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(0,0)
        self.root.title("Tic Tac Toe")
        
        self.won = 0
        self.turn = 1
        self.display_board = [["","",""],["","",""],["","",""]]
        self.game_board = [["","",""],["","",""],["","",""]]
        self.start = False
        self.marker_input()
        self.root.mainloop()


    def create_gameboard(self):
        self.gameboard = tk.Frame(self.root)
        self.gameboard.columnconfigure(0, weight=1)
        self.gameboard.columnconfigure(1, weight=1)
        self.gameboard.columnconfigure(2, weight=1)

    def create_buttons(self):
        for y in range(2,-1,-1) :
            for x in range(2,-1,-1):
                btn_text = tk.StringVar(value="")
                self.display_board[y][x] = tk.Button(
                    self.gameboard,
                    height=4, width= 8,
                    font=('Cascadia', 18),
                    command=partial(self.button_input, x, y),
                    text=""
                )
                self.display_board[y][x].grid(row=x, column=y)
            
        self.gameboard.pack(fill="x")

    def marker_input(self):
        self.input_frame = tk.Frame(self.root)

        self.marker_selection = tk.Text(
            self.input_frame,
            height=1, width=5,
            font=('Cascadia', 12),   
        )
        self.marker_selection.pack()
        self.marker_selection.insert(tk.INSERT, "Enter")

        self.marker_input_button = tk.Button(self.input_frame, text="Start", command=self.marker_confirm)
        self.input_frame.pack()
        
        self.marker_input_button.pack()

    def marker_confirm(self):
        if self.start == False:
            self.player1 = Player(self.marker_selection.get("1.0", "1.1"), "Player 1")
            self.player2 = Player(self.p2Marker(), "Player 2")
            self.current_player = self.which_player()

            self.create_gameboard()
            self.reset()
            print("created")

        else:
            self.resetBoard()
            self.reset()

        
        
    def button_input(self, x_cord, y_cord):
        self.start =  True
        
        self.current_player = self.which_player()

        move = [int(x_cord), int(y_cord)]
        if self.current_player.checkPosition(move, self.game_board):
            self.won = self.current_player.takeTurn(self.game_board, move)
            self.display_board[y_cord][x_cord].configure(text=self.current_player.marker)
            self.turn = self.turn * -1
        self.handleGameState()


            

    def handleGameState(self):
        if self.won == 0:
            return
        else: 
            if self.won == 1: 
                print(f"{self.current_player.name} has Won!")
                self.alert = tk.Message(self.marker_selection, font=('Cascadia', 18), text=f"{self.current_player.name} has Won!")
                self.alert.grid()
            elif self.won == 2: 
                print(f"It's a stalemate, nobody wins.")
                self.alert = tk.Message(self.marker_selection, font=('Cascadia', 18), text=f"It's a stalemate, nobody wins.")
                self.alert.grid()

    def reset(self):
        self.won = 0
        self.game_board = [["","",""],["","",""],["","",""]]
        self.create_buttons()
        self.turn = 1

        
    def resetBoard(self):
        for y in self.display_board:
            for x in y:
                x.grid_forget()
            self.gameboard.pack_forget()
        self.start = False
        if self.won != 0:
            self.alert.grid_forget()

    def p2Marker(self):
        if self.player1.marker == "O":
            return "X"
        else: 
            return "O"
        
    
     
    def which_player(self):
        self.start = True
        if self.turn == 1: 
            return self.player1
        else: 
            return self.player2
        
        
        

main = Gooey()