class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp, costs = collections.deque([(0,0,0)]), {}
        direction = [(0, 1), (0, -1), (1,0), (-1, 0)]
        while dp:
            nx, ny, cost = dp.popleft()
            while 0 <= nx< m and 0<= ny<n and (nx, ny) not in costs:
                costs[(nx, ny)] = cost
                dp += [(nx+x, ny+y, cost + 1) for x, y in direction]
                dx, dy = direction[grid[nx][ny]-1]
                nx = nx + dx
                ny = ny + dy
        return costs[(m-1,n-1)]