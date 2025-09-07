# Kth Largest Element in an Array
# runttime: nlogn is average but n^2 is worst
# leetcode: https://leetcode.com/problems/kth-largest-element-in-an-array/
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            pivot = nums[r]
            i = l
            for j in range(l, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        l, r = 0, len(nums) - 1

        def quickSort(l, r):
            if l < r:
                pivot = partition(l, r)
                quickSort(l, pivot-1)
                quickSort(pivot+1, r)
        quickSort(l, r)
        return nums[len(nums) - k]
