#This program is a noughts and crosses game

print ("Welcome to this Noughts and Crosses Game")
print ("")
winner = False
ended = False
# This sets sets the board

board = [' '] * 9

player_turn = 0

#This announces the turns:
def turn_announcer():
    print ("")
    print ("*************************************************")
    print ("")
    if player_turn % 2 == 0:
        print("It is player 1's turn. Player 1 plays with O")
    else:
        print("It is player 2's turn. Player 2 plays with X")
    print ("")

#This function displays the board
def display_board():
    print("The board currently looks like this: ")
    print ("")
    print (board[0],"|", board[1],"|", board[2])
    print ("----------")    
    print (board[3],"|",board[4], "|",board[5])
    print ("----------")
    print (board[6],"|",board[7], "|",board[8])
    print ("")


# This function asks the player where they'd like to play
def question_board():
    print ("")
    print ("Which position would you like to play in? Pick a number between 0 and 8: ")
    print ("")
    print (" 0  |  1  |   2   ")
    print ("-----------------")    
    print (" 3  |  4  |   5   ")
    print ("-----------------")
    print (" 6  |  7  |   8   ")
    print ("")
    global place
    place = input()
    while place not in ['0','1','2','3','4','5','6','7','8']:
        print ("That is not a valid choice.")
        place = input("Which position would you like to play in? Pick a number between 0 and 8: ")
    
    place = int(place)


# This function checks to see if that's a valid move, and records it if it is

def move_checker():
    while board[place] != ' ':
        print ("That's not a valid move: that space is already occupied")
        display_board()
        question_board()
    if player_turn % 2 == 0:
        board[place] = 'O'
    if player_turn % 2 == 1:
        board[place] = 'X'
    
# This function ends the turn and switches the player

def turn_ender():
    if winner == False:
        global player_turn
        if player_turn == 8:
            display_board()
            print ("This game is a draw. The End.")
            global ended
            ended = True
        player_turn += 1
    if winner == True:
        display_board()
        if player_turn % 2 == 0:
            print("O is victorious. Player 1 has won.")
        else:
            print("X is victorious. Player 2 has won.")
        print ("The End.")
        ended = True
        
#This function checks to see if anyone has won

def winner_test():
    global winner
    if board[0] == board[1] == board[2] == 'X':
        winner = True
    elif board[0] == board[1] == board[2] == 'O':
        winner = True
    elif board[3] == board[4] == board[5] == 'X':
        winner = True
    elif board[3] == board[4] == board[5] == 'O':
        winner = True
    elif board[6] == board[7] == board[8] == 'X':
        winner = True
    elif board[6] == board[7] == board[8] == 'O':
        winner = True
    elif board[0] == board[3] == board[6] == 'X':
        winner = True
    elif board[0] == board[3] == board[6] == 'O':
        winner = True
    elif board[1] == board[4] == board[7] == 'X':
        winner = True
    elif board[1] == board[4] == board[7] == 'O':
        winner = True
    elif board[2] == board[5] == board[8] == 'X':
        winner = True
    elif board[2] == board[5] == board[8] == 'O':
        winner = True
    elif board[0] == board[4] == board[8] == 'X':
        winner = True
    elif board[0] == board[4] == board[8] == 'O':
        winner = True
    elif board[2] == board[4] == board[6] == 'X':
        winner = True
    elif board[2] == board[4] == board[6] == 'O':
        winner = True




        
# This part actually operates the game
while ended == False:
    turn_announcer()
    display_board()
    question_board()
    move_checker()
    winner_test()
    turn_ender()
