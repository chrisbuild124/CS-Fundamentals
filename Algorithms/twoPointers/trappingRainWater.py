# Trapping rainwater from leetcode

# The trick here is to use two pointers to get the max rain water
# Link: https://leetcode.com/problems/trapping-rain-water/description/ 


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        
        while l < r:
            if height[l] < height[r]:
                maxL = max(maxL, height[l])
                res += min(maxL, height[r]) - height[l]
                l += 1
            else:
                maxR = max(maxR, height[r])
                res += min(maxR, height[l]) - height[r]
                r -= 1       

        return res
