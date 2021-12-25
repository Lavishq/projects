"""
rock paper scissor game
play 10 times and gives result with wins, draws and loses
also it does not count wrong inputs
"""
import random
elements = ["rock", "paper", "scissor"]
your_score = 0
cpu_score = 0
draw_g = 0
total_games = 0
game_limit = 10
def ri():
    r = random.choice(elements)
    return r

def lost():
    print("You lost this round")

def won():
    print("You won this round")

def draw():
    print("This round was draw")
    
def cpu_choice():
    print(f"cpu choose {cpu}")

while total_games < game_limit:
    print("")
    choice = input("choose r, p, s as rock, paper, scissor:").lower()
    cpu=ri()

    if choice == 'r':
        if elements[1]==cpu:
            lost()
            cpu_choice()
            your_score += 1
        elif elements[0]==cpu:
            draw()
            cpu_choice()
            draw_g += 1
        else:
            won()
            cpu_choice()
            cpu_score +=1

    elif choice == 'p':
        if elements[2]==cpu:
            lost()
            cpu_choice()
            your_score += 1
        elif elements[1]==cpu:
            draw()
            cpu_choice()
            draw_g += 1
        else:
            won()
            cpu_choice()
            cpu_score +=1
            
    elif choice == 's':
        if elements[0]==cpu:
            lost()
            cpu_choice()
            your_score += 1
        elif elements[1]==cpu:
            won()
            cpu_choice()
            cpu_score +=1
        else:
            draw()
            cpu_choice()
            draw_g += 1
    
    else:
        print('Wrong input')
        continue
    total_games += 1

if total_games == game_limit:
    print()
    print(f"You won {your_score} times and lost {cpu_score} times and the game was draw {draw_g} times")
