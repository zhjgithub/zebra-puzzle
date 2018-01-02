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
                if immediate_right(green, ivory)  # 6
                for (Englishman, Spaniard, Ukrainian, Japanese,
                     Norwegian) in orderings if Englishman is red  # 2
                if Norwegian is first  # 10
                if next_to(Norwegian, blue)  #15
                for (coffee, tea, milk, oj, WATER) in orderings
                if coffee is green  # 4
                if Ukrainian is tea  # 5
                if milk is middle  # 9
                for (OldGold, Kools, Chesterfields, LuckyStrike,
                     Parliaments) in orderings if Kools is yellow  # 8
                if LuckyStrike is oj  # 13
                if Japanese is Parliaments  # 14
                for (dog, snails, fox, horse, ZEBRA) in orderings
                if Spaniard is dog  # 3
                if OldGold is snails  # 7
                if next_to(Chesterfields, fox)  # 11
                if next_to(Kools, horse)  # 12
                )


def timed_call(fn, *args):
    '''
    Call function with args; return the time in seconds and result.
    '''
    import time
    start_time = time.clock()
    result = fn(*args)
    end_time = time.clock()
    return end_time - start_time, result


def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))


def timed_calls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n, int):
        times = [timed_call(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        total_time = 0.0
        while total_time < n:
            time = timed_call(fn, *args)[0]
            times.append(time)
            total_time += time
    return min(times), average(times), max(times)


def c(sequence):
    '''
    Generate items in sequence; keeping counts as we go.
    c.starts is the number of sequences started; c.items is number of items generated.
    '''
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item


def instrument_fn(fn, *args):
    '''
    Instrument for count how many items generator from generator.
    '''
    c.starts, c.items = 0, 0
    result = fn(*args)
    print('%s got %s with %5d iters over %7d items' % (fn.__name__, result,
                                                       c.starts, c.items))


if __name__ == '__main__':
    print(timed_calls(1000, zebra_puzzle))
