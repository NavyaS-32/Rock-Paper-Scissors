from game import move_names
def show_header():
    print("-"*50)
    print("ROCK PAPER SCISSORS")
    print("-"*50)

def show_score(wins, losses, ties):
    print("\n Wins:", wins,"| Losses:",losses,"| Ties:",ties)

def show_round(player_move, comp_move, result):
    p_name = move_names[player_move]
    c_name = move_names[comp_move]
    print()
    print(p_name,"vs",c_name)
    if result == 'win':
        print("You WIN.")
    elif result == 'loss':
        print("You LOSE.")
    else:
        print("It's a TIE.")

def show_final(wins, losses, ties):
    print("\nFinal Scores")
    print("\n Wins:", wins,"| Losses:",losses,"| Ties:",ties)
    print("\nThanks for playing :)")

def show_invalid():
    print("Invalid move. Try again :(")
