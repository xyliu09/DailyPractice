import collections

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = collections.deque([0])
        visited = [0]
        depth = 0
        while queue:
            size = len(queue)
            depth += 1
            while size>0:
                curr = queue.popleft()
                i = 1
                while curr+i*i<=n:
                    if curr+i*i == n:
                        return depth
                    else:
                        queue.append(curr+i*i)
                        visited.append(curr+i*i)
                    i += 1
                size -= 1
        return -1