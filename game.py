def main():
    print('Welcome to the nim game. Nim is a mathematical game of strategy in which two players take turns removing (or "nimming") \n objects from distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap or pile. the player to take the last match wins.')
    global board_state
    board_state = [1,3,5,7]
    playmode = input('Do you want to play with another \'player\' or play a \'bot\'?:')
    if playmode != 'player' and playmode != 'bot':
        print('inproper input! Lets start all over again.')
        return main()
    elif playmode == 'player':
        turn = 'player1'
        while True:
            player_turn(turn)
            if board_state == []:
                break

            if turn == 'player1':
                turn = 'player2'
            else:
                turn = 'player1'
    elif playmode == 'bot':
        turn = 'player'
        while True:
            if turn == 'player':
                player_turn(turn)
            else:
                bot_turn()

            if board_state == []:
                break

            if turn == 'player':
                turn = 'bot'
            else:
                turn = 'player'
    print(turn, 'Won')

def print_board():
    print('Current board state looks like the following')
    global board_state
    for n,i in enumerate(board_state):
        print(f'Pile {n+1} has {i} matches: '+"|"*i)

def removing_matches(state, pair):
    state[int(pair[0])-1] -= int(pair[1])
    if state[int(pair[0])-1] <= 0:
        state.pop(int(pair[0])-1)
    global board_state
    board_state = state

def player_turn(turn):
    global board_state
    print_board()
    print('It is turn for', turn, 'to take matches.')
    curr_input = input('give me a combination of 2 numbers. first is a line you are taking matches from and the second is number of matches you are taking: ').split()
    if len(curr_input) != 2 or int(curr_input[0]) > len(board_state) or  int(curr_input[1]) < 1:
        print('invalid input, try again please!')
        player_turn(turn)
    else:
        removing_matches(board_state, curr_input)
        print('='*20)


def bot_turn():
    global board_state
    nim=0
    for i in board_state:
        nim=nim^i
    print_board()
    counter=0
    for i in board_state:
        if (nim^i) < i:
            print("Bot took {} matche(s) from Pile {}".format(board_state[counter]-(nim^i),counter+1))
            removing_matches(board_state,[str(counter+1),str(board_state[counter]-(nim^i))])
            print('='*20)
            
            break
        counter=counter+1  

main()