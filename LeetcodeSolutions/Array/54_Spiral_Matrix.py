class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return matrix
        m, n = len(matrix), len(matrix[0])
        left, right, up, down = 0, n - 1, 0, m - 1
        res = []
        while len(res) < n * m:
            for i in range(left, right + 1):
                if len(res) < m * n:
                    res.append(matrix[up][i])
            for i in range(up + 1, down):
                if len(res) < m * n:
                    res.append(matrix[i][right])
            for i in range(right, left, -1):
                if len(res) < m * n:
                    res.append(matrix[down][i])
            for i in range(down, up, -1):
                if len(res) < m * n:
                    res.append(matrix[i][left])
            up += 1; down -= 1; left += 1; right -= 1

        return res