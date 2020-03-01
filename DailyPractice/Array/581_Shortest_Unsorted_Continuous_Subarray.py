class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        ssum = sorted(nums)
        start, end = len(nums)-1, 0
        for i in range(len(nums)):
            if nums[i]!= ssum[i]:
                start = min(start, i)
                end = max(end, i)
        return 0 if end - start <=0 else end -start + 1
        '''
        l, r = len(nums) - 1, 0
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)

        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)

        return r - l + 1 if r > l else 0