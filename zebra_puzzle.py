#! python3
'''
Zebra Puzzle
'''

import itertools

HOUSES = [1, 2, 3, 4, 5]
orderings = list(itertools.permutations(HOUSES))

for (red, green, ivory, yellow, blue) in orderings:
    for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in orderings:
        for (dog, snails, fox, horse, ZEBRA) in orderings:
            for (coffee, tea, milk, oj, WATER) in orderings:
                for (OldGold, Kools, Chesterfields, LuckyStrike,
                     Parliaments) in orderings:
                    if Englishman is red:
                        pass
