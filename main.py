from termcolor import colored
import random
import json
from json import JSONDecodeError

rounds = 5
won = False

def load_words():
    try:
        with open("words.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("words.json not found!")
        return []
    except JSONDecodeError:
        print("words.json is empty!")
        return []

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

data = load_words()
if not data:
    print("No words available.")
    quit()
    
language = choose_language()
length = choose_length()
words = []

words = data.get(language, {}).get(length, [])

if not words:
    print("No words available.")
    quit()

answer = random.choice(words)

def get_input():
    guess = input("enter your guess: ").strip().lower()
    while len(guess) != len(answer):
        print(f"the word must have {len(answer)} letters!")
        guess = input("try again: ").strip().lower()
    return guess

def check_guess(guess: str, answer: str):
    result = [0] * len(answer)
    answer_chars = list(answer)

    for i in range(len(answer)):
        if guess[i] == answer[i]:
            result[i] = 1
            answer_chars[i] = None

    for i in range(len(answer)):
        if result[i] == 0 and guess[i] in answer_chars:
            result[i] = 2
            answer_chars[answer_chars.index(guess[i])] = None

    return result

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
        
while(rounds != 0): 
    guess = get_input()
    result = check_guess(guess, answer)   
    show_result(guess, result)
    rounds-=1
    print("\n")
    if guess == answer:
        won = True
        break
    
show_end(won, answer)