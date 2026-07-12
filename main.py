from termcolor import colored
import random


words = ['hello', 'world', 'piano', 'train', 'brave', 'roast',
       'ocean', 'stone', 'plant', 'audio', 'about', 'happy', 'alive']
rounds = 5
won = False
answer = random.choice(words)

def get_input():
    guess = input("enter your guess: ").strip().lower()
    while len(guess) != len(answer):
        print(f"the word must have {len(answer)} letters!")
        guess = input("try again: ").strip().lower()
    return guess

def check_guess(guess: str, answer: str):
    result = [0] * len(answer)

    for i in range(len(answer)):
        if guess[i] == answer[i]:
            result[i] = 1
        elif guess[i] in answer:
            result[i] = 2

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