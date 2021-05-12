class Solution:
    def removeInvalidParentheses(self,s):
        """
        BFS
        :param s:
        :return: list
        """

        queue = [s]
        visited = {s}
        res = []
        found = False
        while queue:
            substring = queue.pop(0)
            if self.isValid(substring):
                res.append(substring)
                found = True
            if found == True:
                continue
            for i in range(len(substring)):
                if substring[i] in '()':
                    nei = substring[:i]+ substring[i+1:]
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
        return res

    def findSolution(self,s):
        count = 0
        temp = ''
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            if count < 0:
                count = 0
                continue
            temp += s[i]

        res = ''
        for j in range(len(temp)-1, -1, -1):
            if count > 0 and temp[j] == '(':
                count -= 1
                continue
            res += temp[j]
        return res[::-1]


    def isValid(self, s):
        count = 0
        for i in range(len(s)):
            if count < 0:
                return False
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
        return count == 0



if __name__ == '__main__':
    a = Solution()
    print(a.findSolution(''))
    print(a.removeInvalidParentheses('a ='))
