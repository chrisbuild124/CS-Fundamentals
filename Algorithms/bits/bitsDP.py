# A DP solution using bits: Partition Equal Subset Sum
# Link: https://leetcode.com/problems/partition-equal-subset-sum/

# Trick: To use each bit as a sum and constantly move over that amount
# of nums over in the number. The actual number value is not relevent. 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        dp = 1 << 0

        for num in nums:
            dp |= dp << num

        return True if (dp & (1 << total//2)) else False
