# Longest Increasing Path In Matrix
# Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

# Solution is in NM which is better than a heap (constant time)
# NOTE: Solution is a DAG

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        N, M = len(matrix), len(matrix[0]) 
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        res = 1
        
        indegrees = [[0]*M for _ in range(N)]
        dp = [[1]*M for _ in range(N)]

        for x in range(N):
            for y in range(M):
                for ox, oy in directions:
                    nx, ny = x + ox, y + oy
                    if nx < 0 or ny < 0 or nx >= N or ny >= M:
                        continue
                    if matrix[x][y] > matrix[nx][ny]:
                        indegrees[x][y] += 1

        for x in range(N):
            for y in range(M):
                if indegrees[x][y] == 0:
                    q.append((x, y))

        while q:
            x, y = q.popleft()
            for ox, oy in directions:
                nx, ny = x + ox, y + oy
                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if matrix[x][y] < matrix[nx][ny]:
                    dp[nx][ny] = max(dp[nx][ny], 1 + dp[x][y])
                    res = max(res, dp[nx][ny])
                    indegrees[nx][ny] -= 1
                    if indegrees[nx][ny] == 0:
                        q.append((nx, ny))
        
        return res
