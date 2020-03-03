class Solution(object):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # bfs queue
    # dfs recursive or stack
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "*"
        for x, y in Solution.directions:
            self.dfs(grid, i + x, j + y)

