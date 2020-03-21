class Solution:
    def depthSum(self, nestedList: List[NestedInteger], count = 1) -> int:
        ans = 0
        for i, value in enumerate(nestedList):
            if value.isInteger():
                ans += count * value.getInteger()
            else:
                ans += self.depthSum(value.getList(), count+1)
        return ans