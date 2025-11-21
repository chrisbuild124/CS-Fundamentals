# Leetcode Permutations algorithm
# Link: https://leetcode.com/problems/permutations/description/

# Order does matter here and all values must be used. Note it uses
# a visited array and searches through entire array each dfs call. 

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        self.perm = []
        self.backtrack([False]*len(nums))
        return self.res
        
    def backtrack(self, visited):
        if len(self.perm) == len(self.nums):
            self.res.append(self.perm.copy())
            return
        
        for i in range(len(self.nums)):
            if not visited[i]:
                self.perm.append(self.nums[i])
                visited[i] = True
                self.backtrack(visited)
                self.perm.pop()
                visited[i] = False
