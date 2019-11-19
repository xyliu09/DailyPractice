class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)
        for i in range(numCourses):
            if not self.dfs(graph, i, visited):
                return False
        return True

    def dfs(self, graph, i, visited):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for c in graph[i]:
            if not self.dfs(graph, c, visited):
                return False
        visited[i] = 1
        return True