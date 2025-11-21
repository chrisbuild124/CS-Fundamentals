# Jump game: A greedy problem
# Link: https://leetcode.com/problems/jump-game/description/

# The trick is to just move the goal post the farthest left and move backwards

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1 ,-1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False
