def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    dp = [0 for _ in nums]
    dp[0] = 1
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = dp[j] + 1
    print(dp)

    return max(dp)+1

a= [10,9,2,5,3,7,101,18]
lengthOfLIS(a)