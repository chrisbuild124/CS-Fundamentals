# Products of Array Except Self
# Leetcode: https://leetcode.com/problems/product-of-array-except-self/description/

# Basically, keep a memory of what came to the left and right product wise, then combine these
# in another loop. 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        newList = [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            right[len(nums) - i - 1] = right[len(nums) - i] * nums[len(nums) - i]
        for i in range(len(nums)):
            newList[i] = left[i] * right[i]
        return newList
