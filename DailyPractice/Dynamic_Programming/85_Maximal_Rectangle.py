class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        res = 0
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
              for j in range(len(matrix[0])):
                    if matrix[i][j] == '0':
                        continue
                    width = dp[i][j] = dp[i][j-1] + 1 if j else 1
                    for k in range(i, -1, -1):
                        width = min(width, dp[k][j])
                        res = max(res, width*(i-k+1))
        return res