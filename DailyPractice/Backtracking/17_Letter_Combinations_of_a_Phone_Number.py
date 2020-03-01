
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        '''
        cmb = [''] if digits else []
        for d in digits:
            cmb = [p + q for p in cmb for q  in phone[d]]
        return cmb
        '''
        res = []

        def dfs(start, curr):
            curr = list(curr)
            if len(curr) == len(digits):
                res.append(''.join(curr[:]))
                return
            for ch in phone[digits[start]]:
                curr.append(ch)
                dfs(start + 1, tuple(curr))
                curr.pop()
        if digits:
            dfs(0, tuple([]))
        return res