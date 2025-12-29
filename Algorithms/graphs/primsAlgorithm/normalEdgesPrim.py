# Network delay time
# Link: https://leetcode.com/problems/network-delay-time/

# Time: V log E 
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, 0)] # distance to point, point index
        res = 0
        mst = set()

        while heap:
            total, idx = heapq.heappop(heap)
            if idx in mst:
                continue
            mst.add(idx)
            res += total
            x1, y1 = points[idx]
            for i in range(len(points)):
                if i in mst:
                    continue
                x2, y2 = points[i]
                dist = abs(y2 - y1) + abs(x2 - x1)
                heapq.heappush(heap, (dist, i))

        return res
