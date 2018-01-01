import string, re, itertools


def valid(f):
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) == True
    except ZeroDivisionError:
        return False


def solve(formula):
    '''
    Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    '''
    for f in fill_in(formula):
        if valid(f):
            return f


def fill_in(formula):
    '''
    Generate all possible fillings-in of letters in formula with digits.
    '''
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    for it in itertools.permutations(string.digits, r=len(letters)):
        table = str.maketrans(letters, ''.join(it))
        yield formula.translate(table)


if __name__ == '__main__':
    print(solve('ODD + ODD == EVEN'))
