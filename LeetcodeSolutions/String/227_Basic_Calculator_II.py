class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        num, stack, sign = 0, [], '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    signage = 1 if stack[-1] >= 0 else -1
                    stack.append(signage * (abs(stack.pop()) // num))
                sign = s[i]
                num = 0
        return sum(stack)
