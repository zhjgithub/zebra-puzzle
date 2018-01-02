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


def longest_subpalindrome_slice2(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if text == '':
        return 0, 0
    if len(text) is 1:
        return 0, 1

    def length(pair):
        a, b = pair
        return b - a

    text = ''.join(map(str.upper, text))
    candidates = (grow(text, start, end)
                  for start in range(len(text)) for end in (start, start + 1))
    return max(candidates, key=length)


def grow(text, start, end):
    '''Start with a 0- or 1- length palindrome; try to grow a bigger one.'''
    while start > 0 and end < len(text) and text[start - 1] == text[end]:
        start -= 1
        end += 1
    return start, end


def test(fun=longest_subpalindrome_slice):
    '''
    Test.
    '''
    assert fun('racecar') == (0, 7)
    assert fun('Racecar') == (0, 7)
    assert fun('RacecarX') == (0, 7)
    assert fun('Race carr') == (7, 9)
    assert fun('Race car') == (0, 1)
    assert fun('') == (0, 0)
    assert fun('something rac e car going') == (8, 21)
    assert fun('xxxxx') == (0, 5)
    assert fun('Mad am I ma dam.') == (0, 15)
    # print('tests pass')


if __name__ == '__main__':
    import cProfile
    cProfile.run('for _ in range(100):test()')
    cProfile.run('for _ in range(100):test(fun=longest_subpalindrome_slice2)')
