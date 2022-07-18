import random

signs = ['rock','paper','scissor']
def get_computer_choice(choices):
    return(random.choice(choices))

def get_user_choice(choices):
    choice = input("Choose: rock, paper or scissor")
    if choice not in choices:
        print('Make valid choice')
        choice = get_user_choice(choices)
    return(choice)

def get_winner(computer_choice, user_choice):
    if (computer_choice == 'rock' and user_choice =='scissor') or (computer_choice == 'scissor' and user_choice == 'paper') or (computer_choice == 'paper' and user_choice == 'rock'):
        return ('computer')
    elif (computer_choice == 'rock' and user_choice =='paper') or (computer_choice == 'paper' and user_choice == 'scissor') or (computer_choice == 'scissor' and user_choice == 'rock') :
        return('user')
    else:
        return('noone')

def play():
    computer_choice = get_computer_choice(signs)
    user_choice = get_user_choice(signs)
    winner = get_winner(computer_choice, user_choice)
    print('Computer played ' + computer_choice)
    print('User played ' + user_choice)
    return('Winner is ' + winner)

print(play())