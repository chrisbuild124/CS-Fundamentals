# Find the Duplicate Number
# This uses Floyd's Tortoise and Hare Algorithm to solve

# The trick is to use the fast and slow pointers and 
# find the repeated value using the trick below. 

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Sol 1: Iterate through nums
            # If the nums[value-1] is not -1:
                # make -1
            # If it is -1
                # return value
            # [1,2,3,2,2]
            # Make pointer 1 and 2
            # check if num is > right
                # If ,move right
            # check if num is < left
                # if ,move left's right

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow
