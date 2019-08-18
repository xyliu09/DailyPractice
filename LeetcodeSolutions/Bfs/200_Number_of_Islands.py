class Solution(object):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

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
        q = []
        q.append((i, j))
        while q:
            m, n = q.pop(0)
            for x, y in Solution.directions:
                if m + x < 0 or n + y < 0 or m + x > len(grid) - 1 or n + y > len(grid[0]) - 1 or grid[m + x][
                            n + y] != "1":
                    continue
                grid[m + x][n + y] = "*"
                q.append((m + x, n + y))

'''
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid,i,j)
                    count +=1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j <0 or i>len(grid)-1 or j >len(grid[0])-1: 
            return
        if grid[i][j]!="1":
            return
        grid[i][j] = "*"
        for x, y in Solution.directions:
            self.dfs(grid, i+x, j+y)

'''