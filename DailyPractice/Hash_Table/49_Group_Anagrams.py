class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            k = ''.join(sorted(s))
            print(k)
            if k in dic:
                dic[k].append(s)
            else:
                dic[k] = [s]
        return dic.values()
