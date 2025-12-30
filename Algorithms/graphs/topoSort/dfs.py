# NOTES: Start at nodes with no directed nodes toward it, and move outward.
# DFS topological sort solution
# https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = defaultdict(list)
        res = []
        cycle = set() # Detects cycles
        visit = set() # Detects if course was already taken

        for b, a in prerequisites:
            adj[a].append(b)
            indegree[b] += 1

        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True
            cycle.add(i)
            visit.add(i)
            res.append(i)
            for nei in adj[i]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    if not dfs(nei):
                        return False
            cycle.remove(i)
            return True

        for i in range(numCourses):
            if indegree[i] == 0:
                if not dfs(i):
                    return []

        return res if len(res) == numCourses else []
