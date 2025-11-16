# Floyd Warshall problem - easier version
# It relies on an intermediate value (k) to continiously update
# the shortest path between two nodes in a two by two matrix.

# Leetcode: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/?envType=problem-list-v2&envId=9idenloe

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[float('inf')]*n for i in range(n)]
        res = [float('-inf'), float('inf')] # City, number

        # n^3 floyd-Warshall algorithm 

        for s, d, w in edges:
            dp[s][d] = w
            dp[d][s] = w
        
        for i in range(n):
            dp[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        for city in range(n):
            count = 0
            for other_city in range(n):
                if city != other_city and dp[city][other_city] <= distanceThreshold:
                    count += 1
            if count <= res[1]:
                res = [max(res[0], city), count]

        return res[0]
        
