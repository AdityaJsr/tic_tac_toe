import itertools

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    #Horizonatal winner
    for row in game:
        print (row)
        if all_same(row):
            print(f"Player {row[0]} is the winner Horizontally (-)!!")
            return True

    # Diagonal winner
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the Winner Diagonally (/)!!")
        return True

    diags = []
    for inx in range(len(game)):
        diags.append(game[inx][inx])
    if all_same(diags):
        print(f"Player {diags[0]} is the Winner Diagonally (\)!!")
        return True

    # Vertical winner
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is the Winner Vertically(|)!!")
            return True
    return False

def game_board(game_map, player=0, row=0, coloumn=0, just_display= False):
    try:
        if game_map[row][coloumn] != 0:
            print("This spot is taken!! Choose another")
            return game_map, False
        print ("   "+"  ".join([str(i) for i in range (len(game_map))]))
        if not just_display:
            game_map[row] [coloumn] = player
        for count, row in enumerate (game_map):
            print(count,row)
        return game_map, True


    except IndexError as e:
        print("Error: Enter the Row/Column between 0-2", e)
        return game_map, False
    except Exception as e:
        print("things are not looking good for you", e)
        return game_map, False
play = True
player = [1,2]
while play:
    game_size = int(input("What should be the size of the game???"))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won =  False
    game, _ = game_board(game, just_display= True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        played = False
        while not played:
            coloumn_choice = int(input("What Coloumn do you want to play?(0,1,2): "))
            row_choice = int(input("What Row do you want to play?(0,1,2): "))
            game, played = game_board(game, current_player, row_choice, coloumn_choice)

            if win(game):
                game_won = True
                again = input("Game Over , Would you like to play again: (y,n)")
                if again.lower() == "y":
                    print("Restarting....")
                elif agin.lower() == "n":
                    print("Thank you for playing the game..")
                    play = False
                else:
                    print("ERROR: Not a valid input")
                    play = False

