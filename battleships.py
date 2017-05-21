def build_board(player_no):
    # Creates a nested list consisting of 10 lists, each containing 10 0s, 0
    # represents an empty square
    board = [[0,0,0,0,0,0,0,0,0,0] for _ in range(10)]
    print "Place 1 ship of length 5, 1 of length 4, 2 of length 3 and 1 of length 4"
    for i in range(0,17):
        mark = raw_input("Player " + player_no + ", enter a position on the 10x10 board in the format x,y - e.g 4,3: ")
        coords = mark.split(',')
        # If the input does not match the form 4,3 or has already been selected,
        # then the user is prompted to enter a valid position
        while (len(coords) != 2) or (coords[0].isdigit() == False) or (coords[1].isdigit() == False) or (int(coords[0]) < 1) or (int(coords[0]) > 10) or (int(coords[1]) < 1) or (int(coords[1]) > 10) or (board[int(coords[0])-1][int(coords[1])-1] == 1):
            mark = raw_input("Invalid input, enter a different position: ")
            coords = mark.split(',')
        # If the input is valid, that element is set to 1, representing a full square
        board[int(coords[0])-1][int(coords[1])-1] = 1
        print "1 represents a marked square, 0 reprsents an empty square"
        for i in board:
            print i
    return board

def build_tracking():
    # Creates a nested list consisting of 10 lists, each containing 10 2s, 2
    # represents an unknowm square
    board = [[2,2,2,2,2,2,2,2,2,2] for _ in range(10)]
    return board

def fire(player_no, tracking, primary):
    target = raw_input("Player " + player_no + ", enter a position to fire at on your opponent's board: ")
    coords = target.split(',')
    # If the input does not match the form 4,3, then the user is prompted to enter
    # a valid position
    while (len(coords) != 2) or (coords[0].isdigit() == False) or (coords[1].isdigit() == False) or (int(coords[0]) < 1) or (int(coords[0]) > 10) or (int(coords[1]) < 1) or (int(coords[1]) > 10) or (tracking[int(coords[0])-1][int(coords[1])-1] != 2):
        target = raw_input("Invalid input, enter a different position: ")
        coords = target.split(',')
    # The selected position on the player's tracking board is updated to match the
    # corresponding position on their opponent's primary board
    if primary[int(coords[0])-1][int(coords[1])-1] == 1:
        tracking[int(coords[0])-1][int(coords[1])-1] = 1
        print "Hit!"
    else:
        tracking[int(coords[0])-1][int(coords[1])-1] = 0
        print "Miss!"

def validate(primary):
    # For each row of the grid
    for i in range(0,10):
        # Get the indexes of any 1s in that row
        full = [j for j, x in enumerate(primary[i]) if x == 1]
        # For each of the indexes check if it is horizontally or vertically adjacent
        # to any other 1s. As 2 is the smallest battleship size, all 1s must be adjacent
        # to another 1 for them to be valid
        for j in full:
            # Specific conditions were created for corners and squares on the edge of
            # the grid to prevent index out of bounds errors
            if j == 0 and i == 0:
                if (primary[i][j+1] != 1) and (primary[i+1][j] != 1):
                    return False
            elif j == 0 and i == 9:
                if (primary[i][j+1] != 1) and (primary[i-1][j] != 1):
                    return False
            elif j == 9 and i == 0:
                if (primary[i][j-1] != 1) and (primary[i+1][j] != 1):
                    return False
            elif j == 9 and i == 9:
                if (primary[i][j-1] != 1) and (primary[i-1][j] != 1):
                    return False
            elif j == 0:
                if (primary[i][j+1] != 1) and (primary[i-1][j] != 1) and (primary[i+1][j] != 1):
                    return False
            elif j == 9:
                if (primary[i][j-1] != 1) and (primary[i-1][j] != 1) and (primary[i+1][j] != 1):
                    return False
            elif i == 0:
                if (primary[i][j-1] != 1) and (primary[i][j+1] != 1) and (primary[i+1][j] != 1):
                    return False
            elif i == 9:
                if (primary[i][j-1] != 1) and (primary[i][j+1] != 1) and (primary[i-1][j] != 1):
                    return False  
            elif (primary[i][j-1] != 1) and (primary[i][j+1] != 1) and (primary[i-1][j] != 1) and (primary[i+1][j] != 1):
                return False
    return True

def win(player_no, tracking):
    # Count the number of 1s in the player's tracking board
    sum = 0
    for i in tracking:
        sum = sum + i.count(1)
    # If they have found all of their opponent's 1s, return true    
    if sum == 17:
        print "Player " + player_no + " wins!"
        return True
    else:
        return False

# Build and validate the primary boards for both players
primary1 = build_board("1")
while validate(primary1) == False:
    print "Invalid battleship placement, try again"
    primary1 = build_board("1")
primary2 = build_board("2")
while validate(primary1) == False:
    print "Invalid battleship placement, try again"
    primary1 = build_board("2")
# Build the tracking boards for both players    
tracking1 = build_tracking()
tracking2 = build_tracking()
# While neither player has found all of their opponents battleships, each player
# takes turns to guess a position on their opponents board
print "1 represents a hit, 0 represents a miss, 2 represents an unknown square"
while win("2", tracking2) == False:
    print "Player 1's tracking board:"
    for i in tracking1:
        print i
    fire("1",tracking1,primary2)
    if win("1", tracking1) != False:
        break
    else:
        print "Player 2's tracking board:"
        for i in tracking2:
            print i
        fire("2", tracking2, primary1)

