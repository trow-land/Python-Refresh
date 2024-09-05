import random


def get_user_choice():
    ''' Function that gets a valid input choice from the user'''

    possible_selections = ['rock', 'paper', 'scissors']

    while True:
        user_choice = input("What is your selection? (rock, paper or scissors?): ").lower()

        # Ensure the choise is valid
        if user_choice not in possible_selections:
            print("Please choose a valid responce (rock, paper, scissors)")
            pass
        else:
            break

    print("Your choice: ", user_choice)

    return user_choice


def get_computer_choice():
    ''' Function that randomly selects a move for the computer'''
    # Selects a random number between one and three representing the computers choice
    computer_choice = random.randint(1,3)

    choice_dict = {
        1 : 'rock',
        2 : 'paper',
        3 : 'scissors'
    }

    print("Computer choice: ", choice_dict[computer_choice])

    computer_selection = choice_dict[computer_choice]

    return computer_selection

def play_game():
    '''Function containing the main game logic for rock paper scissors'''

    if user == computer:
        outcome = 'Draw!'

    # win cases
    elif (user == 'paper' and computer == 'rock') or (user == 'rock' and computer == 'scissors') or ('scissors' and computer == 'paper'):
        outcome = 'You Win!'
    else: # else lose
        outcome = 'You Lose!'

    return outcome


def select_rounds():

    possible_rounds = ['1', '3', '5']

    # ensures correct selection
    while True:
        rounds = input("Would you like to play best of 1, 3 or 5 rounds?    ")
        if rounds in possible_rounds:
            break

    return rounds


rounds = select_rounds()
user_scorecard = 0
computer_scorecard = 0


print("Starting Game.....")

while True:

    user = get_user_choice()
    computer = get_computer_choice()
    outcome = play_game()

    # print game outcome
    print(f"{outcome} You had {user} and your opponent had {computer}")
    

    if outcome == 'You Win!':
        user_scorecard += 1
    elif outcome == 'You Lose!':
        computer_scorecard += 1

    print(f"\nThe current scores are..... you: {user_scorecard}, computer: {computer_scorecard}")


    # max score to win best of x
    max_value =  int(rounds) // 2 + 1

    if user_scorecard >= max_value:
        print(f"You win overall! You had {user_scorecard} points and your opponent had {computer_scorecard} points")
        break
    elif computer_scorecard >= max_value:
        print(f"You lose overall! You had {user_scorecard} points and your opponent had {computer_scorecard} points")
        break






