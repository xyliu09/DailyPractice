#Solution 1: set, o(n)o(n)
#Solution 2：sort,o(nlgn)o(1)
#Solution 2: o(n)o(1)
#def spiralOrder(self, matrix):
#    return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        p1 = nums[0]
        p2 = slow
        while p1!= p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1