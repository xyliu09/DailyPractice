from collections import deque
"bfs"
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        for x, y in prerequisites:
            graph[x].append(y)
            indegree[y] += 1

        queue = deque([])
        for index, item in indegree.iteritems():
            if item == 0:
                queue.append(index)
        visited = []
        while queue:
            course = queue.popleft()
            visited.append(course)
            for i in graph[course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        return len(visited) == numCourses