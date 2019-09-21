from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        indegree = {}
        topo = []
        for des, src in prerequisites:
            graph[src].append(des)
            indegree[des] = indegree.get(des, 0) + 1
        stack = [k for k in range(numCourses) if k not in indegree]
        while stack:
            node = stack.pop()
            topo.append(node)
            if node in graph:
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        stack.append(nei)

        return topo if len(topo) == numCourses else []
