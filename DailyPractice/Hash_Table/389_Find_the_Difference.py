class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict = {}
        for e in s:
            dict[e] = dict.get(e, 0) + 1
        for e in t:
            if dict.get(e, 0) == 0:
                return e
            else:
                dict[e] -= 1
