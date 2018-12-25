"""
>>> arrayManipulation(5, [[1,2,100], [2,5,100],[3,4,100]])
200
"""


def arrayManipulation(n, queries):
    diff_array = [0] * (n + 1)
    for query in queries:
        x, y, increase = query[0], query[1], query[2]
        diff_array[x - 1] = increase
        if y <= len(diff_array):
            diff_array[y] -= increase
    maxval = x = 0
    for i in diff_array:
        x = x + i
        if x > maxval:
            maxval = x
    return maxval


if __name__=="__main__":
    import doctest
    doctest.testmod()