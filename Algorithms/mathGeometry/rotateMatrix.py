# Rotate a matrix by 90 degrees clockwise
# Link: https://leetcode.com/problems/rotate-image/

# The trick here is to transpose it and then reverse it. 
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        for i in range(N):
            for j in range(i + 1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(N):
            matrix[i] = matrix[i][::-1]
