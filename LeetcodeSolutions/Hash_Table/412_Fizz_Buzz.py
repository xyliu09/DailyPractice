class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizzbuzzdict = {3: "Fizz", 5: "Buzz"}
        res = []
        for number in range(1, n+1):
            numstoadd = ""
            for key,item in fizzbuzzdict.iteritems():
                if number%key == 0:
                    numstoadd += item
            if not numstoadd:
                numstoadd = str(number)
            res.append(numstoadd)
        return res