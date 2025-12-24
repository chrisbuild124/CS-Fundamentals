# Find cheapeset flights within k stops
# Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

# NOTE: Uses a q to bfs and a cities array to find if that path is the cheapest so far 
# NOTE: It relaxes the edges iside the "cities" array
# O(E + V) average, O(E*V) worst
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman Ford Optimized, no neg cycles needed

        cities = [float('inf')]*n
        cities[src] = 0
        adj = defaultdict(list)
        for s, e, p in flights:
            adj[s].append((e, p))
        q = deque()
        q.append((src, 0, 0)) # Start, count, total

        while q:
            start, count, total = q.popleft()
            if count > k:
                continue
            for nei, p in adj[start]:
                if total + p < cities[nei]:
                    cities[nei] = total + p
                    q.append((nei, count + 1, total + p))

        return -1 if cities[dst] == float('inf') else cities[dst]
