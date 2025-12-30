# NOTES: Start at nodes with no directed nodes toward it, and move outward.
# WORKS FOR: cyclic (detects if cyclic) and disjoint graphs
# https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        check = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        res = []

        for s, p in prerequisites:
            check[s] += 1
            adj[p].append(s)

        def dfs(node):
            res.append(node)
            check[node] -= 1
            for nei in adj[node]:
                check[nei] -= 1
                if check[nei] == 0:
                    dfs(nei)
        
        for i in range(numCourses):
            if check[i] == 0:
                dfs(i)

        return res if len(res) == numCourses else []
