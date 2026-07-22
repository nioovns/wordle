from termcolor import colored
import random
from game import WordleGame
from utils import load_words

def choose_language():
    print("1. english")
    print("2. persian")

    choice = input("> ")

    if choice == "1":
        return "english"
    elif choice == "2":
        return "persian"
    else:
        print("Invalid choice!")
        return choose_language()

def choose_length():
    length = input("Choose word length (3-6): ")

    while length not in ["3", "4", "5", "6"]:
        print("Choose between 3 and 6")
        length = input("Choose word length: ")

    return length

def get_input(answer):
    guess = input("enter your guess: ").strip().lower()
    while len(guess) != len(answer):
        print(f"the word must have {len(answer)} letters!")
        guess = input("try again: ").strip().lower()
    return guess

def show_result(guess: str, result):
    for i in range(len(guess)):
        if result[i] == 1:
            print(colored(guess[i], "green"), end="")
        elif result[i] == 2:
            print(colored(guess[i], "yellow"), end="")
        else:
            print(colored(guess[i], "red"), end="") 
             
def show_end(won: bool, answer: str):
    if won:
        print(colored("YOU WON!!!", "green"))
    else:
        print(colored(f"YOU LOSE!!! Answer was '{answer}'", "red"))
        


data = load_words()
if not data:
    print("No words available.")
    quit()
    
language = choose_language()
length = choose_length()
words = data.get(language, {}).get(length, [])

if not words:
    print("No words available.")
    quit()

answer = random.choice(words)

game = WordleGame(answer)


while game.rounds > 0:
    print(f"you have {game.rounds} guesses left.")
    guess = get_input(answer)

    result = game.check_guess(guess)
    show_result(guess, result)
    print("\n")
    if game.is_won(guess):
        break
    game.decrease_round()
    
show_end(game.won, answer)