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
        INF = float('inf')
        distances = [INF]*n
        distances[k - 1] = 0
        q = deque()
        q.append((k, 0))
        adj = defaultdict(list)

        for s, e, p in times:
            adj[s].append((e, p))

        while q:
            node, p = q.popleft()
            for nei, edge in adj[node]:
                if distances[node - 1] + edge < distances[nei - 1]:
                    distances[nei - 1] = distances[node - 1] + edge
                    q.append((nei, distances[nei - 1]))

        return -1 if INF in distances else max(distances)
