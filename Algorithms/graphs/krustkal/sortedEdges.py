# Krustkal's algorithm to connect all points
# Link: https://leetcode.com/problems/min-cost-to-connect-all-points/

# Runttime: E log E, or V^2*log(V) 
# Since this is a connected graph, E ~ V^2, and it simplifies to above. Prim's is same, unless optimized (which is faster than this). 

# Comparison between both Prim's and Kruskal's: Both are most times same runttime
# Sparse Graph (E = O(V)):
#
#   Kruskal's Algorithm:
#       Time Complexity: O(E * log V)
#
#   Prim's Algorithm (Heap-based):
#       Time Complexity: O(E * log V)
#
#   -> Same asymptotic runtime on sparse graphs
#
#
# Dense Graph (E = O(V^2)):
#
#   Kruskal's Algorithm:
#       Time Complexity: O(V^2 * log V)
#
#   Prim's Algorithm (Heap-based):
#       Time Complexity: O(V^2 * log V)
#
#   Prim's Algorithm (Array-based):
#       Time Complexity: O(V^2)   # Optimal for dense graphs
#
#   -> Array-based Prim's is strictly better on dense graphs

# Must be undirected, can have neg cycle


class Dsu:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1]*n

    def find_parent(self, node):
        if self.parents[node] != node:
            return self.find_parent(self.parents[node])
        else:
            return node

    def union(self, n1, n2):
        pn1 = self.find_parent(n1)
        pn2 = self.find_parent(n2)
        if pn1 == pn2:
            return False
        if self.size[pn1] < self.size[pn2]:
            pn1, pn2 = pn2, pn1
        self.size[pn1] += self.size[pn2]
        self.size[pn2] = 0
        self.parents[pn2] = pn1
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = list()
        dsu = Dsu(len(points))
        res = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i < j: # Ensures only one edge is added (since it's undirected)
                    edges.append((abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        edges.sort()

        count = 0
        for i in range(len(edges)):
            if dsu.union(edges[i][1], edges[i][2]):
                res += edges[i][0]
                count += 1
            if count == len(points): # Stops early since MST is correct
                break

        return res
        
