# Leetcode Combination Sum II
#

# The trick here is recognizing that repeating elements are not allowed, so 
# skip over it using the continue statement. Need to sort over the array
# for this to be possible. 

# NOTE: Can use temp as a global variable

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                res.append(temp.copy())
                return
            if total > target:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                temp.append(candidates[j])
                dfs(j+1, total + candidates[j])
                temp.pop()
        
        dfs(0, 0)
        return res
