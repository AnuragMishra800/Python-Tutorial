 
# Welcome To My Rock Paprt And Scissors Game

import random

def get_random_choice():
    choices = ['R', 'P', 'S']
    return random.choice(choices)

def main():
    user = input("Enter your choice (R for Rock, P for Paper, or S for Scissor): ").upper()
    print(f"You Chooses {user}, and")

    if user not in ['R', 'P', 'S']:
        print("Invalid Input. Please Choose From 'R', 'P', 'S'")

    pc_choice = get_random_choice()
    print(f"Pc Choice is {pc_choice}, so \nThe Result is :")  

    if(user == pc_choice):
        print("Match Draw")
    elif(user == 'R' and pc_choice == 'S') or \
        (user == 'P' and pc_choice == 'R') or \
        (user == 'S' and pc_choice == 'P'):
        print("Congratulations! You Win The Game.")
    else:
        print("Sorry! You Loss, Pc Wins.") 

main() 