from random import choice
moves = ['r', 'p', 's']
move_names = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}

def get_computer_move():
    #Return a random move: r, p, or s
    return choice(moves)

def get_result(player, computer):
    """
    Compare player and computer moves.
    Returns 'win', 'loss', or 'tie'.
    """
    if player == computer:
        return 'tie'
    wins_against = {'r': 's', 'p': 'r', 's': 'p'}
    if wins_against[player] == computer:
        return 'win'
    return 'loss'

def is_valid_move(move):
    """Return True if move is r, p, s, or q."""
    return move in moves + ['q']