class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = []
        while n > 1:
            n = sum([ int(i)**2 for i in str(n)])
            if n in mem:
                return False
            mem.append(n)
        return True