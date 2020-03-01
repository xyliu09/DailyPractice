class Solution(object):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        self.dp = [[-1 for _ in matrix[0]] for _ in matrix]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, self.dfs(matrix, i, j))
        return ans

    def dfs(self, matrix, i, j):
        if self.dp[i][j] != -1: return self.dp[i][j]
        self.dp[i][j] = 1
        for x, y in Solution.directions:
            tx = i + x
            ty = j + y
            if tx < 0 or ty < 0 or tx > len(matrix) - 1 or ty > len(matrix[0]) - 1 or matrix[tx][ty] <= matrix[i][j]:
                continue
            self.dp[i][j] = max(self.dp[i][j], 1 + self.dfs(matrix, tx, ty))
        return self.dp[i][j]

