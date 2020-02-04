class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            stack.append(a)
        res = []
        candidate = []
        while stack:
            node = stack.pop()

            if node > 0:
                if candidate:
                    negativenode = candidate.pop()
                    if abs(node) > abs(negativenode):
                        stack.append(node)
                    elif abs(node) < abs(negativenode):
                        stack.append(negativenode)
                else:
                    res.append(node)
            else:
                candidate.append(node)
        if candidate:
            res += candidate
        return reversed(res)