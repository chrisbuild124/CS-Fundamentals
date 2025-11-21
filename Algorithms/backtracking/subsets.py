# Subsets leetcode problem (subsets algorithm)
# Link: https://leetcode.com/problems/subsets/description/

# This leetcode problem creates subsets of an array.
# Subset is any combination of elements

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []

        def dfs(i):
            if i >= len(nums):
                res.append(temp.copy())
                return
            temp.append(nums[i])
            dfs(i+1)
            temp.pop()
            dfs(i+1)
        dfs(0)
        return res
