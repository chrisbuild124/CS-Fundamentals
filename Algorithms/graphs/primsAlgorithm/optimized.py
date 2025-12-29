# Leetcode find minimum cost to connect all points
# Link: https://leetcode.com/problems/min-cost-to-connect-all-points

# This is prim's but instead of using a heap, it uses an array. It's optimal
# for graphs that are near complete (doesn't need to be complete, but closer
# is needed). 
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        INF = float('inf')
        N = len(points)
        distances = [INF]*N
        distances[0] = 0
        mst = {0}
        next_node = 0

        for _ in range(N):
            node = next_node
            x1, y1 = points[node][0], points[node][1]
            for j in range(N):
                if j in mst:
                    continue
                x2, y2 = points[j][0], points[j][1]
                dist = abs(y2 - y1) + abs(x2 - x1)
                distances[j] = min(distances[j], dist)
            next_node, dist = -1, INF
            for i in range(N):
                if i not in mst and distances[i] < dist:
                    next_node = i
                    dist = distances[i]
            mst.add(next_node)

        return sum(distances)
