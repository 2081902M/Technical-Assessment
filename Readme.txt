Solution to SIMUL8 Technical Assessment

The solution is written in Python 2.7 and can be started by running the start.bat file from the same directory as battleships.py.
Python is required to run the solution.

### Build a board

Each board is represented by a nested list, containing 10 lists of 10 elements, with each element representing a square on
the board. The lists are generated and marked using the build_board function, which initialises a list containg only 0s before
prompting the user to enter 17 positions on the grid to mark. 0 is used to represent empty squares and the positions chosen by
the user are converted to 1s to represent that they are full. In the main body of the program, the primary boards for the
players are represented by the variables primary1 and primary2.

### Tracking board

Each of the tracking boards is represented by a nested list in the same manner as the primary boards. The lists are initialised
using the build_tracking function, which initialises a list of 2s, which are used to represent the unknown state. In the main
body of the program the tracking boards are represented by tracking1 and tracking2. The fire function is used to prompt the user
to enter a position on their tracking grid. That position in the tracking list is updated to match the corresponding position in
their opponents primary list. Both lists are taken in to the function as parameters. "Hit!" or "Miss!" is then printed to
indicate to the user whether they selected a full or empty square. In the main body, the fire function is called twice in the 
main loop, so that each player may take turns to select positions.

### Validate layout

The primary boards are validated using the validate function, which takes a nested list as a parameter. As the build_board
function ensures that the user marks 17 different squares it does not need to check this again and it is not possible for the
ships to overlap. The ships can only be aligned horizontally or vertically, so the function finds the index of each of the 1s
in the nested list and checks that they are horizontally or vertically adjacent to another 1. This prevents ships that are
aligned vertically from being entered, along with ships of length 1. In the main body, the function is applied to primary1 and
primary2 after they have been created using build_board.

### Determine winner

The main body of the program checks whether or not a player has won the game by running the win function at the end of their
turn. The function counts the number of 1s in that player's tracking board. If there are 17, they have hit all of their opponents
squares and have won. The function then prints a message announcing the winner and returns True. If not, it returns False. If the
function returned True, the loop ends and the program reaches the end of its execution, otherwise the game continues.
