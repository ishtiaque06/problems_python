def warshall(matrix):
    # R_0 = matrix
    # n = len(matrix)
    # for k in range(1, n):
    #     for i in range(1, n):
    #         for j in range(1, n):
    #             R_0[i][j] = R_0[i][j] or (R_0[i][k] and R_0[k][j])
    # return R_0=
    n = len(matrix)
    # temp = [[0] * n for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
        # matrix = temp
    return matrix


print(warshall([[0,1,0,0],[0,0,0,1],[0,0,0,0],[1,0,1,0]]))
print(warshall([[0,1,0,0], [0,0,1,0],[0,0,0,1],[0,0,0,0]]))