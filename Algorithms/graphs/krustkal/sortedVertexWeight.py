# Swim in rising water
# Link: https://leetcode.com/problems/swim-in-rising-water/description/

# This sorts based on each weight of the vertex. It is clever. 

# Must be undirected, can have neg cycle

class DSU:
    def __init__(self, n):
        self.size = [1]*n
        self.parent = [i for i in range(n)]

    def find_parent(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find_parent(self.parent[n])
        return self.parent[n]
    
    def union(self, n1, n2):
        pn1, pn2 = self.find_parent(n1), self.find_parent(n2)
        if pn1 == pn2:
            return True
        if self.size[pn1] < self.size[pn2]:
            n1, n2 = n2, n1
            pn1, pn2 = pn2, pn1
        self.size[pn1] += self.size[pn2]
        self.size[pn2] = 0
        self.parent[pn2] = pn1
        return False

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid) * len(grid[0])
        Dsu = DSU(N)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = grid[0][0]
        heap = [(grid[0][0], 0, 0)]
        target = (len(grid) - 1, len(grid[0]) - 1)

        def convert(i, j):
            return i*len(grid) + j

        while heap:
            hei, x, y = heapq.heappop(heap)
            if (x, y) == target:
                return hei
            for ox, oy in directions:
                nx, ny = x + ox, y + oy
                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                    continue
                if not Dsu.union(convert(x, y), convert(nx, ny)):
                    heapq.heappush(heap, (max(hei, grid[nx][ny]), nx, ny))
