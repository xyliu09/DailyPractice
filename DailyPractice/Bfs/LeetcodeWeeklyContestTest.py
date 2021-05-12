class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        start = 0
        seen = set()
        while start < len(nums): 是 =
        mi, ma = min(nums[start:start + 1]), max(nums[start:start + 1])
        end = start + 1
        while end < len(nums):

            while end < len(nums) and (nums[end] == nums[end - 1] or tuple(nums[start:end + 1]) in seen):
                end += 1
            if end < len(nums):
                if (nums[end] > ma and nums[end] - mi > limit) or (nums[end] < mi and ma - nums[end] > limit):
                    break
                ma = max(ma, nums[end])
                mi = min(mi, nums[end])
                seen.add(tuple(nums[start:end + 1]))
                end += 1
        res = max(res, end - start)
        start += 1

    return res
