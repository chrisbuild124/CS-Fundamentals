# NOTES: Start at nodes with no directed nodes toward it, and move outward.
# WORKS FOR: cyclic (detects if cyclic) and disjoint graphs
# https://leetcode.com/problems/course-schedule-ii/description/

from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inorder = [0]*numCourses
        adj = defaultdict(list)
        q = deque()
        res = []

        for b, a in prerequisites:
            adj[a].append(b)
            inorder[b] += 1

        for i in range(numCourses):
            if inorder[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                inorder[nei] -= 1
                if inorder[nei] == 0:
                    q.append(nei)

        return res if len(res) == numCourses else []
