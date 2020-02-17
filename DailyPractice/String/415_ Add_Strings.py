class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        num1, num2 = num1[::-1], num2[::-1]
        ans = ''
        carry = 0
        i = 0
        while i < m or i < n:
            n1 = int(num1[i]) if i < m else 0
            n2 = int(num2[i]) if i < n else 0
            ans += str((n1 + n2 + carry) % 10)
            carry = int(n1 + n2 + carry) // 10
            i += 1
        ans += '1' if carry else ''
        return ans[::-1]



