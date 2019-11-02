class NumArray(object):
    #Use dp array caching
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.memo = [sum(nums[:j]) for j in range(len(nums) + 1)]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.memo[j + 1] - self.memo[i]



        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)