# 13*4 = 52 Karten
# https://www.cardplayer.com/rules-of-poker/hand-rankings
import random

cards = []
value_cnt = {}
color = ["Kreuz", "Pik", "Karo", "Herz"]
# 11 - Bub, 12 - Dame, 13 - König, 14 - Ass
symbol = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# create list with cards from array
for col in color:
    for sym in symbol:
        # cards.append({'color': col, 'symbol': sym})
        cards.append((sym, col))
        # print(cards)


test_cards = [(9, 'Pik'), (10, 'Pik'), (11, 'Pik'), (12, 'Pik'), (13, 'Pik')]


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
    return r5


# 5, all one suit
def flush(rand_5):
    suit = [i[1] for i in rand_5]
    value_cnt = {}
    for s in suit:
        if s not in value_cnt.keys():
            value_cnt[s] = 1
        else:
            value_cnt[s] += 1
    return list(value_cnt.values()).count(5) == 1


# cards ascending, suit doesn't matter
def straight(rand_5):
    # if difference between the max rank and min rank plus one is equal to the size of the set
    # and the set is the size of the hand, you have a straight
    # rank_set = {card['rank'] for card in rand_5}
    rank_set = [i[0] for i in rand_5]
    rank_range = max(rank_set) - min(rank_set) + 1
    return rank_range == len(rand_5) and len(rank_set) == len(rand_5)


def check_multiple(rand_5):
    ranks = [i[0] for i in rand_5]
    # print(ranks)
    # print (col)
    for rank in ranks:
        # if color is not a key yet, add this color for the first time
        if rank not in value_cnt.keys():
            value_cnt[rank] = 1
        # if we already have our colors in this list we want to add want more
        else:
            value_cnt[rank] += 1


# two cards of the same suit
def one_pair(rand_5):
    check_multiple(rand_5)
    print(list(value_cnt.values()).count(2) == 1)
    return list(value_cnt.values()).count(2) == 1


# successes = [one_pair(random_five()) for _ in range(100)]


# three cards of the same suit
def three_of_a_kind(rand_5):
    check_multiple(rand_5)
    print (list(value_cnt.values()).count(3) == 1)
    return list(value_cnt.values()).count(3) == 1


# one pair and one three_of_a_kind
def full_house(rand_5):
    return three_of_a_kind(rand_5) and one_pair(rand_5)


# four cards of the same suit
def four_of_a_kind(rand_5):
    check_multiple(rand_5)
    print( list(value_cnt.values()).count(4) == 1)
    return list(value_cnt.values()).count(4) == 1


# two pairs
def two_pair(rand_5):
    check_multiple(rand_5)
    print ( list(value_cnt.values()).count(2) == 2)
    return list(value_cnt.values()).count(2) == 2


# royal_flush(random_five())


# same suit, ascending
def straight_flush(rand_5):
    ranks = [i[0] for i in rand_5]
    suit = [i[1] for i in rand_5]
    ranks.sort()
    if straight(rand_5) and suit.count(suit[0]) == len(suit):
        print("true")
        return True
    else:
        print("false")
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
        print("true")
        return True
    else:
        print("false")
        return False


#royal_flush(test_cards)
# royal_flush(rand_5x)
# random_five()
# one_pair(random_five())
