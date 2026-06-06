Rock Paper Scissors (Python)

A simple command-line implementation of the classic Rock Paper Scissors game built with Python.

This project was created as a beginner programming exercise to practice core Python concepts such as functions, loops, conditionals, user input, and random number generation.

Features
	•	Play Rock, Paper, Scissors against the computer
	•	Random computer move generation
	•	Win/Loss/Tie tracking
	•	Input validation
	•	Quit at any time with q
	•	Displays final statistics when the game ends

How It Works
The computer randomly selects one of:
	•	Rock (r)
	•	Paper (p)
	•	Scissors (s)
The player enters a move, and the game determines the winner according to the standard rules:
	•	Rock beats Scissors
	•	Scissors beat Paper
	•	Paper beats Rock
Scores are updated after each round and displayed throughout the game.

Requirements
	•	Python 3.x

Running the Game
Clone the repository:
git clone <repository-url>
Navigate into the project folder:
cd rock-paper-scissors-python

Run the game:
python rock_paper_scissors.py

Example Gameplay
--------------------------------------------------
ROCK PAPER SCISSORS
--------------------------------------------------

Wins = 0, Losses = 0, Ties = 0

Enter your move (r = rock, p = paper, s = scissors, q = quit): r

ROCK vs SCISSORS!
You win.

Skills Demonstrated
	•	Python functions
	•	While loops
	•	Conditional statements
	•	User input handling
	•	Random number generation
	•	Basic game development

Future Improvements
	•	Best-of-3 mode
	•	Best-of-5 mode
	•	Save game statistics to a file
	•	Graphical user interface (Tkinter)
	•	Multiplayer mode
	•	Rock-Paper-Scissors-Lizard-Spock variation

Created as a Python learning project — inspired by Rock Paper Scissors example from the book Automate the Boring Stuff with Python by Al Sweigart.
# Rock Paper Scissors — Refactored

A command-line Rock Paper Scissors game built in Python.

## What I changed
The original was a single script with all logic, display, and 
state mixed together. Refactored into three modules:

- `game.py` — move logic and result calculation
- `display.py` — all terminal output
- `main.py` — game loop and entry point

## How to run
python3 main.py

## What I learned
- Modular code structure and separation of concerns
- Git workflow and meaningful commit messages
- Importing between modules

