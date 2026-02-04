# Boyer Moore algirithm for finding most common element
# Link: https://leetcode.com/problems/majority-element/

# Basically keeps a tally for mahority element and always lands at 1 for majority element. 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore
        res = nums[0]
        count = 1

        for num in nums[1::]:
            if num == res:
                count += 1
            else:
                count -= 1
            if count <= 0:
                res = num
                count = 1
        
        return res
