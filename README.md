## Python TTToe GUI

Two player game of Tic Tac Toe created in Python utilizing a dynamic tkinter GUI.

The game board is a Tkinter Frame with three columns configured, three buttons are then created and inserted into each column before being packed into the root and rendered onto the screen. These buttons have a command property that references the player object to take each players turn, placing a marker and checking for wins/stalemates.

# Thoughts

The game logic was a process of problem-solving that I feel I gained a lot from on day 1, and I had a functioning game by the end of it. Day 2, however, was spent refining the game and working on input validation, trying to ensure that an incorrect input would not cause the entire application to crash and would instead prompt the user to input the correct value with a suggestion to point them in the right direction.
-- 12/15/2023

The development of this GUI led me to directly face many of the flaws in the design of the code behind my original game. Running into issues storing the values in a way that could communicate with the GUI. This led my design away from the main() function while loop I initially used to exclusively handling the game logic/state within the came GUI class and its "mainloop()".
--12/21/2023
