class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        def find(parents, i):
            if parents[i] == -1:
                return i
            return find(parents, parents[i])

        def union(parents, x, y):
            xset = find(parents, x)
            yset = find(parents, y)
            if xset != yset:
                parents[xset] = yset

        parents = [-1 for _ in M]

        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1 and i != j:
                    union(parents, i, j)

        count = 0
        for p in parents:
            if p == -1:
                count += 1
        return count
