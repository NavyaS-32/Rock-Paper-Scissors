from game import get_computer_move, get_result, is_valid_move
from display import (show_header,show_score, show_round,show_final, show_invalid)
from scores import load_scores, save_scores

def play():
    saved = load_scores()
    wins = saved["wins"]
    losses = saved["losses"]
    ties = saved["ties"]
    show_header()
    try:
        while True:
            show_score(wins, losses, ties)
            move = input("\nYour move (r/p/s or q): ").strip().lower()
            if move == 'q':
                save_scores(wins, losses, ties)
                show_final(wins, losses, ties)
            break

            if not is_valid_move(move):
                show_invalid()
                continue

            comp_move = get_computer_move()
            result = get_result(move, comp_move)
            show_round(move, comp_move, result)

            if result == 'win':
                wins += 1
            elif result == 'loss':
                losses += 1
            else:
                ties += 1
    
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Saving scores...")
        save_scores(wins, losses, ties)

if __name__ == "__main__":
    play()