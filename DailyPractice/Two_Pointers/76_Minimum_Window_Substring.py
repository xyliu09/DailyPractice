import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        l, r = 0, 0
        dict_t = collections.Counter(t)
        required = len(dict_t)
        window_t = {}
        formed = 0
        ans = float("inf"), None, None
        while r < len(s):
            character = s[r]
            window_t[character] = window_t.get(character, 0) + 1
            if character in dict_t and window_t[character] == dict_t[character]:
                formed += 1
            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                character = s[l]
                window_t[character] -= 1

                if character in dict_t and window_t[character] < dict_t[character]:
                    formed -= 1

                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]