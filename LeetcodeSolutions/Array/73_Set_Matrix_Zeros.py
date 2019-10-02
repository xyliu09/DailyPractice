class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]: return
        rowZero, colZero = False, False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                rowZero = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                colZero = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if rowZero:
            for i in range(m):
                matrix[i][0] = 0
        if colZero:
            for j in range(n):
                matrix[0][j] = 0