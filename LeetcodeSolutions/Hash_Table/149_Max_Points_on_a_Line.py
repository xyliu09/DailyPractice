class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            dic = {'i': 1}
            duplicate = 0
            maxPoint = 0
            for j in range(i + 1, len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dx == 0 and dy == 0:
                    duplicate += 1
                    continue
                gcd = self.gcd(dy, dx)
                k = (dx / gcd, dy / gcd)
                if k in dic:
                    dic[k] += 1
                else:
                    dic[k] = 1
                maxPoint = max(max(dic.values()), maxPoint)
            res = max(res, duplicate + maxPoint + 1)
        return res

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)