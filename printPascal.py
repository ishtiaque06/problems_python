"""

>>> printPascal(5)


"""


def printPascal(n):
    if n == 0:
        return []
    pascal = [[1]]
    for i in range(1, n):
        if i == 1:
            pascal.append([1, 1])
        else:
            previous = pascal[-1]
            new = [0] * (len(previous)+1)
            new[0] = 1
            new[-1] = 1
            for j in range(1, len(previous)):
                new[j] += previous[j] + previous[j-1]
            pascal.append(new)
    return pascal


if __name__ == "__main__":
    import doctest
    doctest.testmod()