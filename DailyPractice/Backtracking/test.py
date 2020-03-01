def matrixSummation(after):
    before = [[0 for i in range(len(after))] for j in range(len(after[0]))]
    before[0][0] = after[0][0]
    for i in range(1, len(after)):
        before[i][0] = after[i][0] - after[i - 1][0]

    for j in range(1, len(after[0])):
        before[0][j] = after[0][j] - after[0][j - 1]
    print('before',before)
    for i in range(1, len(after)):
        for j in range(1, len(after[0])):
            print(i,j)
            print(after[i][j] ,after[i - 1][j - 1] , after[i - 1][j] ,after[i][j - 1])
            before[i][j] = after[i][j] + after[i - 1][j - 1] - after[i - 1][j] - after[i][j - 1]
            print(before)
    return before


a= [[1,2],[3,4]]
res = matrixSummation(a)