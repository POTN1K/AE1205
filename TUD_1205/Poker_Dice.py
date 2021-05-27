# Assignment Three. A poker dice game against the computer
# Author: Nikolaus Ricker

# ----------------------------------------------------------
# Libraries
from random import randint


# ----------------------------------------------------------
# Functions
def roll(hand_):
    ndice = 5 - len(hand_)
    for n in range(0, ndice):
        hand_.append(randint(1, 6))
    hand_.sort()
    return hand_


def analyse(hand_):
    """Takes the hand, separates it in unique values and amount of them"""
    unique = sorted(set(hand_))
    values = []
    score = len(unique)
    """ score=1, five of a kind
        score=2, four of a kind/ full house
        score=3, three of a kind/ two pairs
        score=4, one pair
        score=5, bust/ straight"""

    for i in unique:
        values.append((i, hand_.count(i)))

    values.sort(key=lambda tup: tup[1], reverse=True)
    return values, score


def select(values, score, hand_):
    """Checks what you have and the possibilities, then chooses what to keep"""
    if score == 1:  # Five of a kind
        pass
    elif score == 2:  # Four of a kind/Full house
        for i in values:
            if i[1] == 1:  # Four of a kind
                hand_.remove(i[0])
                break
            if i[1] == 2:  # Full house
                break
    elif score == 3:  # Three of a kind/Two pairs
        for i in values:
            if i[1] == 3:  # Three of a kind
                hand_ = [i[0], i[0], i[0]]
                break
            if i[1] == 1:  # Two pairs
                hand_.remove(i[0])
    elif score == 4:  # One pair
        for i in values:
            if i[1] == 2:
                hand_ = [i[0], i[0]]
                break
    elif score == 5:  # Bust/ straight
        if hand_ == [1, 2, 3, 4, 5] or hand_ == [2, 3, 4, 5, 6]:
            pass
        else:
            hand_ = []
    return hand_


def choose(positions_, hand_):
    new_hand = []
    choose_ = positions_.split()
    for i in choose_:
        if i.isdigit():
            i = int(i)
            if i != 1 and i != 2 and i != 3 and i != 4 and i != 5:
                print("Give a number in the range")
                return True, hand_
        else:
            print("Give a valid answer. Eg 2 5 3")
            return True, hand_
        new_hand.append(hand_[i - 1])
    return False, new_hand


def points(p_):
    if len(p_) == 1:  # Five of a kind
        return [10, p_[0][0], 0, 0, 0, 0]
    if len(p_) == 2:
        if p_[0][1] == 4:  # Four of a kind
            return [11, p_[0][0], p_[1][0], 0, 0, 0]
        else:
            return [12, p_[0][0], p_[1][0], 0, 0, 0]
    if len(p_) == 3:
        if p_[0][1] == 3:
            return [14, p_[0][0], p_[1][0], p_[2][0], 0, 0]
        else:
            return [15, p_[0][0], p_[1][0], p_[2][0], 0, 0]
    if len(p_) == 4:
        return [16, p_[0][0], p_[1][0], p_[2][0], p_[3][0], 0]
    if len(p_) == 5:
        if (p_[0][0] == 6 and p_[4][0] == 2) or (p_[0][0] == 5 and p_[4][0] == 1):
            return [13, p_[0][0], p_[1][0], p_[2][0], p_[3][0], p_[4][0]]
        else:
            return [17, p_[0][0], p_[1][0], p_[2][0], p_[3][0], p_[4][0]]


def winner_round(p1_, p2_):
    if p1_[0] > p2_[0]:
        return [0, 1]
    elif p2_[0] > p1_[0]:
        return [1, 0]
    elif p1_[1] > p2_[1]:
        return [1, 0]
    elif p2_[1] > p1_[1]:
        return [0, 1]
    elif p1_[2] > p2_[2]:
        return [1, 0]
    elif p2_[2] > p1_[2]:
        return [0, 1]
    elif p1_[3] > p2_[3]:
        return [1, 0]
    elif p2_[3] > p1_[3]:
        return [0, 1]
    elif p1_[4] > p2_[4]:
        return [1, 0]
    elif p2_[4] > p1_[4]:
        return [0, 1]
    else:
        return [0, 0]


# ----------------------------------------------------------
# Classes
class Player:
    def __init__(self, name_):
        self.name_ = name_
        self.hand = []
        self.score = 0
        self.sorted_values = []
        self.points = []


# ----------------------------------------------------------
# Variables
score_list = []

# ----------------------------------------------------------
# Start code
print("Welcome to Dice Poker! Beat the computer by getting the highers score.")
print("What is your name?")
name = input()

# Define players
p1 = Player(name)
p2 = Player('Computer')

# Repeat game three times
for j in range(3):
    print(f"Round {j+1}")
    error = True
    # Create/Update a hand for players
    p1.hand = roll(p1.hand)
    p2.hand = roll(p2.hand)

    # Computer
    print(f"{p2.name_} rolled: {p2.hand}")
    p2.sorted_values, p2.score = analyse(p2.hand)
    p2.points = points(p2.sorted_values)
    if j == 0 or j == 1:
        p2.hand = select(p2.sorted_values, p2.score, p2.hand)
        print(f"It kept {p2.hand}\n")

    # Player
    print(f"{p1.name_} rolled: {p1.hand}")
    p1.sorted_values, p1.score = analyse(p1.hand)
    p1.points = points(p1.sorted_values)
    if j == 0 or j == 1:
        print("which positions you want to keep? [1,2,3,4,5] \nSeparate them with a space:")

        while error:
            positions = input()
            error, new_hand_ = choose(positions, p1.hand)
        p1.hand = new_hand_
    print("\n----------------------------------\n")

    # Keeping track of score
    score_list.append(winner_round(p1.points, p2.points))

print(f"The score list is: {score_list}\n{p2.name_} - {p2.hand}\n{p1.name_} - {p1.hand}")

# Winner
i = 2
loop = True
while loop:
    if score_list[i][0] == 1:
        print(f"{p1.name_} wins!!!!!!!")
        loop = False
    elif score_list[i][1] == 1:
        print(f"{p2.name_} wins!!!!!!!")
        loop = False
    elif i == 0:
        print("Its a draw, what are the odds?!?!?!")
        loop = False
    else:
        i = i - 1
