#! python3
'''
Zebra Puzzle
'''

import itertools

HOUSES = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(HOUSES))


def is_right(house1, house2):
    '''
    House house1 is immediately right of house2 if house1-house2 == 1.
    '''
    return house1 - house2 == 1


def next_to(house1, house2):
    '''
    Two houses are next to each other if they differ by 1.
    '''
    return abs(house1 - house2) == 1


for (red, green, ivory, yellow, blue) in orderings:
    for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings:
        for (dog, snails, fox, horse, ZEBRA) in orderings:
            for (coffee, tea, milk, oj, WATER) in orderings:
                for (OldGold, Kools, Chesterfields, LuckyStrike,
                     Parliaments) in orderings:
                    if Englishman is red:
                        pass
