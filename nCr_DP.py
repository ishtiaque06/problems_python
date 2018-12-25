"""
>>> nCr(4, 2)
6
"""


def nCr(n, k):
    # C = [[0] * (k+1) for i in range(n+1)]
    # for i in range(n+1):
    #     C[i][0] = 1
    # for i in range(1, k+1):
    #     C[0][i] = 0
    # for i in range(1, n+1):
    #     for j in range(1, k+1):
    #         C[i][j] = C[i-1][j-1] + C[i-1][j]
    # return C
    C = [0] * (k+1)
    C[0] = 1
    for i in range(n):
        print(i)
        C_backup = C[:]
        for j in range(1, k+1):
            C[j] += C_backup[j-1]
    return C[k]


print(nCr(4, 2))
print(nCr(5, 4))
print(nCr(6, 3))