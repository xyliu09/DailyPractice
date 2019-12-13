class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        hashmap = set()
        maxlen = 0
        for i in range(len(s)):
            res = 0
            for j in range(i, len(s)):
                if s[j] in hashmap:
                    continue
                hashmap.add(s[j])

                if len(hashmap) > k:
                    res = j - i + 1
                    break
            maxlen = max(maxlen, res)

        return maxlen            