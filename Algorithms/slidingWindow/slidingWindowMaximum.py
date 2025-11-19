# MaxSlid
# Link: https://leetcode.com/problems/sliding-window-maximum/description/

# The trick is to use a deque to pop from the left/right and append to the right
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        returnList = []
        
        for i in range(len(nums)):        
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if queue and queue[0] <= i - k:
                queue.popleft()
        
            if i >= k - 1:
                returnList.append(nums[queue[0]])
        
        return returnList
