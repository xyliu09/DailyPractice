class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        seen = set()

        def dfs(node):
            for nei, adj in enumerate(M[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        res = 0
        for i in range(len(M)):
            if i not in seen:
                seen.add(i)
                dfs(i)
                res += 1
        return res