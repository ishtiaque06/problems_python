"""
>>> countSubstrings("abc")
"""


def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    "aaaaaa"
    import math
    p_count = 0
    for i in range(len(s)):
        if i > 0:
            if i % 2 == 0:
                hello = s[:i // 2]
                hi = s[(i // 2) + 1:i + 1]
                if s[:i // 2] == s[(i // 2) + 1:i + 1]:
                    p_count += 1
            elif i % 2 != 0:
                if s[:math.ceil(i / 2)] == s[math.ceil(i / 2):i + 1]:
                    p_count += 1
    p_count += len(s)
    return p_count


if __name__ == "__main__":
    import doctest
    doctest.testmod()