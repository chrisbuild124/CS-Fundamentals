# Bellman Ford Algorithm
# Link: https://leetcode.com/problems/network-delay-time/

# Network Delay Time
# Runttime: average: O(E + V), worst: O(E*V), Space: O(E)

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Bellman ford, relaxes edges and takes E*V
        # E + V (average optimized)
        INF = float('inf')
        distances = [INF]*n
        distances[k - 1] = 0
        q = deque()
        q.append(k)
        adj = defaultdict(list)

        for s, e, p in times:
            adj[s].append((e, p))

        while q:
            node = q.popleft()
            for nei, edge in adj[node]:
                if distances[node - 1] + edge < distances[nei - 1]:
                    distances[nei - 1] = distances[node - 1] + edge
                    q.append((nei))

        return -1 if INF in distances else max(distances)
