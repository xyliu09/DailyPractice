from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t: return ''
        dic_t = Counter(t)
        l,r = 0, 0
        formed,required,dict_window = 0, len(dic_t),{}
        ans = (float('inf'), r, l)
        while r < len(s):
            char = s[r]
            dict_window[char] = dict_window.get(char,0) + 1
            if char in dic_t and dict_window[char] == dic_t[char]:
                formed+=1
            while l<= r and formed == required:
                char = s[l]
                if r-l+1<ans[0]:
                    ans = (r-l+1, l, r)
                dict_window[char]-= 1
                if char in dic_t and dict_window[char] < dic_t[char]:
                    formed -=1
                l += 1
            r += 1
        return '' if ans[0] == float('inf') else s[ans[1]:ans[2]+1]