# Leetcode: https://leetcode.com/problems/binary-search/description/

# This problem is the simplest to understand binary search.
# There are definetly other variations but the main idea is
# to cut portions out of the search since it can rule out
# values due to a value being less or more from sorting. 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # No edge cases at this time

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1
