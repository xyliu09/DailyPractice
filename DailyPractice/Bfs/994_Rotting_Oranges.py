import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        print(queue)
        def neighbor(i, j):
            for x, y in directions:
                nr, nc = i+x, j+y
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    yield nr, nc
        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in neighbor(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d+1))
        if any(1 in row for row in grid):
            return -1
        return d