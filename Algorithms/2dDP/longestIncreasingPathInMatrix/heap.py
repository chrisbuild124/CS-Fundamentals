# Longest Increasing Path In Matrix
# Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

# Solution is in NM * logNM and uses a heap
# it's simpler but less efficient than the queue

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        N, M = len(matrix), len(matrix[0]) 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        heap = []
        res = 1
        dp = [[1]*(M) for _ in range(N)]


        for i in range(N):
            for j in range(M):
                heap.append((matrix[i][j], i, j))

        heapq.heapify(heap)

        while heap:
            cur, x, y = heapq.heappop(heap)
            for ox, oy in directions:
                nx, ny = x + ox, y + oy
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if cur > matrix[nx][ny]:
                    dp[x][y] = max(dp[x][y], 1 + dp[nx][ny])
                    res = max(res, dp[x][y])
        print(dp)
        return res



