# This code is copied straight from neetcode's solution
# Link: https://neetcode.io/problems/longest-increasing-subsequence?list=neetcode150

# It tracks the longest increasing subsequence using DP and binary search 
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue

            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return LIS
