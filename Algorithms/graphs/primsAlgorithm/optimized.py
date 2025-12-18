# Leetcode find minimum cost to connect all points
# Link: https://leetcode.com/problems/min-cost-to-connect-all-points

# This is prim's but instead of using a heap, it uses an array. It's optimal
# for graphs that are near complete (doesn't need to be complete, but closer
# is needed). 
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Try Prim's alg (E * logE)
        # However, E = V^2 in this problem (dense graph, all nodes are connected)
        # V^2 * logV^2 = 2V^2logV = V^2logV
        # Doing an array of V^2 is < V^2logV

        # If it was at most sparse, then E = V, and then V*logV < V^2logV, therefore, use
        # the heap. 
        res = 0
        count = 1
        visit = {0}
        distances = [float('inf')]*len(points)
        next_node = 0

        while count < len(points):
            node = next_node
            for j in range(len(points)):
                dist = abs(points[node][0] - points[j][0]) + abs(points[node][1] - points[j][1])
                if distances[j] > dist and j != node:
                    distances[j] = dist
            next_node, next_dist = -1, float('inf')
            visit.add(node)
            for i in range(len(points)): # Find cheapest available node edge to node
                if i not in visit and distances[i] < next_dist:
                    next_node, next_dist = i, distances[i]
            res += next_dist
            count += 1

        return res
