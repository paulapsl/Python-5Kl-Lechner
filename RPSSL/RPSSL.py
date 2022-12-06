import random
import ast
# https://docs.python.org/3/library/enum.html
from enum import IntEnum

player_wins = 0
comp_wins = 0

dict_stat = {"Rock": 0, "Paper": 0, "Scissors": 0, "Spock": 0, "Lizard": 0}


# create enum containing all possible actions
class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Spock = 3
    Lizard = 4


# define victories - dict
victories = {
    Action.Scissors: [Action.Lizard, Action.Paper],
    Action.Paper: [Action.Spock, Action.Rock],
    Action.Rock: [Action.Lizard, Action.Scissors],
    Action.Lizard: [Action.Spock, Action.Paper],
    Action.Spock: [Action.Scissors, Action.Rock]
}


# let computer select a random Action
# TODO: make the selection based on earlier choices, idea: get max count from .txt
# TODO: and computer has to select from victories from this Action
def get_computer_selection():
    # chooses random value (0-4) defined in enum Action
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    print(f"Computer chose: ", action)
    return action


# get input from user
def get_user_selection():
    # display possible choices
    # value returns value assigned to the action in enum, name returns name of element in enum
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    # get user input
    #  F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    # dict_stat["Action.Lizard"] = dict_stat["Action.Lizard"] + 1
    # print(dict_stat)
    return action


def determine_winner(user_action, computer_action):
    global comp_wins, player_wins
    # define defeats - consists of defined victories from specified user input
    defeats = victories[user_action]
    print("defeats:", defeats)
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif computer_action in defeats:
        # if computer chose something in the user's selected action victories dict, user wins
        print(f"{user_action.name} beats {computer_action.name}! You win!")
        player_wins = player_wins + 1
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")
        comp_wins = comp_wins + 1


def save_data_to_file():
    data = "Spieler gewinnt: " + str(player_wins) + "\nComputer gewinnt: " + str(comp_wins) + "\n" + str(dict_stat)
    with open("statistics/stat.txt", 'w') as stat:
        stat.write(data)
        stat.close()


if __name__ == "__main__":
    while True:
        try:
            user_action = get_user_selection()
            print("User chose:", user_action)
            
            if user_action == Action.Rock:
                dict_stat["Rock"] = dict_stat["Rock"] + 1
            elif user_action == Action.Paper:
                dict_stat["Paper"] = dict_stat["Paper"] + 1
            elif user_action == Action.Scissors:
                dict_stat["Scissors"] = dict_stat["Scissors"] + 1
            elif user_action == Action.Spock:
                dict_stat["Spock"] = dict_stat["Spock"] + 1
            elif user_action == Action.Lizard:
                dict_stat["Lizard"] = dict_stat["Lizard"] + 1

        except ValueError as e:
            # if an impossible actions gets chosen, let the user know
            range_str = f"[0, {len(Action) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            # continue statement in Python returns the control to the beginning of the while loop.
            continue
        # let computer pick choice
        computer_action = get_computer_selection()
        determine_winner(user_action, computer_action)

        play_again = input("Play again? (y/n): ")
        # .lower because we also accept Y as well as y
        if play_again.lower() != "y":
            break  # ends while True

        save_data_to_file()


