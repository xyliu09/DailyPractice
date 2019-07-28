class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        stringlist = []
        maxlength = 0
        table = {}
        head = 0
        for x in s:
            if x in stringlist[head:]:
                head = table[x]+1
            stringlist.append(x)
            table[x] = len(stringlist)-1
            maxlength = max(maxlength, len(stringlist)-head)
        return maxlength