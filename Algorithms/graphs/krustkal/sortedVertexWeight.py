# Swim in rising water
# Link: https://leetcode.com/problems/swim-in-rising-water/description/

# This sorts based on each weight of the vertex. It is clever. 

class Dsu:
    def __init__(self, n):
        self.size = [1]*n
        self.parents = [i for i in range(n)]
    
    def find_parent(self, n):
        if self.parents[n] != n:
            return self.find_parent(self.parents[n])
        return n

    def union(self, n1, n2):
        pn1 = self.find_parent(n1)
        pn2 = self.find_parent(n2)
        if pn1 == pn2:
            return False
        if self.size[pn1] < self.size[pn2]:
            n1, n2, pn1, pn2 = n2, n1, pn2, pn1
        self.parents[pn2] = pn1
        self.size[pn1] += self.size[pn2]
        self.size[pn2] = 0
        return True

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def convert(i, j):
            return len(grid[0])*i + j
        DSU = Dsu(convert(len(grid)-1, len(grid[0])-1) + 1)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        positions = sorted((grid[r][c], r, c) for r in range(len(grid)) for c in range(len(grid[0])))

        for t, x, y in positions:
            for ox, oy in directions:
                nx, ny = x + ox, y + oy
                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                    continue
                if t >= grid[nx][ny]:
                    DSU.union(convert(x, y), convert(nx, ny))
            if DSU.find_parent(0) == DSU.find_parent(convert(len(grid) - 1, len(grid) - 1)):
                return t
