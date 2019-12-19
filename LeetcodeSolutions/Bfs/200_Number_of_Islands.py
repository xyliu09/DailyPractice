from collections import deque


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
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, i, j):
        queue = deque([(i, j)])
        grid[i][j] = "0"
        while queue:
            i, j = queue.popleft()
            for x, y in Solution.directions:
                if i + x < len(grid) and j + y < len(grid[0]) and i + x >= 0 and j + y >= 0 and grid[i + x][
                            j + y] == "1":
                    queue.append((i + x, j + y))
                    grid[i + x][j + y] = "0"
