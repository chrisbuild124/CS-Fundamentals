# This is dijkstra's algorithm, a pretty conventional problem.
# Basically uses BFS to find shortest path from one node to another.
# It cannot have negative weights on graph.

# Problem
# 2.	Apply graph traversal to solve a problem:
# You are presented with a 3-D puzzle defined by a 2D matrix called `puzzle[m][n]`. The length and breadth of the puzzle correspond to the dimensions of this matrix, while the height of each cell is determined by the value stored in that cell. Specifically, the value at `puzzle[row][column]` represents the height of the cell located at the coordinates `[row][column]`.

# Your starting position is at the top-left cell `[0][0]`, and your goal is to reach the bottom-right cell `[m-1][n-1]`. You can move in four directions: up, down, left, or right. Write an algorithm that allows you to reach the destination cell with minimal effort.

# Effort is defined as the maximum absolute difference between the heights of two consecutive cells along the path. For example, if a path crosses heights of 1, 3, 4, 6, 3, and 1, the absolute differences between consecutive cells would be calculated as follows: 
#  |1 - 3| = 2 
#  |3 - 4| = 1 
#  |4 - 6| = 2 
#  |6 - 3| = 3 
#  |3 - 1| = 2 

# This results in the values: {2, 1, 2, 3, 2}. Therefore, the maximum value of these absolute differences is 3. Consequently, the effort required on this path would be 3.


import heapq

def minEffort(puzzle):
    """This will find the shortest path from [0, 0] to
    [n-1, m-1]. The path's distance will be defined as
    the maximum absolute differende between a 
    consecutive cell in the puzzle to the next cell."""

    heap = [(0, 0, 0)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    res = 0
    visit = set()

    while heap:
        w, i, j = heapq.heappop(heap)
        if i == len(puzzle)-1 and j == len(puzzle[0])-1:
            res = w
            break
        visit.add((i, j))
        for ox, oy in directions:
            nx, ny = ox + i, oy + j
            if nx < 0 or ny < 0 or nx >= len(puzzle) or ny >= len(puzzle[0]):
                continue
            if (nx, ny) in visit:
                continue
            heapq.heappush(heap, (max(w, abs(puzzle[nx][ny] - puzzle[i][j])), nx, ny))

    return res

print(minEffort([[1, 3, 5], [2, 8, 3], [3, 4, 5]]))
