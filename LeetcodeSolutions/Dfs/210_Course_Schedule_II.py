from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        for des, src in prerequisites:
            graph[src].append(des)
        topo = []
        self.is_possible = True
        color = {k: 0 for k in range(numCourses)}

        def dfs(node):

            if not self.is_possible:
                return
            color[node] = -1
            if node in graph:
                for nei in graph[node]:
                    if color[nei] == -1:
                        self.is_possible = False
                    elif color[nei] == 0:
                        dfs(nei)
            color[node] = 1
            topo.append(node)

        for i in range(numCourses):
            if color[i] == 0:
                dfs(i)

        return topo[::-1] if self.is_possible else []