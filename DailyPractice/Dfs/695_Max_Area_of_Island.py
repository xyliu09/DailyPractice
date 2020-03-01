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
                    self.dfs(grid, i, j)
                    count = max(count, Solution.maxArea)
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] != 1:
            return
        grid[i][j] = 0
        Solution.maxArea += 1
        for x, y in Solution.directions:
            self.dfs(grid, i + x, j + y)
