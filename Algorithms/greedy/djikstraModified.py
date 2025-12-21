# Swim in rising water
# Link: https://leetcode.com/problems/swim-in-rising-water/

# Instead of a classic djikstra's, it greedily picks the
# smallest edge each iteration (not the smallest maximum edge in path)
# This is faster than the classic djikstra but is special for this problem since
# it's greedy to only keep track of the current smallest height. 

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        target = (len(grid)-1, len(grid[0])-1)
        heap = [(grid[0][0], grid[0][0], 0, 0)] # Elevation, max el, i, j
        visit = {(0, 0)}
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        while heap:
            _, max_el, x, y = heapq.heappop(heap)
            if (x, y) == target:
                return max_el
            for ox, oy in directions:
                nx, ny = x + ox, y + oy
                if (nx, ny) in visit:
                    continue
                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                    continue
                heapq.heappush(heap, (grid[nx][ny], max(max_el, grid[nx][ny]), nx, ny))
                visit.add((nx, ny))
        
