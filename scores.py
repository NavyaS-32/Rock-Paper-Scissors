import json
from pathlib import Path
scores_file = Path("scores.json")

def load_scores():
    if not scores_file.exists():
        return {"wins": 0, "losses": 0, "ties": 0}
    try:
        with open(scores_file, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, KeyError):
        return {"wins": 0, "losses": 0, "ties": 0}
    
def save_scores(wins,losses,ties):
    new_score= {"wins":wins, "losses":losses, "ties":ties}
    with open(scores_file, "w") as f:
        json.dump(new_score,f)

def reset_scores():
    if SCORES_FILE.exists():
        SCORES_FILE.unlink()
    print("Scores reset.")

