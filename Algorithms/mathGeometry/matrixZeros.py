# Set matrix to zeros for col and row
# Link: https://leetcode.com/problems/set-matrix-zeroes/

# There are multiple tricks. One category of tricks is saving
# the memory into the array to get O(1) time complexity.
# Next, only save it to first row/col. Notice that we cannot
# save the first row's values and first col's values in 0, 0,
# so a temp value is made.

# After, check the middle values if they're 0 in their respective
# col/row. Then, do first row/col.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstRow = False
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        firstRow = True
                    else:
                        matrix[i][0] = 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0:
                    matrix[i][j] = 0
                if matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
        for i in range(len(matrix)):
            matrix[i][0] = 0
        
        if firstRow:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

