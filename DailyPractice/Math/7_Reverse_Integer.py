class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = -1 if x <0 else 1
        value = abs(x)
        new = 0
        while value >0:
            new = new*10 + value%10
            if new > 2**31-1 or new < -2**31:
                return 0
            value /=10
        return isNegative*new