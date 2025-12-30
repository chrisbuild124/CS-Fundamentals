# NOTES: Start at nodes with no directed nodes toward it, and move outward.
# WORKS FOR: cyclic (detects if cyclic) and disjoint graphs
# https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Try bfs
        adj = defaultdict(list)
        for i in range(numCourses):
            adj[i] = []
        q = deque()
        res = []
        visit = set()
        cycle = set()

        for e, s in prerequisites:
            adj[e].append(s)

        def dfs(i):
            if i in visit:
                return True
            if i in cycle:
                return False
            cycle.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            cycle.remove(i)
            visit.add(i)
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res
