class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0: return '0'
        res = ''
        if (numerator > 0) ^ (denominator > 0):
            res += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator / denominator)
        numerator %= denominator
        if numerator == 0: return res
        res += '.'
        dic = {numerator: len(res)}
        while numerator != 0:
            numerator *= 10
            res += str(numerator / denominator)
            numerator %= denominator
            if numerator in dic:
                index = dic[numerator]
                res = res[:index] + '(' + res[index:] + ')'
                break
            else:
                dic[numerator] = len(res)

        return res