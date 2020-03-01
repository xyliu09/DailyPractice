class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        '''
        if len(digits) == 1 and digits[-1] ==9:
            return [1,0]

        if digits[-1] != 9:
            digits[-1] += 1
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
        return   digits
        '''
        '''
        nums = 0
        for n in digits:
            nums = nums * 10 + n
        return [int(_) for _ in str(nums+1)]       
        '''
        for i in range(len(digits)):
            if digits[~i] < 9:
                digits[~i] += 1
                return digits
            digits[~i] = 0
        return [1] + [0] * len(digits)
