# Classic Dijkstra
# Link: https://leetcode.com/problems/network-delay-time/description/

# Network Delay Time - this is classic dijkstra algorithm 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra: bfs: V*logE, Space: E
            # Adj: Make: E, space: E + V
        # Floyd Warshall: V^3 time, space: V
        # Bellman-Ford classic: Time: V*E, space: V
        # Bellman-Ford optimized: Average: (E + V), max: (E*V)

        # TLDR: Relaxes edges and uses a heap, but vertices can
        # be visited multiple times. 

        adj = defaultdict(list)
        distances = [float('inf')]*n
        distances[k-1] = 0
        heap = [(0, k)]
        for s, e, p in times:
            adj[s].append((e, p))
        
        while heap:
            total, node = heapq.heappop(heap)
            if distances[node-1] < total:
                continue
            
            for nei, p in adj[node]:
                if distances[node-1] + p < distances[nei-1]:
                    distances[nei - 1] = distances[node-1] + p
                    heapq.heappush(heap, (total + p, nei))

        return -1 if float('inf') in distances else max(distances)
