# Leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Search in Rotated Sorted Array

# This problem is slightly more tricky and is an implimentation of binary sort
# It still relies on the sort and removing values

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l)//2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
