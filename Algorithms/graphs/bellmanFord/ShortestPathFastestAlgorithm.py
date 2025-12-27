# Bellman Ford Algorithm
# Link: https://leetcode.com/problems/network-delay-time/

# Network Delay Time
# Runttime: average: O(E + V), worst: O(E*V), Space: O(E)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra: bfs: V*logE, Space: E
            # Adj: Make: E, space: E + V
        # Floyd Warshall: V^3 time, space: V
        # Bellman-Ford classic: Time: V*E, space: V
        # Bellman-Ford optimized: Average: (E + V), max: (E*V)
        adj = defaultdict(list)
        for s, e, p in times:
            adj[s].append((e, p))
        distances = [float('inf')] * n
        distances[k - 1] = 0
        q = deque()
        q.append((0, k))
        
        while q:
            total, node = q.popleft()
            for nei, p in adj[node]:
                if distances[node - 1] + p < distances[nei - 1]:
                    q.append((total + p, nei))
                    distances[nei - 1] = total + p
        print(distances)
        return -1 if float('inf') in distances else max(distances)
