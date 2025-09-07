# Kth Largest Element in an Array
# runttime: nlogn is average but n^2 is worst
# leetcode: https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            pivotIdx = r
            i = l
            for j in range(l, r):
                if nums[j] < nums[pivotIdx]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            print(i, nums)
            nums[i], nums[pivotIdx] = nums[pivotIdx], nums[i]
            return i
        
        l, r = 0, len(nums) - 1
        pivot = len(nums)
      # Uses a variation of binary search to find the correct value by going left or right of the pivot
        while pivot != len(nums) - k:
            pivot = partition(l, r)
            if pivot > len(nums) - k:
                r = pivot - 1
            else:
                l = pivot + 1
        return nums[pivot]
