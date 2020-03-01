class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i = 0
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            p, q = i+1, len(nums)-1
            while p < q:
                if nums[i] + nums[p] +nums[q] > 0:
                    q -= 1
                elif nums[i] + nums[p] +nums[q] < 0:
                    p += 1
                elif nums[i] + nums[p] + nums[q] == 0:
                    res.append((nums[i], nums[p], nums[q]))
                    while p < q and nums[p] == nums[p+1]:
                        p += 1
                    while p < q and nums[q] == nums[q-1]:
                        q -= 1
                    p += 1
                    q -= 1
        return res