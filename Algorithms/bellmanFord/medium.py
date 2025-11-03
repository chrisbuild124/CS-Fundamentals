# Bellman Ford's algorithm
# Used to find shortest distance from one node to all other nodes in both negative and positive weighted graphs

# leetcode: https://leetcode.com/problems/cheapest-flights-within-k-stops/?envType=problem-list-v2&envId=9id9smj2
# Note: I believe djikstra's would be faster but this works with negative edges (this problem doesn't have negative edges though)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float('inf')]*n
        dp[src] = 0
        
        for _ in range(k+1):
            step = []
            for s, d, p in flights:
                if dp[s] != float('inf') and dp[s] + p < dp[d]:
                    step.append((d, dp[s] + p))
            for d, p in step:
                if p < dp[d]:
                    dp[d] = p
                
        return -1 if dp[dst] == float('inf') else dp[dst]
