class Solution(object):
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    maxArea = 0

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    Solution.maxArea = 0
                    self.bfs(grid, i, j)
                    count = max(count, Solution.maxArea)
        return count

    def bfs(self, grid, i, j):
        q = []
        q.append((i, j))
        grid[i][j] = 0
        while q:
            m, n = q.pop(0)
            Solution.maxArea += 1
            for x, y in Solution.directions:
                if m + x < 0 or n + y < 0 or m + x > len(grid) - 1 or n + y > len(grid[0]) - 1 or grid[m + x][
                            n + y] != 1:
                    continue
                grid[m + x][n + y] = 0
                q.append((m + x, n + y))