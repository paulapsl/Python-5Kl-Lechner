import random
from enum import IntEnum


# create enum containing all possible actions
class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Spock = 3
    Lizard = 4


# define victories
victories = {
    Action.Scissors: [Action.Lizard, Action.Paper],
    Action.Paper: [Action.Spock, Action.Rock],
    Action.Rock: [Action.Lizard, Action.Scissors],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
}


# let computer select a random Action - TODO: make the selection based on earlier choices
def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    print(f"Computer chose: ", action)
    return action


# get input from user
def get_user_selection():
    # display possible choices
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    # get user input
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action


def determine_winner(user_action, computer_action):
    # define defeats - consists of defined victories from specified user input
    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif computer_action in defeats:
        # if computer chose something in the user's selected action victories dict, user wins
        print(f"{user_action.name} beats {computer_action.name}! You win!")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")


if __name__ == "__main__":
    while True:
        try:
            user_action = get_user_selection()
        except ValueError as e:
            # if an impossible actions get chosen, let the user know
            range_str = f"[0, {len(Action) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue
        # let computer pick choice
        computer_action = get_computer_selection()
        determine_winner(user_action, computer_action)

        play_again = input("Play again? (y/n): ")
        # .lower because we also accept Y aswell as y
        if play_again.lower() != "y":
            break  # ends while True
