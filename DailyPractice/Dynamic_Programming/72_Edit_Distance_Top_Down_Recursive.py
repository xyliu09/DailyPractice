class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        self.memo = [[-1 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        return self.helper(word1, word2, l1, l2)

    def helper(self, word1, word2, l1, l2):
        if l1 == 0: return l2
        if l2 == 0: return l1
        if self.memo[l1][l2] >= 0: return self.memo[l1][l2]

        if word1[l1 - 1] == word2[l2 - 1]:
            ans = self.helper(word1, word2, l1 - 1, l2 - 1)
        else:
            ans = min(self.helper(word1, word2, l1 - 1, l2 - 1), self.helper(word1, word2, l1 - 1, l2),
                      self.helper(word1, word2, l1, l2 - 1)) + 1
        self.memo[l1][l2] = ans
        return self.memo[l1][l2]
