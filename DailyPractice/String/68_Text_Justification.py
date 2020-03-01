class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr, currLen, ans = [], 0, []
        for word in words:
            if currLen + len(curr) + len(word) > maxWidth:
                for i in range(maxWidth - currLen):
                    curr[i % (len(curr) - 1 or 1)] += ' '
                ans.append(''.join(curr))
                curr, currLen = [], 0
            currLen += len(word)
            curr += [word]
        return ans + [' '.join(curr).ljust(maxWidth)]
