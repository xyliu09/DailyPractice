class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, i  = 0, 0
        while i < len(s):
            seen = {}
            seen[s[i]] = i
            j =  i + 1
            while j < len(s):
                if s[j] in seen:
                    break
                seen[s[j]] = j
                j += 1
            res = max(res, j - seen[s[i]])  
            i += 1
        return res