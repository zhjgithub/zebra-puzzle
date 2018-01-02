'''
Longest palindrome.
'''


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if text == '':
        return 0, 0
    if len(text) is 1:
        return 0, 1
    text = ''.join(map(str.upper, text))
    cur = l = len(text)
    for _ in range(l):
        for i in range(l - cur + 1):
            temp = text[i:i + cur]
            if is_palindrome_iteration(temp):
                return i, i + cur
        cur -= 1


def is_palindrome_iteration(s):
    '''
    Return true if a string is palindrome.
    '''
    for i in range(0, len(s) // 2):
        if s[i] != s[-1 - i]:
            return False
    return True


def test():
    '''
    Test.
    '''
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('Race car') == (0, 1)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'


print(test())
