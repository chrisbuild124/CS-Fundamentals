# Modified dijkstra algorithm - it uses a visit set instead of a distances array
# and doesn't modify a distances array, it just requires the heap (E time)

# Link: https://leetcode.com/problems/network-delay-time/description/ 
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra: bfs: V*logE, Space: E
            # Adj: Make: E, space: E + V
        # Floyd Warshall: V^3 time, space: V
        # Bellman-Ford classic: Time: V*E, space: V
        # Bellman-Ford optimized: Average: (E + V), max: (E*V)

        # TLDR: Relaxes edges and uses a heap, and verticies
        # cannot be visited multiple times. 
        # Same runttime: ~ E log V

        adj = defaultdict(list)
        visit = set()
        heap = [(0, k)]
        for s, e, p in times:
            adj[s].append((e, p))
        
        while heap:
            total, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            if len(visit) == n:
                return total

            for e, p in adj[node]:
                heapq.heappush(heap, (total + p, e))
                
        return -1
