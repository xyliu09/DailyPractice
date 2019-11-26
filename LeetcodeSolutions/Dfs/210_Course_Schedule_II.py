import collections


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[y].append(x)
        visit = {i: 0 for i in range(numCourses)}
        self.ans = []
        for i in range(numCourses):
            if self.dfs(i, graph, visit): return
        return self.ans[::-1]

    def dfs(self, i, graph, visit):
        if visit[i] == 1:
            return True
        if visit[i] == 2:
            return False
        visit[i] = 1
        for node in graph[i]:
            if self.dfs(node, graph, visit): return True
        visit[i] = 2
        self.ans.append(i)
        return False