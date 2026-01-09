# Single number leetcode problem
# Link: https://leetcode.com/problems/single-number/

# Doing the XOR trick cancels out numbers

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res = res ^ num
        
        return res
