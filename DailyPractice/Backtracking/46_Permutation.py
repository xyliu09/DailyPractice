class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(start=0, curr=[]):
            if len(curr) == len(nums):
                output.append(curr[:])
            for s in range(0, len(nums)):
                if nums[s] in curr: continue
                curr.append(nums[s])
                backtrack(start + 1, curr)
                curr.pop()

        output = []
        backtrack()
        return output
