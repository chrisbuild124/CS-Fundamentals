# NOTES: Start at nodes with no directed nodes toward it, and move outward.
# WORKS FOR: cyclic (detects if cyclic) and disjoint graphs
# https://leetcode.com/problems/course-schedule-ii/description/

from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        check = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        q = deque()
        res = []

        for s, p in prerequisites:
            check[s] += 1
            adj[p].append(s)
        
        for i in range(numCourses):
            if check[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            for pre in adj[node]:
                check[pre] -= 1
                if check[pre] == 0:
                    q.append(pre)
            res.append(node)

        return res if len(res) == numCourses else []
