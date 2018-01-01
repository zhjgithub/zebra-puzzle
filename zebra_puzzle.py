#! python3
'''
Zebra Puzzle
'''

import itertools


def immediate_right(house1, house2):
    '''
    House house1 is immediately right of house2 if house1-house2 == 1.
    '''
    return house1 - house2 == 1


def next_to(house1, house2):
    '''
    Two houses are next to each other if they differ by 1.
    '''
    return abs(house1 - house2) == 1


def zebra_puzzle():
    '''
    Return a tuple (WATER, ZEBRA) indicating their house numbers.
    '''
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))  # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in orderings
                for (Englishman, Spaniard, Ukrainian, Japanese,
                     Norwegian) in orderings
                for (dog, snails, fox, horse, ZEBRA) in orderings
                for (coffee, tea, milk, oj, WATER) in orderings
                for (OldGold, Kools, Chesterfields, LuckyStrike,
                     Parliaments) in orderings
                if Englishman is red  # 2
                if Spaniard is dog  # 3
                if coffee is green  # 4
                if Ukrainian is tea  # 5
                if immediate_right(green, ivory)  # 6
                if OldGold is snails  # 7
                if Kools is yellow  # 8
                if milk is middle  # 9
                if Norwegian is first  # 10
                if next_to(Chesterfields, fox)  # 11
                if Kools is horse  # 12
                if LuckyStrike is oj  # 13
                if Japanese is Parliaments  # 14
                if next_to(Norwegian, blue))  #15
