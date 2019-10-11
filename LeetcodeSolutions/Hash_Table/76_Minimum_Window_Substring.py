import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t: return ""
        r, l =0, 0
        ans = float('inf'), None, None
        count = collections.Counter(t)
        required=len(count)
        window = {}
        formed = 0
        while r < len(s):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1
            if ch in count and window[ch] == count[ch]:
                formed +=1
            while l<=r and formed == required:
                ch = s[l]
                if r-l+1 < ans[0]:
                    ans = r-l+1, l, r
                window[ch] -= 1
                if ch in count and window[ch] < count[ch]:
                    formed -=1
                l += 1
            r+=1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]