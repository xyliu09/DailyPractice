from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        queue = deque()
        for i in range(len(nums)):
            queue = self.push(queue, nums[i])
            qmax = self.max(queue)
            if i - k + 1 >= 0:
                ans.append(qmax)
                if nums[i - k + 1] == qmax:
                    queue.popleft()
        return ans

    def push(self, queue, e):
        while queue and e > queue[-1]:
            queue.pop()
        queue.append(e)
        return queue

    def max(self, queue):
        return queue[0]

