# Turn negative number into positive was used in this problem
# Link: https://leetcode.com/problems/majority-element/

# The trick is at the end, subtracking by 1 << 32.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bits = [0] * 32
        half = len(nums) / 2
        res = 0

        for num in nums:
            for j in range(32):
                if num & (1 << j):
                    bits[j] += 1

        for i in range(32):
            res <<= 1
            if bits[31 - i] > half:
                res |= 1

        if res >= (1 << 31):
            res -= (1 << 32)
        
        return res
