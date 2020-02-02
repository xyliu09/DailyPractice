import functools


class Solution:
    @functools.lru_cache()
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 or not s2:
            return (s3 and (s3 == s1 or s3 == s2)) or s3 == s1 == s2
        if s3[-1] != s1[-1] and s3[-1] != s2[-1]:
            return False
        left, right = None, None
        if s3[-1] == s1[-1]:
            left = self.isInterleave(s1[:-1], s2, s3[:-1])
        if s3[-1] == s2[-1]:
            right = self.isInterleave(s1, s2[:-1], s3[:-1])
        return left or right

