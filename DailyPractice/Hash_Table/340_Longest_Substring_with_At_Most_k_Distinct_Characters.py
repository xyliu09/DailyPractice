from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        if k == 0 or n == 0:
            return 0
        left, right = 0, 0
        hashmap = defaultdict()
        max_len = 1
        while right < n:
            hashmap[s[right]] = right
            right += 1
            if len(hashmap) == k + 1:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                left = del_idx + 1
            max_len = max(max_len, right - left)
        return max_len