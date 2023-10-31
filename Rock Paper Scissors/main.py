from figures import Figures, string_to_figure
from random import randint

choice_number = randint(1, 3)
npc_choice = Figures(choice_number)
user_choice = string_to_figure(input("Do you want rock, paper or scissors?\n"))

if (user_choice == None) :
    print("Invalid input, please restart!")
    exit(-1)

print("The computer chose: " + npc_choice.name)

if (npc_choice == user_choice): 
    print("TIE")
elif user_choice == Figures.ROCK and npc_choice == Figures.SCISSORS:
    print("WIN")
elif user_choice == Figures.PAPER and npc_choice == Figures.ROCK:
    print("WIN")
elif user_choice == Figures.SCISSORS and npc_choice == Figures.PAPER:
    print("WIN")
else:
    print('you loose, the computer wins')