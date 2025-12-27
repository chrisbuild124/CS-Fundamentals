# Bellman Ford Algorithm
# Link: https://leetcode.com/problems/network-delay-time/

# Network Delay Time
# Runttime: O(E*V), Space: O(E)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra: bfs: V*logE, Space: E
            # Adj: Make: E, space: E + V
        # Floyd Warshall: V^3 time, space: V
        # Bellman-Ford classic: Time: V*E, space: V
        # Bellman-Ford optimized: Average: (E + V), max: (E*V)
        distances = [float('inf')] * n
        distances[k - 1] = 0
        
        for i in range(n):
            for s, e, p in times:
                distances[e - 1] = min(distances[e - 1], distances[s - 1] + p)
        return -1 if float('inf') in distances else max(distances)


