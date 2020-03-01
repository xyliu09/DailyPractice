class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.grid = grid
        n = len(self.grid)
        self.memo = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]
        return max(0, self.dp(n - 1, n - 1, n - 1))

    def dp(self, x1, y1, x2):
        y2 = x1 + y1 - x2
        if x1 < 0 or x2 < 0 or y1 < 0 or y2 < 0 or self.grid[y1][x1] < 0 or self.grid[y2][x2] < 0:
            return -1
        if x1 == 0 and y1 == 0:
            return self.grid[y1][x1]
        if self.memo[y1][x1][x2] is not None:
            return self.memo[y1][x1][x2]
        ans = max(self.dp(x1 - 1, y1, x2 - 1), self.dp(x1, y1 - 1, x2), self.dp(x1, y1 - 1, x2 - 1),
                  self.dp(x1 - 1, y1, x2))
        if ans < 0:
            self.memo[y1][x1][x2] = -1
            return -1
        ans += self.grid[y1][x1] + (x1 != x2) * self.grid[y2][x2]
        self.memo[y1][x1][x2] = ans
        return ans