from termcolor import colored
import random

dic = ['hello', 'world', 'piano', 'train', 'brave', 'roast',
       'ocean', 'stone', 'plant', 'audio', 'about', 'happy', 'alive']
result = [0] * 5
ROUND = 5
WON = False
answer = random.choice(dic)

while(ROUND != 0):
    in1 = input("enter your guess: ").strip().lower()
    while len(in1) != 5:
        print("the word must have 5 letters!")
        in1 = input("try again: ").strip().lower()
       
    for i in range(5):
        if in1[i] == answer[i]:
            result[i] = 1
        elif in1[i] in answer:
            result[i] = 2
        else:
            result[i] = 0

    for i in range(5):
        if result[i] == 1:
            print(colored(in1[i], "green"), end="")
        elif result[i] == 2:
            print(colored(in1[i], "yellow"), end="")
        else:
            print(colored(in1[i], "red"), end="")
    
    ROUND-=1
    print("\n")
    if in1 == answer:
        print(colored('YOU WON!!!', "green"))
        WON = True
        break
    
if not WON:
    print(colored(f"YOU LOSE!!! Answer was '{answer}'", "red"))        