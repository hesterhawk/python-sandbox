# Score categories
# Change the values as you see fit
YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def score(dice, category):
    dice = dict((x,dice.count(x)) for x in set(dice))

    switch = {
        1: _sumNumber,
        2: _sumNumber,
        3: _sumNumber,
        4: _sumNumber,
        5: _sumNumber,
        6: _sumNumber,
        7: _fullHouse,
        8: _fourOfAKind,
        9: _littleStraight,
        10: _bigStraight,
        11: _choice,
        12: _yacht
    }

    return switch[category](dice,category)

def _yacht(dice,category):
    if 5 in dice.values():
        return 50
    else:
        return 0

def _choice(dice,category): 
    result = 0
    for key,dd in dice.items():
        result += key * dd
    
    return result

def _bigStraight(dice,category): 
    if dice.keys() == set([2,3,4,5,6]):
        return 30
    else:
        return 0

def _littleStraight(dice,category): 
    if dice.keys() == set([1,2,3,4,5]):
        return 30
    else:
        return 0

def _fourOfAKind(dice,category):
    for key,dd in dice.items():
        if dd >= 4:
            return key * 4
    
    return 0

def _fullHouse(dice,category):
    if 2 in dice.values() and 3 in dice.values():
        inv = {v: k for k, v in dice.items()}
        return inv[2] * 2 + inv[3] * 3
    else:
        return 0

def _sumNumber(dice,category):  
    if category in dice:        
        return category * dice[category]
    else:
        return 0