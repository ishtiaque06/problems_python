"""
>>> reverse(123)
321

>>> reverse(1534236469)
0

"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    lower = -(2 ** 31)
    upper = (2 ** 31) - 1
    if x < 0:
        neg = True
    else:
        neg = False
    x = abs(x)
    answer = 0
    while (x // 10) >= 0:
        answer = (answer * 10) + x % 10
        x //= 10
        if x == 0:
            break
    if neg:
        answer = -answer
    else:
        answer = answer
    if answer < lower or answer > upper:
        return 0
    return answer


if __name__ == "__main__":
    import doctest
    doctest.testmod()


