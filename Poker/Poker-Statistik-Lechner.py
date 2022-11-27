# 13*4 = 52 Karten
# https://www.cardplayer.com/rules-of-poker/hand-rankings
# https://www.888poker.de/magazine/strategy/wahrscheinlichkeit-nutzen-poker#:~:text=Die%20Wahrscheinlichkeit%2C%20ein%20Full%20House,H%C3%A4nden%20oder%200%2C00139%25.
# filter: https://www.programiz.com/python-programming/methods/built-in/filter
# inspired by Marcel Maffey's Lösung mit Filter bei der 1. Besprechung der Aufgabe, weil eigen V1 bei Schleifendurchlauf
# nicht mehr funktioniert

import random

cards = []
value_cnt = {}
color = ["Kreuz", "Pik", "Karo", "Herz"]
# 11 - Bub, 12 - Dame, 13 - König, 14 - Ass
symbol = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
outcomes = ["Highcard", "Pair", "Two Pair", "Three of a Kind", "Straight", "Flush",
            "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]

stat = {}
games = 100001


def stat_dict():
    for i in outcomes:
        stat[i] = 0


# create list with cards from array
for col in color:
    for sym in symbol:
        cards.append((sym, col))
        # print(cards)

# test_cards = [(5, 'Pik'), (6, 'Herz'), (7, 'Karo'), (8, 'Kreuz'), (9, 'Pik')]
# test2 = [(2, 'Kreuz'), (2, 'Herz'), (13, 'Karo'), (14, 'Herz'), (10, 'Kreuz')]
test3 = [(4, 'Karo'), (4, 'Pik'), (4, 'Kreuz'), (7, 'Kreuz'), (10, 'Kreuz')]
test4 = [(5, 'Kreuz'), (6, 'Kreuz'), (7, 'Kreuz'), (8, 'Pik'), (9, 'Kreuz')]



# shuffle cards
def create_cards():
    deck_copy = cards.copy()
    shuffled_deck = []
    for i in range(len(cards)):
        random_card = random.choice(deck_copy)
        shuffled_deck.append(random_card)
        deck_copy.remove(random_card)
    # print(shuffled_deck)
    return shuffled_deck


# choose 5 random cards --> hand
def random_five():
    global drawn_card
    r5 = []
    shuffled_deck = create_cards()
    for i in range(5):
        drawn_card = random.choice(shuffled_deck)
        r5.append(drawn_card)
        shuffled_deck.remove(drawn_card)
    # print(r5)
    return r5


# 5, all one suit
def flush(rand_5):
    for i in color:
        # get/count length of same suits
        # adds all cards with the same suit to a new list and counts cards, if all cards are in one list we have a flush
        cnt = len(list(filter(lambda card: card[1] == i, rand_5)))
        # print(len(list(filter(lambda card: card[1] == i, rand_5))))
        if cnt == 5:
            # print("True")
            return True
    # print("False")
    return False


# cards ascending, suit doesn't matter
def straight(rand_5):
    # if difference between the max rank and min rank plus one is equal to the size of the set
    # and the set is the size of the hand, you have a straight
    rank_set = [i[0] for i in rand_5]
    rank_range = max(rank_set) - min(rank_set) + 1
    # print(rank_range == len(rand_5) and len(rank_set) == len(rand_5))
    return rank_range == len(rand_5) and len(rank_set) == len(rand_5)


# checks whether there are one or more pairs
def pairs(rand_5):
    pair = 0
    for i in symbol:
        # get length of list with same number
        # everytime we have the same number twice, the counter is increased by 1, therefore we can use this function for
        # one or more pairs
        cnt = len(list(filter(lambda card: card[0] == i, rand_5)))
        if cnt == 2:
            pair += 1
    return pair


# three cards of the same suit
def three_of_a_kind(rand_5):
    for i in symbol:
        # get length of list with same numbers
        # we have to have a list with three items for a three_of_a_kind
        cnt = len(list(filter(lambda card: card[0] == i, rand_5)))
        if cnt == 3:
            # print("True")
            return True
    # print("False")
    return False


# one pair and one three_of_a_kind
def full_house(rand_5):
    return three_of_a_kind(rand_5) and pairs(rand_5)


# four cards of the same suit
def four_of_a_kind(rand_5):
    for i in symbol:
        cnt = len(list(filter(lambda card: card[0] == i, rand_5)))
        if cnt == 4:
            return True
    return False


# same suit, ascending
def straight_flush(rand_5):
    ranks = [i[0] for i in rand_5]
    suit = [i[1] for i in rand_5]
    ranks.sort()
    if straight(rand_5) and suit.count(suit[0]) == len(suit):
        # print("true")
        return True
    else:
        # print("false")
        return False


# same suit ascending, lowest value ten
def royal_flush(rand_5):
    ranks = [i[0] for i in rand_5]
    suit = [i[1] for i in rand_5]
    ranks.sort()
    # check whether there is a street, the lowest rank is 10 and everything is of the same suit
    # suit-list must only contain one kind of suit in order to have a royal flush
    # suit.count has to be 5 because we need the same suit 5 times
    # --> len.count has as well as len(suit) to be five
    if straight(rand_5) and ranks[0] == 10 and suit.count(suit[0]) == len(suit):
        # print("true")
        return True
    else:
        # print("false")
        return False


# straight(test_cards)
# 1 / games * 100

def poker_stat(rand_cards):
    if royal_flush(rand_cards):
        stat["Royal Flush"] += round((1 / games * 100), 2)
    elif straight_flush(rand_cards):
        stat["Straight Flush"] += round((1 / games * 100), 2)
    elif four_of_a_kind(rand_cards):
        stat["Four of a Kind"] += round((1 / games * 100), 2)
    elif full_house(rand_cards):
        stat["Full House"] += round((1 / games * 100), 2)
    elif flush(rand_cards):
        stat["Flush"] += round((1 / games * 100), 2)
    elif straight(rand_cards):
        stat["Straight"] += round((1 / games * 100), 2)
    elif three_of_a_kind(rand_cards):
        stat["Three of a Kind"] += round((1 / games * 100), 2)
    elif pairs(rand_cards) == 2:
        stat["Two Pair"] += round((1 / games * 100), 2)
    elif pairs(rand_cards) == 1:
        stat["Pair"] += round((1 / games * 100), 2)
    else:
        stat["Highcard"] += round((1 / games * 100), 2)


stat_dict()


def main():
    for i in range(0, games):
        poker_stat(random_five())
    print(stat)


if __name__ == "__main__":
    main()




# royal_flush(test_cards)
# royal_flush(rand_5x)
# random_five()
# one_pair(random_five())
