from termcolor import colored
import random


words = ['hello', 'world', 'piano', 'train', 'brave', 'roast',
       'ocean', 'stone', 'plant', 'audio', 'about', 'happy', 'alive']
rounds = 5
won = False
answer = random.choice(words)
WORD_LENGTH = len(answer)

def get_input():
    guess = input("enter your guess: ").strip().lower()
    while len(guess) != WORD_LENGTH:
        print(f"the word must have {WORD_LENGTH} letters!")
        guess = input("try again: ").strip().lower()
    return guess

def check_guess(guess: str, answer: str):
    result = [0] * WORD_LENGTH

    for i in range(WORD_LENGTH):
        if guess[i] == answer[i]:
            result[i] = 1
        elif guess[i] in answer:
            result[i] = 2

    return result
        
while(rounds != 0):
    
    guess = get_input()
    result = check_guess(guess, answer)   
    

    for i in range(WORD_LENGTH):
        if result[i] == 1:
            print(colored(guess[i], "green"), end="")
        elif result[i] == 2:
            print(colored(guess[i], "yellow"), end="")
        else:
            print(colored(guess[i], "red"), end="")
    
    rounds-=1
    print("\n")
    if guess == answer:
        print(colored('YOU won!!!', "green"))
        won = True
        break
    
if not won:
    print(colored(f"YOU LOSE!!! Answer was '{answer}'", "red"))        