# Product use of kadane's algorithm
# https://leetcode.com/problems/maximum-product-subarray

# Min and max are tracked (hint: array can only increase (abs wise) going from left to right, only the sign changes)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        minVal, maxVal = 1, 1

        for num in nums:
            temp = minVal
            minVal = min(maxVal*num, minVal*num, num)
            maxVal = max(temp*num, maxVal*num, num)
            res = max(res, maxVal)
        
        return res
