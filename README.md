# Wordle Terminal Game

A simple Wordle-like game written in Python.

## Features

- Terminal-based gameplay
- Random word selection from JSON
- language selection
- Word lengths from 3 to 6 letters
- Dynamic number of attempts based on word length
- Correct duplicate-letter handling
- Colored feedback
  - Green: correct letter in the correct position
  - Yellow: correct letter in the wrong position
  - Red: letter not found

## Future Improvements

- Guess history
- On-screen keyboard
- Difficulty levels
- Statistics (wins, losses, streak)
- GUI version

## Project Structure

```
wordle/
├── main.py
├── game.py
├── utils.py
├── words.json
├── requirements.txt
└── README.md
```
## How to run

### Requirements

- Python 3.x

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/wordle-terminal.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Start the game

```bash
python main.py
```

Enjoy :>