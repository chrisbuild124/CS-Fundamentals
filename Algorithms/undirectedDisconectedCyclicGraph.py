# This is a cycle detection problem - a cyclic undirected disconnected graph 
# https://leetcode.com/problems/course-schedule/

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        map = defaultdict(list)
        for cor, pre in prerequisites:
            map[cor].append(pre)

        visit = set()
        
        def dfs(cor):
            if cor in visit:
                return False
            visit.add(cor)
            for pre in map[cor]:
                if dfs(pre) is False:
                    return False
            visit.remove(cor)
            map[cor] = []
            return True
        
        for cor, pre in prerequisites:
            if dfs(cor) is False:
                return False
            
        return True
