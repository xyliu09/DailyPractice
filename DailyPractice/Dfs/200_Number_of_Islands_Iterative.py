class Solution:
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] == "*"
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        stack = [(i, j)]
        while stack:
            nx, ny = stack.pop()
            for x, y in Solution.direction:
                if 0 <= nx + x < len(grid) and 0 <= ny + y < len(grid[0]) and grid[nx + x][ny + y] == "1":
                    stack.append((nx + x, ny + y))
                    grid[nx + x][ny + y] = "*"
