class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse= True)
        queue0, queue1, queue2 = [], [], []
        total = 0
        for i in range(len(digits)):
            total += digits[i]
            if digits[i]%3 == 0:
                queue0.append(digits[i])
            elif digits[i]%3 == 1:
                queue1.append(digits[i])
            elif digits[i]%3 == 2:
                queue2.append(digits[i])
        if total%3 == 1:
            if queue1:
                queue1.pop()
            else:
                if queue2:
                    queue2.pop()
                else:
                    return 0
                if queue2:
                    queue2.pop()
                else:
                    return 0
        elif total%3 ==2:
            if queue2:
                queue2.pop()
            else:
                if queue1:
                    queue1.pop()
                else:
                    return 0
                if queue1:
                    queue1.pop()
                else:
                    return 0
        arr = queue1+queue2+queue0
        arr.sort(reverse = True)
        if arr:
            return ''.join([str(i) for i in arr]) if arr[0] else "0"
        return ""