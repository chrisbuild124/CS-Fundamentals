# 3 Sum on leetcode
# n^2 time complexity

# The trick here is sorting the matrix and using 3 pointers to loop through the entire array.
# Leetcode: https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        left = 0
        middle = 1
        right = len(nums) - 1

        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i
            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                if nums[i] + nums[middle] + nums[right] < 0:
                    middle += 1
                elif nums[i] + nums[middle] + nums[right] > 0:
                    right -= 1
                else:
                    output.append([nums[left], nums[middle], nums[right]])
                    middle += 1
                    right -= 1
                    while nums[middle] == nums[middle - 1] and middle < right:
                        middle += 1 
        return output
