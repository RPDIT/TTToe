## Python TTToe Game

Two player game of Tic Tac Toe that allows player 1 to select their marker as any single character while player 2 uses one of the standard pre-determined markers.

The game board is a list of 3 lists, each nested list has three elements of blank strings.

Each turn, the system takes a comma-separated x,y value, checks that the input is valid, checks that the desination coordinate is empty, and places the marker. It then generates a matrix of the current game board that processes each valid axis of the game board to see if any have 3 of the current player's marker; if not, return to the start of the loop and take the next input.

# Thoughts

The game logic was a process of problem-solving that I feel I gained a lot from on day 1, and I had a functioning game by the end of it. Day 2, however, was spent refining the game and working on input validation, trying to ensure that an incorrect input would not cause the entire application to crash and would instead prompt the user to input the correct value.

```
$ python board.py
Input the single character you would like to use as a marker. Z
  |    |
  |    |
  |    |
Player Z: Enter the x,y values 1,1
  |    |
  | Z |
  |    |
Player O: Enter the x,y values 2,2
  |    | O
  | Z |
  |    |
Player Z: Enter the x,y values 0,2
  |    | O
  | Z |
  |    | Z
Player O: Enter the x,y values 2,1
| O | O
| Z |
| | Z
Player Z: Enter the x,y values 2,0
Z | O | O
| Z |
| | Z
Player 1 wins!
```
