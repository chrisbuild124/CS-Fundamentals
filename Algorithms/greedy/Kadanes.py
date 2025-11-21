# Maximum subarray sum
# Link: https://leetcode.com/problems/maximum-subarray/description/

# The trick is to use Kadane's alg, and mimic a sliding window.
# Move the left when the entire window goes neg

class Solution:
    def maxSubArray(self, nums):
        # Kadane's Algorithm 
        cur = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if cur < 0:
                cur = 0
            cur += nums[i]
            res = max(cur, res)
        
        return res
