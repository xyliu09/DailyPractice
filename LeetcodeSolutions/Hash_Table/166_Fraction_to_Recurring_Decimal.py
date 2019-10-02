class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ""
        if numerator == 0:
            return "0"
        if (numerator > 0) ^ (denominator > 0):
            res += "-"
        num = abs(numerator)
        den = abs(denominator)
        res += str(num / den)
        num %= den;
        if (num == 0):
            return str(res)
        res += "."
        dic = {num: len(res)}
        while num != 0:
            num *= 10
            res += str(num / den)
            num %= den
            if num in dic:
                index = dic[num]
                res = res[:index] + "(" + res[index:] + ")"
                break
            else:
                dic[num] = len(res)

        return res