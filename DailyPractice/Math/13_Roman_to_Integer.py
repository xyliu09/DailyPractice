class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        prev, total = 0, 0
        for l in s[::-1]:
            curr = dic[l]
            if prev > curr:
                total -= curr
            else:
                total += curr
            prev = curr
        return total