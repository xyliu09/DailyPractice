class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        visited = set()

        def dfs(i):
            for nei, adj in enumerate(M[i]):
                if adj and nei not in visited:
                    visited.add(nei)
                    dfs(nei)
            return

        for i in range(len(M)):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count += 1
        return count