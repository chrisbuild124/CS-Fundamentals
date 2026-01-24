# Spiral Matrix pattern
# Link: https://leetcode.com/problems/spiral-matrix/description/

# The trick here is to change the l, r, t, b borders to get the new rectangle.
# Also change the l, r, t, b borders after use. 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        N, M = len(matrix), len(matrix[0])
        l, t, r, b = 0, 0, M - 1, N - 1
        res = []

        while l <= r and t <= b:
            for y in range(l, r + 1):
                res.append(matrix[t][y])
            t += 1
            for x in range(t, b + 1):
                res.append(matrix[x][r])
            r -= 1
            if t <= b:
                for y in range(r, l - 1, -1):
                    res.append(matrix[b][y])
            b -= 1
            if l <= r:
                for x in range(b, t - 1, -1):
                    res.append(matrix[x][l])
            l += 1

        return res
            
