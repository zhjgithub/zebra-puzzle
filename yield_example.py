'''
Examples of yield.
'''


def ints(start, end=None):
    '''
    Generate integers from start to end or infinite.
    '''
    i = start
    while end is None or i <= end:
        yield i
        i = i + 1


def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    yield 0
    for i in ints(1):
        yield +i
        yield -i
