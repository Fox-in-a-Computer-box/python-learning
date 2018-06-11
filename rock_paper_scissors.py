#test rock paper scissors

import random

win_map = {'rock':'scissors','paper':'rock','scissors':'paper'}
player_choice = None

comp_choices = ['rock','paper','scissors']
comp_choice = random.choice(comp_choices)

player_inp = input('Rock, Paper, or Scissors?')
player_inp = player_inp.lower()

if player_inp == 'rock' or player_inp == 'r':
    player_choice = 'rock'
elif player_inp == 'paper' or player_inp == 'p':
    player_choice = 'paper'
elif player_inp == 'scissors' or player_inp == 's':
    player_choice = 'scissors'
else:
    print('please put in an appropriate choice')

if comp_choice == player_choice:
    print('You tied! you both picked: ',player_choice)
elif win_map[comp_choice] == player_choice:
    print('You lost! they picked: ',comp_choice)
elif win_map[player_choice] == comp_choice:
    print('You won! they picked: ',comp_choice)
else:
    print('something broke')
