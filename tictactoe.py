#Board
positions = [' ' for _ in range(9)]

def update_board():
    board = f'''
    -------------
    | {positions[0]} | {positions[1]} | {positions[2]} |
    -------------
    | {positions[3]} | {positions[4]} | {positions[5]} |
    -------------
    | {positions[6]} | {positions[7]} | {positions[8]} |
    -------------
    '''
    return board


#Players
player = "X"
def switch():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
        
        
#Checks
def columns():
    for i in range(3):
        if positions[i] == positions[i+3] == positions[i+6]:
            if positions[i] != ' ' and  positions[i+3] != ' ' and positions[i+6] != ' ':
                return True
            else:
                return False
            
def rows():
    for i in range(0, 9, 3):
        if positions[i] == positions[i+1] == positions[i+2]:
            if positions[i] != ' ' and  positions[i+1] != ' ' and positions[i+2] != ' ':
                return True
            else:
                return False
            
def diagonals():
    if positions[2] == positions[4] == positions[6]:
        if positions[2] != ' ' and  positions[4] != ' ' and positions[6] != ' ':
            return True
        else:
            return False
    if positions[0] == positions[4] == positions[8]:
        if positions[0] != ' ' and  positions[4] != ' ' and positions[8] != ' ':
            return True
        else:
            return False


#Game
game_over = False
while not game_over:
    print(update_board())
    positions[(int(input("Pick positions (1-9): "))-1)] = player
    if columns() or rows() or diagonals():
        print(f"{player} wins!")
        print(update_board())
        game_over = True
    elif ' ' not in positions:
        print(f"\nIt's a tie!")
        print(update_board())
        game_over = True
    else:
        switch()