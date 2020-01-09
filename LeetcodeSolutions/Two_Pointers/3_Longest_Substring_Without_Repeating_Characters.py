class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, i = 0, 0
        while i < len(s):
            j = i + 1
            seen = {s[i]: i}
            while j < len(s):
                if s[j] in seen:
                    break
                seen[s[j]] = j
                j += 1
            res = max(j - i, res)
            i += 1
        return res