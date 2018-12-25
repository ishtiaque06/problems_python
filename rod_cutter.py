"""
>>> cut_rod(8, [1,5,8,9,10,17,17,20])
22

>>> cut_rod(8, [3,5,8,9,10,17,17,20])
24

>>> cut_rod(4, [2,5,9,10])
11


>>> cut_rod(3, [1,4,5])
5

>>> cut_rod(3, [5,3,4])
15
"""


def cut_rod(n, price):
    val = [0 for x in range(n + 1)]
    val[0] = 0

    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n + 1):
        max_val = -12345678
        for j in range(i):
            max_val = max(max_val, val[j] + price[i - j - 1])
        val[i] = max_val

    return val[n]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

