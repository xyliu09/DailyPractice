import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        for index, item in enumerate(s):
            if count[item]==1:
                return index
        return -1