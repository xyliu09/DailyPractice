class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        table = set()
        while n > 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in table:
                return False
            table.add(n)
        return True