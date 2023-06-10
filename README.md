# Nim_game
 Nim is a mathematical game of strategy in which two players take turns removing (or "nimming") objects from distinct heaps or piles. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap or pile.Depending on the version being played, the goal of the game is either to avoid taking the last object or to take the last object.

 In this repository you can find a python code for playing a game in terminal. 

There are 2 playmodes: PvP and PvC. 

In order to understand how logic of the bot(computer) in PvC works, I would recommend to check out my other repository with 21-matchsticks game and wiki page of Nim-Game.

The code consists of several functions:

<h2>Main Function</h2>
This function controls the flow of the game for different playmodes. The current condittion of the game is controled by the global list variable 'board_state' It can be optimised. 

```

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


```

<h2>Print board function</h2>
This one is used to display the current condition of the game by looping through the board_state. 

```
def print_board():
    print('Current board state looks like the following')
    global board_state
    for n,i in enumerate(board_state):
        print(f'Pile {n+1} has {i} matches: '+"|"*i)
```

<h2>Removing matches function</h2>
This function receives a pair of two integer values to change the global_state variable.

```
def removing_matches(state, pair):
    state[int(pair[0])-1] -= int(pair[1])
    if state[int(pair[0])-1] <= 0:
        state.pop(int(pair[0])-1)
    global board_state
    board_state = state
```

<h2>Player turn function</h2>
This funciton is used to get the proper input from the user/player. it controls whether inputt makes sense in the current condition of the board and uses remove matches function to change it.

```
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
```

<h2>Bot turn function</h2>

This is the main function for those who found this repo trying to solve the problem in codewars. here is a logic for making correct move to get the board to the nim state. Bot cannot lose when taking matches second, as computer finds a combination that returns board_state to a nim state. more on what is nim state in wiki.

```
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

```